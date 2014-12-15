class Element:
    """ An data element of a row in a table """
    htmlCode = "";
    @staticmethod
    def imgToHTML(img_path, width = 200):
        return '<img src="' + img_path + ' width="' + str(width) + 'px" />'
    
    def addImg(self, img_path, width = 200):
        self.htmlCode += imgToHTML(img_path, width)

    def addTxt(self, txt):
        self.htmlCode += txt

    def getHTML(self):
        return self.htmlCode

