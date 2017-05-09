#!/usr/bin/python3
import requests
import re
def fetch_vote_count(userid):
    URL = "http://54.221.6.249/level0.php"
    r = requests.get(URL)
    m = re.search('<tr>\n    <td>\n' + userid + '    </td>\n    <td>\n([0-9]+)    </td>', r.text)
    if m:
        return m.group(1)
    else:
        print("Error: unable to parse currewnt votes")
        return 0
