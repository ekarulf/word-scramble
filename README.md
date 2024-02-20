# word-scramble
Creates word scramble flash cards

Sample usage
```
$ ./build.sh ./words.txt
+ rm -rf build/template
+ mkdir -p build/
+ rsync -a template/ build/
+ cat sample/words.txt
+ python3 ./scramble.py
1   window  I O W W D N
2   year    R Y E A
3   letter  E R E T T L
[ . . . ]
+ weasyprint ./build/quiz.html ./build/quiz.pdf
+ weasyprint ./build/answer.html ./build/answer.pdf
```
