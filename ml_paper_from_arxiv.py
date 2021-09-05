import arxiv
import time
import pprint
import pytz
import datetime
import slackweb
from tqdm import tqdm
from googletrans import Translator
translator = Translator()

def main():
    try:
        dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        dt_old = dt_now - datetime.timedelta(days=7)
        dt_all = dt_old.strftime('%Y%m%d%H%M%S')
        dt_day = dt_old.strftime('%Y%m%d')
        dt_hour = dt_old.strftime('%H')
        if dt_hour == '00':
            dt_last = dt_day + '115959'
            paper = arxiv.Search(
                query = 'cat:cs.cv AND submittedDate:[{} TO {}]'.format(dt_day, dt_last),
                sort_by = arxiv.SortCriterion.SubmittedDate,
                sort_order = arxiv.SortOrder.Descending)
        else:
            dt_last = dt_day + '235959'
            paper = arxiv.Search(
                query = 'cat:cs.cv AND submittedDate:[{} TO {}]'.format(dt_day, dt_last),
                sort_by = arxiv.SortCriterion.SubmittedDate,
                sort_order = arxiv.SortOrder.Descending)

        for result in paper.results():
            title = result.title
            pdf = result.pdf_url
            summary = result.summary
            summary = ''.join(summary.splitlines())
            summary_ja = translator.translate(summary, src='en', dest='ja')
            summary_ja = str(summary_ja.text)
            print(title)
            print(summary + '\n')
            print(summary_ja + '\n\n')
            attachments_title = []
            attachments_contents = []
            paper_title = {"title": title,
                    "text": pdf}
            paper_contents = {"title": summary,
                    "text": summary_ja}
            attachments_title.append(paper_title)
            attachments_contents.append(paper_contents)
            #slack = slackweb.Slack(url="")
            #slack.notify(attachments=attachments_title)

            time.sleep(1)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
