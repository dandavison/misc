#!/bin/bash -eu
pdf=$1
pdftotext $pdf
cat ${pdf%%.pdf}.txt
