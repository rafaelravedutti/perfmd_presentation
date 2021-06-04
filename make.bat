set TEXINPUTS=.\themefau

pdflatex presentation.tex
biber presentation
pdflatex presentation.tex

del *.aux *.bbl *.bcf *.blg *.nav *.out *.snm *.log *.toc *.vrb
exit
