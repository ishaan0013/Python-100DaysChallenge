# Merge pdf using pyPDF

from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs=['AI.pdf','ML.pdf']

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
