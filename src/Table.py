import csv
from Element import Element
from TableRow import TableRow

class Table:
    def __init__(self, rows = []):
        self.rows = [row for row in rows if not row.isHeader]
        self.headerRows = [row for row in rows if row.isHeader]
    def addRow(self, row):
        if not row.isHeader:
            self.rows.append(row)
        else:
            self.headerRows.append(row)
    def getHTML(self):
        html = '<table border=1>'
        for r in self.headerRows + self.rows:
            html += r.getHTML()
        html += '</table>'
        return html
    def readFromCSV(self, fpath):
        with open(fpath) as f:
            tablereader = csv.reader(f)
            for row in tablereader:
                tr = TableRow()
                for elt in row:
                    tr.addElement(Element(elt))
                self.addRow(tr)
    def countRows(self):
        return len(self.rows)

