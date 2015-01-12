import random
import string

class Element:
    """ A data element of a row in a table """
    def __init__(self, htmlCode = ""):
        self.htmlCode = htmlCode
        self.isHeader = False

    @staticmethod
    def imgToHTML(img_path, width = 200):
        return '<img src="' + img_path.strip().lstrip() + '" width="' + str(width) + 'px" />'
    def imgToBboxHTML(self, img_path, bbox):
        idd = "img_" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
        return """
            <canvas id=""" + idd + """ style="border:1px solid #d3d3d3;
                background-image: url(""" + img_path + """);
                background-repeat: no-repeat;
                background-size: 100% 100%;">
           </canvas>
           <script>
                var c = document.getElementById(\"""" + idd + """\");
                var ctx = c.getContext("2d");
                ctx.rect(""" + ",".join([str(i) for i in bbox]) + """);
                ctx.stroke();
        </script>
        """
    
    def addImg(self, img_path, width = 200, bbox=None):
        if bbox:
            self.htmlCode += self.imgToBboxHTML(img_path, bbox)
        else:
            self.htmlCode += self.imgToHTML(img_path, width)

    def addTxt(self, txt):
        if self.htmlCode: # not empty
                self.htmlCode += '<br />'
        self.htmlCode += str(txt)

    def getHTML(self):
        return self.htmlCode

    def setIsHeader(self):
        self.isHeader = True

