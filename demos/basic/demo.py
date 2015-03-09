import sys
sys.path.append('/home/rohit/Software/utils/PyHTMLWriter/src');
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
        e.addImg('http://rack.2.mshcdn.com/media/ZgkyMDE0LzAzLzMxL2UxL2VpZmZlbHRvd2VyLjYwMmIyLmpwZwpwCXRodW1iCTk1MHg1MzQjCmUJanBn/fe683380/ba4/eiffeltower.jpg')
        r.addElement(e)
    t.addRow(r)
tw = TableWriter(t, 'out')
tw.write()

