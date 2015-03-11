import random
import string
from PIL import Image
import urllib2 as urllib
import io

class Element:
    """ A data element of a row in a table """
    def __init__(self, htmlCode = ""):
        self.htmlCode = htmlCode
        self.isHeader = False
        self.drawCheck = False
        self.drawUnCheck = False

    def imgToHTML(self, img_path, width = 200):
        res = '<img src="' + img_path.strip().lstrip() + '" width="' + str(width) + 'px" '
        if self.drawCheck:
            res += 'style="border: 10px solid green"'
        if self.drawUnCheck:
            res += 'style="border: 10px solid red"'
        res += '/>'
        return res

    def imgToBboxHTML(self, img_path, bboxes, col='green', wid=300, ht=300, imsize = None):
        idd = "img_" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))

        # compute the ratios
        if imsize:
            actW = imsize[0]
            actH = imsize[1]
        else:
            actW, actH = self.tryComputeImgDim(img_path)
        actW = float(actW)
        actH = float(actH)
        if actW > actH:
            ht = wid * (actH / actW)
        else:
            wid = ht * (actW / actH)
        ratioX = wid / actW
        ratioY = ht / actH

        for i in range(len(bboxes)):
            bboxes[i] = [bboxes[i][0] * ratioX, bboxes[i][1] * ratioY, bboxes[i][2] * ratioX, bboxes[i][3] * ratioY]
        htmlCode = """
            <canvas id=""" + idd + """ style="border:1px solid #d3d3d3;
                background-image: url(""" + img_path + """);
                background-repeat: no-repeat;
                background-size: contain;"
                width=""" + str(wid) + """,
                height=""" + str(ht) + """>
           </canvas>
           <script>
                var c = document.getElementById(\"""" + idd + """\");
                var ctx = c.getContext("2d");
                ctx.lineWidth="2";
                ctx.strokeStyle=\"""" + col + """\";"""
        for i in range(len(bboxes)):
            htmlCode += """ctx.rect(""" + ",".join([str(i) for i in bboxes[i]]) + """);"""
        htmlCode += """ctx.stroke();
        </script>
        """
        return htmlCode
    
    def addImg(self, img_path, width = 200, bbox=None, imsize=None):
        # imsize is the natural size of image at img_path.. used for putting bboxes, not required otherwise
        # even if it's not provided, I'll try to figure it out -- using the typical use cases of this software
        if bbox:
            self.htmlCode += self.imgToBboxHTML(img_path, bbox, 'green', 300, 300, imsize)
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

    def setDrawCheck(self):
        self.drawCheck = True
    
    def setDrawUnCheck(self):
        self.drawUnCheck = True
 
    @staticmethod
    def tryComputeImgDim(impath):
        try:
            im = Image.open(impath)
            res = im.size
            return res
        except:
            pass
        try:
            # most HACKY way to do this, remove the first '../'
            # since most cases
            impath2 = impath[3:]
            im = Image.open(impath2)
            res = im.size
            return res
        except:
            pass
        try:
            # read from internet
            fd = urllib.urlopen(impath)
            image_file = io.BytesIO(fd.read())
            im = Image.open(image_file)
            return im.size
        except:
            pass
        print 'COULDNT READ THE IMAGE SIZE!'

