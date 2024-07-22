from urllib.request import urlopen

from bs4 import BeautifulSoup

from config import settings


def parse_plaza_tara(theatre, url):
    if theatre == 'plaza':
        url_to_scrape = url + '/now-showing'
    elif theatre == 'tara':
        url_to_scrape = url + '/home'
    page = urlopen(url_to_scrape).read()
    soup = BeautifulSoup(page, 'lxml')
    title_url = url + '/movie/'
    ticket_url = url + '/checkout/showing'

    todays_screenings = []
    for p in soup.find_all('p'):
        if '<p>NOW PLAYING' in str(p):
            screenings = str(p).split('\n')
            for screening in screenings[1:]:
                screening_info, times = {}, []
                screening_soup = BeautifulSoup(
                    screening, 'lxml'
                )
                for link in screening_soup.find_all('a'):
                    if title_url in link.get('href'):
                        screening_info['title'] = link.string
                    elif ticket_url in link.get('href'):
                        times.append(str(link))
                screening_info['times'] = ', '.join(times)
                todays_screenings.append(screening_info)

    screenings_html = ''
    for movie in todays_screenings:
        film_html = '<b>' + movie['title'] + '</b>: '
        for time in movie['times']:
            film_html += time
        film_html += '<br />'
        screenings_html += film_html
    
    return screenings_html