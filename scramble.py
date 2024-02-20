import fileinput
import random

from better_profanity import profanity
from jinja2 import Environment, FileSystemLoader, select_autoescape

def main():
    env = Environment(
        loader=FileSystemLoader("template"),
        autoescape=select_autoescape()
    )

    words = set()
    for line in fileinput.input():
        words.add(line.lower().strip())

    results = list()
    for number, word in enumerate(random.sample(sorted(words), len(words)), start=1):
        scrambled_word = word
        while scrambled_word == word or profanity.contains_profanity(scrambled_word):
            scrambled_letters = random.sample(word, len(word))
            scrambled_word = "".join(scrambled_letters)

        # add spaces into final output
        scrambled_word = " ".join(scrambled_letters).upper()

        results.append((number, word, scrambled_word))
        print(f"{number}\t{word}\t{scrambled_word}")

    for template_name in ["quiz.html", "answer.html"]:
        template = env.get_template(template_name)
        with open(f"build/{template_name}", "w") as page:
            html = template.render(results=results)
            page.write(html)


if __name__ == '__main__':
    main()