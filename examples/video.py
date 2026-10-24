import os
from jsonscraper_tiktok import TikTok
client = TikTok(os.environ["JSONSCRAPER_TIKTOK_LICENSE_KEY"])
response = client.request("/getVideoByID", **{'video_id': '7106855913906081070', 'cache_timeout': 60})
print(response)
