class TableRow:
    def __init__(self, isHeader = False):
        self.isHeader = isHeader
        self.elements = []
    def addElement(self, element):
        self.elements.append(element)
    def getHTML(self):
        elTag = 'td'
        if self.isHeader:
            elTag = 'th'
        html = '<tr>'
        for e in self.elements:
            html += '<%s>' % elTag + e.getHTML() + '</%s>' % elTag
        html += '</tr>'
        return html

