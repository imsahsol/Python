with open('NewTextDocument.txt','w') as new_text:
    new_text.write('Hello World')

with open('New_Text_Document.txt','r+') as text1:
    data = text1.read()
    print(data)
    text1.write('and also, sepjackticy')
    jack = text1.read()
    print(jack)
