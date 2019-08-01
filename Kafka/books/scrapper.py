from bs4 import BeautifulSoup as soup
import requests
import csv


source = requests.get('http://coreyms.com').text

# source variable is equals to html of the html site

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])



soup = soup(source,'lxml')
for article in soup.find_all('article'):




    try:
        headline = article.header.h2.a.text

        summary = article.find('div', class_='entry-content')

        defi = summary.p.text

        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4].split('?')
        youtube_link = 'https://youtube.com/watch?v={0}'.format(vid_id[0])
    except Exception as e:
        headline, summary , defi, vid_src, vid_id, youtube_link = None


    print(headline)
    print(defi)
    print(youtube_link)
    print("    ")

    csv_writer.writerow([headline,defi,youtube_link])


csv_file.close()




