class TableRow:
    def __init__(self, isHeader = False):
        self.isHeader = isHeader
        self.elements = []
    def addElement(self, element):
        self.elements.append(element)
    def getHTML(self):
        html = '<tr>'
        for e in self.elements:
            if self.isHeader or e.isHeader:
                elTag = 'th'
            else:
                elTag = 'td'
            html += '<%s>' % elTag + e.getHTML() + '</%s>' % elTag
        html += '</tr>'
        return html

