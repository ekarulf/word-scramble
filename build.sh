#!/bin/bash
set -euxo pipefail

rm -rf build/*
mkdir -p build/
rsync -a template/ build/

./scramble.py "$1" --verbose
weasyprint ./build/quiz.html ./build/quiz.pdf
weasyprint ./build/answer.html ./build/answer.pdf