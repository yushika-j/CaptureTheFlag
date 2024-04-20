import hashlib
import re
import requests

# Fetch the data from the URL and set the cookies
response = requests.get("http://challenges.ringzer0team.com:10014/", cookies={"PHPSESSID": "8gkplmcji73umhvnourbcgmidj"})
data = response.text

# Extract the desired portion of the data using regex
data = re.search(r"(?<=BEGIN MESSAGE -----<br />\s{9})(.*)(?=<br />)", data).group(0)


# Compute the SHA-512 hash of the extracted message

data = requests.get("http://challenges.ringzer0team.com:10014/"+hashlib.sha512(data).hexdigest(), cookies={"PHPSESSID": "8gkplmcji73umhvnourbcgmidj"}).text
print(data)
