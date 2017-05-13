#!/usr/bin/python3
import requests
from  functions import fetch_vote_count

URL = "http://54.221.6.249/level1.php"
r = requests.get(URL)
key = r.cookies["HoldTheDoor"]
userid = "108"
start_votes = fetch_vote_count(userid, URL)
payload = {
    "id": userid,
    "holdthedoor": "Submit+Query",
    "key": key
}
for i in range(1):
    r = requests.post(URL, data=payload, cookies={"HoldTheDoor": key})
    print(i+1)
end_votes = fetch_vote_count(userid, URL)
votes_cast = int(end_votes) - int(start_votes)
print("Votes cast: {:d}".format(votes_cast))
