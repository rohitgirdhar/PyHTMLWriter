class Element:
    """ A data element of a row in a table """

    def __init__(self, htmlCode = ""):
        self.htmlCode = htmlCode

    @staticmethod
    def imgToHTML(img_path, width = 200):
        return '<img src="' + img_path.strip().lstrip() + '" width="' + str(width) + 'px" />'
    
    def addImg(self, img_path, width = 200):
        self.htmlCode += self.imgToHTML(img_path, width)

    def addTxt(self, txt):
        self.htmlCode += txt

    def getHTML(self):
        return self.htmlCode

