import sys
sys.path.append('/home/rohit/Software/utils/PyHTMLWriter/src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter

t = Table()
print "NOTE that this is buggy still... will make images at the std size of canvas, and will put the square at absolute values mentioned"
for r in range(100):
    if r == 0:
        r = TableRow(isHeader = True)
    else:
        r = TableRow()
    for e in range(10):
        e = Element()
        # X, Y, W, H
        e.addImg("http://upload.wikimedia.org/wikipedia/commons/d/db/A_small_forest_clearing_-_geograph.org.uk_-_540354.jpg", [], [20,20,100,150])
        
        r.addElement(e)
    t.addRow(r)
tw = TableWriter(t, 'out')
tw.write()

