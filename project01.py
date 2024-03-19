import PyPDF2
import os  # fazer a manipulação dos arquivos

# faz a mesclagem dos pdfs
merger = PyPDF2.PdfMerger()

# pega os arquivos da pasta
lista_arquivos = os.listdir('arquivos')
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

merger.write("pdf final.pdf")