#!/usr/bin/python3
import requests
import re
def fetch_vote_count(userid, URL):
    r = requests.get(URL)
    m = re.search('<tr>\n    <td>\n' + userid + '    </td>\n    <td>\n([0-9]+)    </td>', r.text)
    if m:
        return m.group(1)
    else:
        print("Error: unable to parse current votes")
        return 0
