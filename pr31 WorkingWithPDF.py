import PyPDF2

a = PyPDF2.PdfFileReader('files/java.pdf')
# print(a.documentInfo)
# print(a.getNumPages())

# print(a.getPage(0).extractText())

sstr = ""
for i in range(1, 5):
    sstr += a.getPage(i).extractText()

# print(sstr)

with open("files/java.txt", "w", encoding='utf-8') as f:
    f.write(sstr)
