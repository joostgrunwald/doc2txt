#pip install docx2txt
import docx2txt

# extract text
text = docx2txt.process("AD-april-0005.docx")

# correct for double newlines present
text = text.replace("\n\n", "\n")
text = text.replace("\n\n", "\n")

# print text
with open('readme.txt', 'w') as f:
    f.write(text)
