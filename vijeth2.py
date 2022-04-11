import requests
import json
import os

EMAIL = os.environ['EMAIL']
JIRA_API = os.environ['JIRA_API']


url = "https://vijeths.atlassian.net/rest/api/3/issue/SM-14"

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

r = requests.get(url, headers=headers, auth=(EMAIL, JIRA_API))

#print(r.text)
#print(type(r))


print(r.json())














# url = "https://chandratech.atlassian.net/rest/api/3/issue/Ap-17"
# # token = 'EqijvLWIwETIVbQXEgBFEA26'
# headers = {
#    "Accept": "application/json",
#    "Content-Type": "application/json"
# }

# r = requests.get(url, headers=headers, auth=(EMAIL_CHANDRA, API_CHANDRA))

# #print(r.text)
# #print(type(r))


# print(json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(",", ": ")))
