from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    def handle_comment(self,data):
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("/tAt line: ", pos[0], " position", p[1])




def main():
    parser = myHTMLParser()
    f = open("samplehtml.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

if __name__=="__main__":
    main()