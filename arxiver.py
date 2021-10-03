import time
import arxiv
from googletrans import Translator
translator = Translator()
def doit(ys, cs):
    sb = arxiv.SortCriterion.SubmittedDate
    so = arxiv.SortOrder.Descending
    for c in cs:
        print('Category: ' + c)
        for y in ys:
            q = 'cat:' + c + ' '\
                'AND submittedDate:[' + y[0] + ' TO ' + y[1] + ']'
            print('From: '+y[0]+ ' To: '+y[1])
            try:
                cnt = 0
                p = arxiv.Search(query = q, sort_by = sb, sort_order = so)
                for r in p.results():
                    if 'attention' in r.title.lower():
                        cnt += 1
                        print('['+str(cnt)+'] '+r.title)
                        time.sleep(1)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    cs = ['cs.LG', 'cs.CV']
    ys = [['20210101','20210927'],
          ['20200101','20200927'],
          ['20190101','20190927'],
          #['20180101','20181231'],
          #['20170101','20171231'],
          #['20160101','20161231'],
          #['20150101','20151231'],
          #['20140101','20141231']
    ]
    doit(ys, cs)
