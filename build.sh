#!/bin/bash
set -euxo pipefail

rm -rf build/*
mkdir -p build/
rsync -a template/ build/

cat "$1" | python3 ./scramble.py
weasyprint ./build/quiz.html ./build/quiz.pdf
weasyprint ./build/answer.html ./build/answer.pdf