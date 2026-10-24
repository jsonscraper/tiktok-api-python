# TikTok python request examples

Every file below is a complete single-request CLI program with environment-based authentication, all documented query options, timeout configuration, error handling and full response output. Sample defaults come from Postman; replace account names, IDs and URLs for your use case. `--help` requires no API key and makes no network request.

Set `JSONSCRAPER_TIKTOK_LICENSE_KEY` and install the SDK as described in the main README. Each execution makes one live request and may consume quota. None of these programs loops through a feed automatically.

## Get non watermarked video url

[Open the complete example](endpoints/get_no_watermark_url.py) · `GET /getNoWatermarkUrl`

```sh
python examples/endpoints/get_no_watermark_url.py --help
```

## Get non watermarked video url by video ID

[Open the complete example](endpoints/get_no_watermark_url_by_id.py) · `GET /getNoWatermarkUrlByID`

```sh
python examples/endpoints/get_no_watermark_url_by_id.py --help
```

## Get video info by ID

[Open the complete example](endpoints/get_video_by_id.py) · `GET /getVideoByID`

```sh
python examples/endpoints/get_video_by_id.py --help
```

## Get video info by URL

[Open the complete example](endpoints/get_video_by_url.py) · `GET /getVideoByUrl`

```sh
python examples/endpoints/get_video_by_url.py --help
```

## Convert short TikTok video URL to full TikTok video URL

[Open the complete example](endpoints/get_unshortened_url.py) · `GET /getUnshortenedUrl`

```sh
python examples/endpoints/get_unshortened_url.py --help
```

## Get comments list by video URL

[Open the complete example](endpoints/get_comments_by_url.py) · `GET /getCommentsByUrl`

```sh
python examples/endpoints/get_comments_by_url.py --help
```

## Get comments list by video ID

[Open the complete example](endpoints/get_comments_by_id.py) · `GET /getCommentsByID`

```sh
python examples/endpoints/get_comments_by_id.py --help
```

## Get comments replies

[Open the complete example](endpoints/get_comments_replies.py) · `GET /getCommentsReplies`

```sh
python examples/endpoints/get_comments_replies.py --help
```

## Search for user by keyword

[Open the complete example](endpoints/search_user.py) · `GET /searchUser`

```sh
python examples/endpoints/search_user.py --help
```

## Search for video by keyword

[Open the complete example](endpoints/search_video.py) · `GET /searchVideo`

```sh
python examples/endpoints/search_video.py --help
```

## Search for music by keyword

[Open the complete example](endpoints/search_music.py) · `GET /searchMusic`

```sh
python examples/endpoints/search_music.py --help
```

## Search for live by keyword

[Open the complete example](endpoints/search_live.py) · `GET /searchLive`

```sh
python examples/endpoints/search_live.py --help
```

## Search for hashtag by keyword

[Open the complete example](endpoints/search_hashtag.py) · `GET /searchHashtag`

```sh
python examples/endpoints/search_hashtag.py --help
```

## Search for location by keyword

[Open the complete example](endpoints/search_location.py) · `GET /searchLocation`

```sh
python examples/endpoints/search_location.py --help
```

## Top search by text query

[Open the complete example](endpoints/search_top.py) · `GET /searchTop`

```sh
python examples/endpoints/search_top.py --help
```

## Search insights by text query

[Open the complete example](endpoints/search_insights.py) · `GET /searchInsights`

```sh
python examples/endpoints/search_insights.py --help
```

## Search comment suggested users

[Open the complete example](endpoints/search_comment_suggested_users.py) · `GET /searchCommentSuggestedUsers`

```sh
python examples/endpoints/search_comment_suggested_users.py --help
```

## Get user info by profile URL or nickname

[Open the complete example](endpoints/get_user_info.py) · `GET /getUserInfo`

```sh
python examples/endpoints/get_user_info.py --help
```

## Get user info by profile ID

[Open the complete example](endpoints/get_user_info_by_id.py) · `GET /getUserInfoByID`

```sh
python examples/endpoints/get_user_info_by_id.py --help
```

## Get user info by username

[Open the complete example](endpoints/get_basic_user_info.py) · `GET /getBasicUserInfo`

```sh
python examples/endpoints/get_basic_user_info.py --help
```

## Get user feed by profile URL or nickname

[Open the complete example](endpoints/get_user_feed.py) · `GET /getUserFeed`

```sh
python examples/endpoints/get_user_feed.py --help
```

## Get user feed by profile ID

[Open the complete example](endpoints/get_user_feed_by_id.py) · `GET /getUserFeedByID`

```sh
python examples/endpoints/get_user_feed_by_id.py --help
```

## Get user ID by profile URL or nickname

[Open the complete example](endpoints/get_user_id.py) · `GET /getUserID`

```sh
python examples/endpoints/get_user_id.py --help
```

## Get username by TikTok user ID

[Open the complete example](endpoints/get_username_by_id.py) · `GET /getUsernameByID`

```sh
python examples/endpoints/get_username_by_id.py --help
```

## Get Twitter username by profile URL, nickname or TikTok user ID

[Open the complete example](endpoints/get_twitter_username.py) · `GET /getTwitterUsername`

```sh
python examples/endpoints/get_twitter_username.py --help
```

## Get Instagram username by profile URL, nickname or TikTok user ID

[Open the complete example](endpoints/get_instagram_username.py) · `GET /getInstagramUsername`

```sh
python examples/endpoints/get_instagram_username.py --help
```

