import os
from jsonscraper_tiktok import TikTok
client = TikTok(os.environ["JSONSCRAPER_TIKTOK_LICENSE_KEY"])
response = client.request("/getUserFeed", **{'query': 'therock', 'count': 10, 'max_cursor': '', 'cache_timeout': 60})
print(response)
