import os
from jsonscraper_tiktok import TikTok
client = TikTok(os.environ["JSONSCRAPER_TIKTOK_LICENSE_KEY"])
response = client.request("/searchVideo", **{'keyword': 'nature', 'count': 10, 'cache_timeout': 60})
print(response)
