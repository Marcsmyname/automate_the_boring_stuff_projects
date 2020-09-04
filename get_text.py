#! python3
#Get Text function
#Marc Leon
#9/4/2020
'''
This gets all of the text form a docx file and magically makes it a string. 

'''

import docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

#enter the name of the file in the next line between the quotations
print(getText('C:\\Users\\Marc\\MyPythonScripts\\demo5.docx'))
