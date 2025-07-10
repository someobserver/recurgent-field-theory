#!/bin/sh
cd $(dirname $0)
xelatex -interaction=nonstopmode recurgent_field_theory.tex
biber recurgent_field_theory
xelatex -interaction=nonstopmode recurgent_field_theory.tex
xelatex -interaction=nonstopmode recurgent_field_theory.tex
