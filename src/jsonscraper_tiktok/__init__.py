"""Official jsonscraper API clients. License keys stay on the server."""
import json
import math
import re
import time
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError, URLError

class APIError(Exception):
    def __init__(self, status, retry_after=None):
        self.status = status
        self.retry_after = retry_after
        super().__init__(f"jsonscraper API returned HTTP {status}")

class TransportError(Exception):
    pass

class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

class Client:
    def __init__(self, license_key, *, base_url=None, timeout=30, retries=0, cache_timeout=None):
        if not isinstance(license_key, str) or not license_key.strip():
            raise ValueError("A license key is required")
        base_url = base_url or 'https://tiktok.evelode.com'
        url = urlsplit(base_url)
        if url.scheme not in ("https", "http") or not url.netloc or url.username or url.password or url.query or url.fragment:
            raise ValueError("Invalid base URL")
        if url.scheme != "https" and url.hostname not in ("localhost", "127.0.0.1", "::1"):
            raise ValueError("HTTPS is required outside localhost")
        if not math.isfinite(timeout) or timeout <= 0 or not isinstance(retries, int) or not 0 <= retries <= 5:
            raise ValueError("Invalid timeout or retries")
        self._key, self.base_url = license_key, base_url.rstrip("/")
        self.timeout, self.retries, self.cache_timeout = timeout, retries, cache_timeout
        self._opener = build_opener(_NoRedirect())

    def request(self, path, **params):
        if not isinstance(path, str) or not re.fullmatch(r"/[A-Za-z0-9_/-]+", path) or ".." in path or "//" in path:
            raise ValueError("Use an API path, not a URL")
        params = {k: v for k, v in params.items() if v is not None and k != "license_key"}
        if self.cache_timeout is not None:
            params.setdefault("cache_timeout", self.cache_timeout)
        params["license_key"] = self._key
        query = urlencode({k: str(v).lower() if isinstance(v, bool) else v for k, v in params.items()}, doseq=True)
        req = Request(self.base_url + path + "?" + query, headers={"Accept": "application/json", "User-Agent": "jsonscraper-python/0.1.1"})
        for attempt in range(self.retries + 1):
            try:
                with self._opener.open(req, timeout=self.timeout) as response:
                    body = response.read()
                    if "json" not in response.headers.get("Content-Type", "").lower():
                        return body
                    try:
                        return json.loads(body)
                    except (ValueError, UnicodeError):
                        raise TransportError("Invalid JSON response") from None
            except HTTPError as error:
                status, header = error.code, error.headers.get("Retry-After")
                error.close()
                delay = min(60, int(header)) if header and header.isdigit() else min(2 ** attempt, 30)
                if attempt == self.retries or status not in (429, 502, 503, 504):
                    raise APIError(status, header) from None
                time.sleep(delay)
            except (URLError, TimeoutError, OSError):
                raise TransportError("Unable to reach jsonscraper API") from None

