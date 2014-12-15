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
    def countRows(self):
        return len(self.rows)

