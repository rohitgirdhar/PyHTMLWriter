import sys
sys.path.append('/media/data-nix/work/side/PyHTMLWriter/src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter

t = Table()
for i in range(100):
    if i == 0:
        r = TableRow(isHeader = True)
    else:
        r = TableRow(rno = i)
    for e in range(10):
        e = Element()
        e.setDrawCheck()
        e.addImg('../eiffeltower.jpg', bboxes=[[900,500,50,34],[100,100,100,100]])
        r.addElement(e)
    t.addRow(r)
tw = TableWriter(t, 'out')
tw.write()

