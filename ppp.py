import PyPDF2
a=PyPDF2.PdfReader("sample.pdf")
print(a.metadata)
print(len(a.pages))
str=""
for i in range(1):
  str+=a.pages[i].extract_text() 
print(str)  
with open("hp.txt","w",encoding='utf-8')as f:
 f.write(str)