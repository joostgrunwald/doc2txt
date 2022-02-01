#pip install docx2txt
import docx2txt
import os

#SETTINGS
directory = "C:\Users\joost\Desktop"

#MAIN
def main()
    output_directory = directory + "\txt" 

    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
             # print(os.path.join(directory, filename))
            continue
        else:
            continue
    # extract text
    text = docx2txt.process("AD-april-0005.docx")

    # correct for double newlines present
    text = text.replace("\n\n", "\n")
    text = text.replace("\n\n", "\n")

    # print text
    with open('readme.txt', 'w') as f:
        f.write(text)

main()
