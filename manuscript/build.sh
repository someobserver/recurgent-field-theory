#!/bin/sh
cd $(dirname $0)
xelatex -interaction=nonstopmode recurgence.tex
bibtex recurgence
xelatex -interaction=nonstopmode recurgence.tex
xelatex -interaction=nonstopmode recurgence.tex
