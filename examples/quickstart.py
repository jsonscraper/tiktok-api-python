import os
from jsonscraper_tiktok import TikTok, APIError

client = TikTok(os.environ["JSONSCRAPER_TIKTOK_LICENSE_KEY"], timeout=30, retries=1)
try:
    response = client.get_user_info(query="therock", cache_timeout=60)
    if response.get("status") != "ok":
        raise RuntimeError("The API returned an application error")
    print(response["tiktok"])
except APIError as error:
    print(f"HTTP {error.status}; check your key, quota, or parameters")
