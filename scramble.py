#!/usr/bin/env python3

import argparse
import logging
import os.path
import random

from better_profanity import profanity
from jinja2 import Environment, FileSystemLoader, select_autoescape

try:
    from DictionaryServices import DCSCopyTextDefinition
except:
    DCSCopyTextDefinition = None

logger = logging.getLogger(__name__)

def is_valid_word(word, scrambled_word, checkDictionary=True):
    # If the word was not scrambled, scramble again
    if word == scrambled_word:
        logger.debug(f"Refusing to scramble {word} into {scrambled_word} as it was not scrambled")
        return False

    # If the word is profane, scramble again
    if profanity.contains_profanity(scrambled_word):
        logger.debug(f"Refusing to scramble {word} into {scrambled_word} as it contains profanity")
        return False

    # If the word is an English word, scramble again
    if checkDictionary and is_dictionary_word(scrambled_word):
        logger.debug(f"Refusing to scramble {word} into {scrambled_word} as it is found in the dictionary")
        return False

    return True

def is_dictionary_word(word):
    if DCSCopyTextDefinition is None:
        raise RuntimeError("Unable to load OS X Dictionary")

    return DCSCopyTextDefinition(None, word, (0, len(word))) is not None


def scramble_word(word):
    # typo protection: don't try and scramble a word without an answer
    if not is_dictionary_word(word):
        raise ValueError(f"{word} is not a valid word to scramble")

    rejected = set([word])
    for num in range(100):
        scrambled_letters = random.sample(word, len(word))
        scrambled_word = "".join(scrambled_letters)
        if scrambled_word in rejected:
            continue
        elif not is_valid_word(word, scrambled_word, checkDictionary=True):
            rejected.add(scrambled_word)
        else:
            break
    else:
        logger.debug(f"Unable to scramble {word} without a dictionary match... disabling check and trying again")
        # If we didn't have any matches, disable the dictionary check and try again
        while not is_valid_word(word, scrambled_word, checkDictionary=False):
            scrambled_letters = random.sample(word, len(word))
            scrambled_word = "".join(scrambled_letters)

    # the final output should be upper case and space delimited
    return " ".join(scrambled_letters).upper()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('wordlist', type=argparse.FileType('r'))
    parser.add_argument("--verbose", help="print additional debugging information", action="store_true")
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        level=log_level
    )

    env = Environment(
        loader=FileSystemLoader("template"),
        autoescape=select_autoescape()
    )

    # read & shuffle wordlist passed in as an argument
    words = [line.lower().strip() for line in args.wordlist]
    random.shuffle(words)

    # scramble each word in the wordlist
    results = [(number, word, scramble_word(word)) for number, word in enumerate(words, start=1)]

    # if verbose output requested, print the answer key to the commandline
    if args.verbose:
        for number, word, scrambled_word in results:
            print("\t".join((str(number), word, scrambled_word)))

    # render the quiz and answer templates into the build/ folder
    for template_name in ["quiz.html", "answer.html"]:
        template = env.get_template(template_name)
        with open(os.path.join("build", template_name), "w") as page:
            html = template.render(results=results)
            page.write(html)


if __name__ == '__main__':
    main()