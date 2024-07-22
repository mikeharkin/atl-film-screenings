import re

import utils


tara_html = utils.parse_plaza_tara(
    'tara', 'https://www.taraatlanta.com')
plaza_html = utils.parse_plaza_tara(
    'plaza', 'https://www.plazaatlanta.com'
)

site_html = f"""
    <html>
        <head>
            <title>Film Screenings in Atlanta</title>
        </head>
        <body>
            <h1>Movies Showing Today in Atlanta, GA<h1>
            <h2>Tara Theatre</h2>
            2345 Cheshire Bridge Rd NE
            Atlanta, GA 30324
            <br />
            (470) 567-1968
            <br /><br />
            {tara_html}
            <h2>Plaza Theatre</h2>
            1049 Ponce De Leon Ave NE
            Atlanta, GA 30306
            <br />
            (470) 410-1939
            <br /><br />
            {plaza_html}
        </body>
    </html>
"""

with open('index.html', 'w') as f:
    f.write(site_html)
    f.close()