## Get YouTube channel info by profile URL, nickname or TikTok user ID

[Open the complete example](endpoints/get_youtube_channel.py) · `GET /getYoutubeChannel`

```sh
python examples/endpoints/get_youtube_channel.py --help
```

## Get user followers by profile URL or nickname

[Open the complete example](endpoints/get_followers.py) · `GET /getFollowers`

```sh
python examples/endpoints/get_followers.py --help
```

## Get user followers by profile ID

[Open the complete example](endpoints/get_followers_by_id.py) · `GET /getFollowersByID`

```sh
python examples/endpoints/get_followers_by_id.py --help
```

## Get user following by profile URL or nickname

[Open the complete example](endpoints/get_following.py) · `GET /getFollowing`

```sh
python examples/endpoints/get_following.py --help
```

## Get user following by profile ID

[Open the complete example](endpoints/get_following_by_id.py) · `GET /getFollowingByID`

```sh
python examples/endpoints/get_following_by_id.py --help
```

## Get live event info by ID

[Open the complete example](endpoints/get_live_event_info_by_id.py) · `GET /getLiveEventInfoByID`

```sh
python examples/endpoints/get_live_event_info_by_id.py --help
```

## Get hashtag info by URL or tag name

[Open the complete example](endpoints/get_hashtag_info.py) · `GET /getHashtagInfo`

```sh
python examples/endpoints/get_hashtag_info.py --help
```

## Get hashtag feed by URL or tag name

[Open the complete example](endpoints/get_hashtag_feed.py) · `GET /getHashtagFeed`

```sh
python examples/endpoints/get_hashtag_feed.py --help
```

## Get hashtag feed by ID

[Open the complete example](endpoints/get_hashtag_feed_by_id.py) · `GET /getHashtagFeedByID`

```sh
python examples/endpoints/get_hashtag_feed_by_id.py --help
```

## Get location info by ID

[Open the complete example](endpoints/get_location_info_by_id.py) · `GET /getLocationInfoByID`

```sh
python examples/endpoints/get_location_info_by_id.py --help
```

## Get videos by location ID

[Open the complete example](endpoints/get_location_feed_by_id.py) · `GET /getLocationFeedByID`

```sh
python examples/endpoints/get_location_feed_by_id.py --help
```

## Get music info by URL or ID

[Open the complete example](endpoints/get_music_info.py) · `GET /getMusicInfo`

```sh
python examples/endpoints/get_music_info.py --help
```

## Get music feed by URL or ID

[Open the complete example](endpoints/get_music_feed.py) · `GET /getMusicFeed`

```sh
python examples/endpoints/get_music_feed.py --help
```

## Get music charts

[Open the complete example](endpoints/get_music_charts.py) · `GET /getMusicCharts`

```sh
python examples/endpoints/get_music_charts.py --help
```

## Get trending categories list

[Open the complete example](endpoints/get_trending_categories_list.py) · `GET /getTrendingCategoriesList`

```sh
python examples/endpoints/get_trending_categories_list.py --help
```

## Get trending feed

[Open the complete example](endpoints/get_trending_feed.py) · `GET /getTrendingFeed`

```sh
python examples/endpoints/get_trending_feed.py --help
```

## Get effect information by IDs

[Open the complete example](endpoints/get_stickers_by_id.py) · `GET /getStickersByID`

```sh
python examples/endpoints/get_stickers_by_id.py --help
```

## Get effect information by ID

[Open the complete example](endpoints/get_sticker_by_id.py) · `GET /getStickerByID`

```sh
python examples/endpoints/get_sticker_by_id.py --help
```

## Get videos by effect ID

[Open the complete example](endpoints/get_sticker_feed_by_id.py) · `GET /getStickerFeedByID`

```sh
python examples/endpoints/get_sticker_feed_by_id.py --help
```

## Get user stories

[Open the complete example](endpoints/get_user_stories.py) · `GET /getUserStories`

```sh
python examples/endpoints/get_user_stories.py --help
```

## Get story info by ID

[Open the complete example](endpoints/get_story_info_by_id.py) · `GET /getStoryInfoByID`

```sh
python examples/endpoints/get_story_info_by_id.py --help
```

## Get user playlists

[Open the complete example](endpoints/get_user_playlists.py) · `GET /getUserPlaylists`

```sh
python examples/endpoints/get_user_playlists.py --help
```

## Get user playlist by ID

[Open the complete example](endpoints/get_user_playlist_by_id.py) · `GET /getUserPlaylistByID`

```sh
python examples/endpoints/get_user_playlist_by_id.py --help
```

## Get video by playlist ID

[Open the complete example](endpoints/get_video_by_playlist_id.py) · `GET /getVideoByPlaylistID`

```sh
python examples/endpoints/get_video_by_playlist_id.py --help
```

## Get available ranking list

[Open the complete example](endpoints/get_available_ranking_list.py) · `GET /getAvailableRankingList`

```sh
python examples/endpoints/get_available_ranking_list.py --help
```

## Get ranking info

[Open the complete example](endpoints/get_ranking_info.py) · `GET /getRankingInfo`

```sh
python examples/endpoints/get_ranking_info.py --help
```

## Get live info

[Open the complete example](endpoints/get_live_info.py) · `GET /getLiveInfo`

```sh
python examples/endpoints/get_live_info.py --help
```

## Get live feed

[Open the complete example](endpoints/get_live_feed.py) · `GET /getLiveFeed`

```sh
python examples/endpoints/get_live_feed.py --help
```

