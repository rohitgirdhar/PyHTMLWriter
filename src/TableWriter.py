import os
from Table import Table
import errno

class TableWriter:
    def __init__(self, table, outputdir, rowsPerPage = 20):
        self.outputdir = outputdir
        self.rowsPerPage = rowsPerPage
        self.table = table
    def write(self):
        self.mkdir_p(self.outputdir)
        nRows = self.table.countRows()
        counter = 1
        for i in range(0, nRows, self.rowsPerPage):
            rowsSubset = self.table.rows[i : i + self.rowsPerPage]
            t = Table(self.table.headerRows + rowsSubset)
            f = open(os.path.join(self.outputdir, str(counter) + '.html'), 'w')
            f.write(t.getHTML())
            f.close()
            counter += 1
    @staticmethod
    def mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

