# /opt/conda/envs/pytorch/lib/python3.6/site-packages/arxiv/arxiv.py
import time
import datetime
import arxiv
from googletrans import Translator
def doit(ys, cs):
    ts = Translator(service_urls=['translate.googleapis.com'])
    sb = arxiv.SortCriterion.SubmittedDate
    so = arxiv.SortOrder.Descending
    paper_list = []
    for c in cs:
        for y in ys:
            q = 'cat:' + c + ' '\
                'AND submittedDate:[' + y[0] + ' TO ' + y[1] + ']'
            print('From: '+y[0]+ ' To: '+y[1])
            try:
                cnt = 0
                p = arxiv.Search(query = q, sort_by = sb, sort_order = so)
                for r in p.results():
                    title = r.title
                    summary = r.summary
                    url = r.entry_id
                    published = str(r.published)
                    if 'multimodal' in title.lower() or \
                       'multimodal' in summary.lower():
                        if title not in paper_list:
                            paper_list.append(title)
                            print('[Multimoda]')
                            print(published+'\n'+title+'\n'+url+'\n')
                    if 'transformer' in title.lower() or \
                       'transformer' in summary.lower():
                        if title not in paper_list:
                            paper_list.append(title)
                            print('[Transformer]')
                            print(published+'\n'+title+'\n'+url+'\n')
                    if 'attention' in title.lower() or \
                       'attention' in summary.lower():
                        if title not in paper_list:
                            paper_list.append(title)
                            print('[Attention]')
                            print(published+'\n'+title+'\n'+url+'\n')
                    if 'GAN ' in title or 'GAN ' in summary:
                        if title not in paper_list:
                            paper_list.append(title)
                            print('[GAN]')
                            print(published+'\n'+title+'\n'+url+'\n')
                    if 'GPT' in title or 'GPT' in summary:
                        if title not in paper_list:
                            paper_list.append(title)
                            print('[GPT]')
                            print(published+'\n'+title+'\n'+url+'\n')
                    if 'DALL-E' in title or 'DALL-E' in summary:
                        if title not in paper_list:
                            paper_list.append(title)
                            print('[DALL-E]')
                            print(published+'\n'+title+'\n'+url+'\n')
                    if 'BERT' in title or 'BERT' in summary:
                        if title not in paper_list:
                            paper_list.append(title)
                            print('[BERT]')
                            print(published+'\n'+title+'\n'+url+'\n')
                    time.sleep(10)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    today = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d')
    week =  (datetime.date.today() -
             datetime.timedelta(days=7)).strftime('%Y%m%d')
    cs = ['cs.LG','cs.CV','cs.AI']
    ys = [[week,today],
          #['20211010','20211021'],
          #['20200101','20200927'],
          #['20190101','20190927'],
          #['20180101','20181231'],
          #['20170101','20171231'],
          #['20160101','20161231'],
          #['20150101','20151231'],
          #['20140101','20141231']
    ]
    doit(ys, cs)
