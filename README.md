# word-scramble
Creates word scramble flash cards

Sample usage
```
ekarulf-mac$ ./build.sh sample/words.txt
+ rm -rf build/answer.html build/answer.pdf build/firasans-bold.otf build/firasans-italic.otf build/firasans-light.otf build/firasans-lightitalic.otf build/firasans-regular.otf build/page.css build/quiz.html build/quiz.pdf
+ mkdir -p build/
+ rsync -a template/ build/
+ ./scramble.py sample/words.txt --verbose
02-20 08:19 DEBUG    Refusing to scramble car into arc as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble car into rca as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble came into emac as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble came into mace as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble eat into eta as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble for into fro as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble are into era as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble arm into amr as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble arm into mra as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble arm into mar as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble arm into rma as it is found in the dictionary
02-20 08:19 DEBUG    Refusing to scramble arm into ram as it is found in the dictionary
02-20 08:19 DEBUG    Unable to scramble arm without a dictionary match... disabling check and trying again
1   found   D U N O F
2   soon    O O N S
3   own O N W
4   garden  D G A N R E
5   paper   R A P E P
[ . . . ]
68  about   A B U O T
69  cowboy  W B Y O C O
70  boat    A B T O
+ weasyprint ./build/quiz.html ./build/quiz.pdf
+ weasyprint ./build/answer.html ./build/answer.pdf
```