class TikTok(Client):
    def __init__(self, license_key, **options):
        super().__init__(license_key, **options)

    def get_no_watermark_url(self, **params):
        """Get non watermarked video url. See docs/endpoints.md for parameters."""
        return self.request("/getNoWatermarkUrl", **params)

    def get_no_watermark_url_by_id(self, **params):
        """Get non watermarked video url by video ID. See docs/endpoints.md for parameters."""
        return self.request("/getNoWatermarkUrlByID", **params)

    def get_video_by_id(self, **params):
        """Get video info by ID. See docs/endpoints.md for parameters."""
        return self.request("/getVideoByID", **params)

    def get_video_by_url(self, **params):
        """Get video info by URL. See docs/endpoints.md for parameters."""
        return self.request("/getVideoByUrl", **params)

    def get_unshortened_url(self, **params):
        """Convert short TikTok video URL to full TikTok video URL. See docs/endpoints.md for parameters."""
        return self.request("/getUnshortenedUrl", **params)

    def get_comments_by_url(self, **params):
        """Get comments list by video URL. See docs/endpoints.md for parameters."""
        return self.request("/getCommentsByUrl", **params)

    def get_comments_by_id(self, **params):
        """Get comments list by video ID. See docs/endpoints.md for parameters."""
        return self.request("/getCommentsByID", **params)

    def get_comments_replies(self, **params):
        """Get comments replies. See docs/endpoints.md for parameters."""
        return self.request("/getCommentsReplies", **params)

    def search_user(self, **params):
        """Search for user by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchUser", **params)

    def search_video(self, **params):
        """Search for video by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchVideo", **params)

    def search_music(self, **params):
        """Search for music by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchMusic", **params)

    def search_live(self, **params):
        """Search for live by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchLive", **params)

    def search_hashtag(self, **params):
        """Search for hashtag by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchHashtag", **params)

    def search_location(self, **params):
        """Search for location by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchLocation", **params)

    def search_top(self, **params):
        """Top search by text query. See docs/endpoints.md for parameters."""
        return self.request("/searchTop", **params)

    def search_insights(self, **params):
        """Search insights by text query. See docs/endpoints.md for parameters."""
        return self.request("/searchInsights", **params)

    def search_comment_suggested_users(self, **params):
        """Search comment suggested users. See docs/endpoints.md for parameters."""
        return self.request("/searchCommentSuggestedUsers", **params)

    def get_user_info(self, **params):
        """Get user info by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getUserInfo", **params)

    def get_user_info_by_id(self, **params):
        """Get user info by profile ID. See docs/endpoints.md for parameters."""
        return self.request("/getUserInfoByID", **params)

    def get_basic_user_info(self, **params):
        """Get user info by username. See docs/endpoints.md for parameters."""
        return self.request("/getBasicUserInfo", **params)

    def get_user_feed(self, **params):
        """Get user feed by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getUserFeed", **params)

    def get_user_feed_by_id(self, **params):
        """Get user feed by profile ID. See docs/endpoints.md for parameters."""
        return self.request("/getUserFeedByID", **params)

    def get_user_id(self, **params):
        """Get user ID by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getUserID", **params)

    def get_username_by_id(self, **params):
        """Get username by TikTok user ID. See docs/endpoints.md for parameters."""
        return self.request("/getUsernameByID", **params)

    def get_twitter_username(self, **params):
        """Get Twitter username by profile URL, nickname or TikTok user ID. See docs/endpoints.md for parameters."""
        return self.request("/getTwitterUsername", **params)

    def get_instagram_username(self, **params):
        """Get Instagram username by profile URL, nickname or TikTok user ID. See docs/endpoints.md for parameters."""
        return self.request("/getInstagramUsername", **params)

    def get_youtube_channel(self, **params):
        """Get YouTube channel info by profile URL, nickname or TikTok user ID. See docs/endpoints.md for parameters."""
        return self.request("/getYoutubeChannel", **params)

    def get_followers(self, **params):
        """Get user followers by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getFollowers", **params)

    def get_followers_by_id(self, **params):
        """Get user followers by profile ID. See docs/endpoints.md for parameters."""
        return self.request("/getFollowersByID", **params)

    def get_following(self, **params):
        """Get user following by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getFollowing", **params)

    def get_following_by_id(self, **params):
        """Get user following by profile ID. See docs/endpoints.md for parameters."""
        return self.request("/getFollowingByID", **params)

    def get_live_event_info_by_id(self, **params):
        """Get live event info by ID. See docs/endpoints.md for parameters."""
        return self.request("/getLiveEventInfoByID", **params)

    def get_hashtag_info(self, **params):
        """Get hashtag info by URL or tag name. See docs/endpoints.md for parameters."""
        return self.request("/getHashtagInfo", **params)

    def get_hashtag_feed(self, **params):
        """Get hashtag feed by URL or tag name. See docs/endpoints.md for parameters."""
        return self.request("/getHashtagFeed", **params)

    def get_hashtag_feed_by_id(self, **params):
        """Get hashtag feed by ID. See docs/endpoints.md for parameters."""
        return self.request("/getHashtagFeedByID", **params)

    def get_location_info_by_id(self, **params):
        """Get location info by ID. See docs/endpoints.md for parameters."""
        return self.request("/getLocationInfoByID", **params)

    def get_location_feed_by_id(self, **params):
        """Get videos by location ID. See docs/endpoints.md for parameters."""
        return self.request("/getLocationFeedByID", **params)

    def get_music_info(self, **params):
        """Get music info by URL or ID. See docs/endpoints.md for parameters."""
        return self.request("/getMusicInfo", **params)

    def get_music_feed(self, **params):
        """Get music feed by URL or ID. See docs/endpoints.md for parameters."""
        return self.request("/getMusicFeed", **params)

    def get_music_charts(self, **params):
        """Get music charts. See docs/endpoints.md for parameters."""
        return self.request("/getMusicCharts", **params)

    def get_trending_categories_list(self, **params):
        """Get trending categories list. See docs/endpoints.md for parameters."""
        return self.request("/getTrendingCategoriesList", **params)

    def get_trending_feed(self, **params):
        """Get trending feed. See docs/endpoints.md for parameters."""
        return self.request("/getTrendingFeed", **params)

    def get_stickers_by_id(self, **params):
        """Get effect information by IDs. See docs/endpoints.md for parameters."""
        return self.request("/getStickersByID", **params)

    def get_sticker_by_id(self, **params):
        """Get effect information by ID. See docs/endpoints.md for parameters."""
        return self.request("/getStickerByID", **params)

    def get_sticker_feed_by_id(self, **params):
        """Get videos by effect ID. See docs/endpoints.md for parameters."""
        return self.request("/getStickerFeedByID", **params)

    def get_user_stories(self, **params):
        """Get user stories. See docs/endpoints.md for parameters."""
        return self.request("/getUserStories", **params)

    def get_story_info_by_id(self, **params):
        """Get story info by ID. See docs/endpoints.md for parameters."""
        return self.request("/getStoryInfoByID", **params)

    def get_user_playlists(self, **params):
        """Get user playlists. See docs/endpoints.md for parameters."""
        return self.request("/getUserPlaylists", **params)

    def get_user_playlist_by_id(self, **params):
        """Get user playlist by ID. See docs/endpoints.md for parameters."""
        return self.request("/getUserPlaylistByID", **params)

    def get_video_by_playlist_id(self, **params):
        """Get video by playlist ID. See docs/endpoints.md for parameters."""
        return self.request("/getVideoByPlaylistID", **params)

    def get_available_ranking_list(self, **params):
        """Get available ranking list. See docs/endpoints.md for parameters."""
        return self.request("/getAvailableRankingList", **params)

    def get_ranking_info(self, **params):
        """Get ranking info. See docs/endpoints.md for parameters."""
        return self.request("/getRankingInfo", **params)

    def get_live_info(self, **params):
        """Get live info. See docs/endpoints.md for parameters."""
        return self.request("/getLiveInfo", **params)

    def get_live_feed(self, **params):
        """Get live feed. See docs/endpoints.md for parameters."""
        return self.request("/getLiveFeed", **params)

