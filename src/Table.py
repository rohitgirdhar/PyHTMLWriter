import csv
import os
import inspect
import string
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
    def getHTML(self, makeChart = False, transposeTableForChart = False):
        html = '<table border=1 id="data">'
        for r in self.headerRows + self.rows:
            html += r.getHTML()
        html += '</table>'
        if makeChart:
            html += self.genChart(transposeTable=transposeTableForChart)
        return html
    def readFromCSV(self, fpath, scale=1.0):
        with open(fpath) as f:
            tablereader = csv.reader(f)
            for row in tablereader:
                tr = TableRow()
                for elt in row:
                    try:
                        tr.addElement(Element(str(float(elt) * scale)))
                    except:
                        tr.addElement(Element(elt))
                self.addRow(tr)
    def countRows(self):
        return len(self.rows)
    def genChart(self, transposeTable=False):
        # Generate HighCharts.com chart using the table
        # data. Assumes that data is numeric, and first row
        # and the first column are headers
        for row in self.rows:
            row.elements[0].setIsHeader()
        scrdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        f = open(os.path.join(scrdir, '../templates/highchart_js.html'))
        base_js =  string.Template(f.read()).safe_substitute({'transpose': 'true'} if transposeTable else {'transpose': 'false'})
        f.close()
        return base_js

