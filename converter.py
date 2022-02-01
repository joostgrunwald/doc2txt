#pip install docx2txt
import docx2txt
import os

#SETTINGS
directory = "C:\\Users\\joost\\Desktop\\werkmap"

#MAIN
def main():

    #we write the converted file to this path
    output_directory = directory + "\\txt"

    #we first check if the path exists and make it if it does not exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    #we iterate over all files in the given folder with extension .docx
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            
            #DEBUG
            #print(os.path.join(directory, filename))
             
            # extract text
            input_path = directory + "\\" + filename
            text = docx2txt.process(input_path)

            # correct for double newlines present
            text = text.replace("\n\n", "\n")

            # create needed output path
            output_filename = filename.replace(".docx",".txt")
            output_path = output_directory + "\\" + output_filename

            # write output
            with open(output_path, 'w') as f:
                f.write(text)

if __name__ == "__main__":
    main()
