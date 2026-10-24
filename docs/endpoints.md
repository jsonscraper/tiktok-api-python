# TikTok API endpoint reference

54 unique GET routes from the published Postman collection. Configure `license_key` on the client. Query parameters below use the same names as the API; check Postman for required/optional rules.

| SDK method | GET path | Query parameters | Purpose |
| --- | --- | --- | --- |
| `get_no_watermark_url` | `/getNoWatermarkUrl` | `video_url`, `region`, `cache_timeout` | Get non watermarked video url |
| `get_no_watermark_url_by_id` | `/getNoWatermarkUrlByID` | `video_id`, `region`, `cache_timeout` | Get non watermarked video url by video ID |
| `get_video_by_id` | `/getVideoByID` | `video_id`, `region`, `cache_timeout` | Get video info by ID |
| `get_video_by_url` | `/getVideoByUrl` | `video_url`, `region`, `cache_timeout` | Get video info by URL |
| `get_unshortened_url` | `/getUnshortenedUrl` | `video_url`, `cache_timeout` | Convert short TikTok video URL to full TikTok video URL |
| `get_comments_by_url` | `/getCommentsByUrl` | `video_url`, `region`, `cursor`, `count`, `cache_timeout` | Get comments list by video URL |
| `get_comments_by_id` | `/getCommentsByID` | `video_id`, `region`, `cursor`, `count`, `cache_timeout` | Get comments list by video ID |
| `get_comments_replies` | `/getCommentsReplies` | `video_id`, `comment_id`, `cursor`, `count`, `cache_timeout` | Get comments replies |
| `search_user` | `/searchUser` | `keyword`, `cursor`, `count`, `region`, `follower_count`, `profile_type`, `other_pref`, `cache_timeout` | Search for user by keyword |
| `search_video` | `/searchVideo` | `keyword`, `cursor`, `count`, `cache_timeout`, `date_posted`, `sort_by`, `region` | Search for video by keyword |
| `search_music` | `/searchMusic` | `keyword`, `cursor`, `count`, `cache_timeout`, `filter_by`, `sort_type`, `region` | Search for music by keyword |
| `search_live` | `/searchLive` | `keyword`, `offset`, `count`, `cache_timeout`, `region` | Search for live by keyword |
| `search_hashtag` | `/searchHashtag` | `keyword`, `cursor`, `count`, `region`, `cache_timeout` | Search for hashtag by keyword |
| `search_location` | `/searchLocation` | `keyword`, `cursor`, `count`, `region`, `cache_timeout` | Search for location by keyword |
| `search_top` | `/searchTop` | `keyword`, `cursor`, `count`, `region`, `sort_type`, `publish_time`, `cache_timeout` | Top search by text query |
| `search_insights` | `/searchInsights` | `keyword`, `cursor`, `count`, `region`, `cache_timeout` | Search insights by text query |
| `search_comment_suggested_users` | `/searchCommentSuggestedUsers` | `keyword`, `count`, `region`, `cache_timeout` | Search comment suggested users |
| `get_user_info` | `/getUserInfo` | `query`, `region`, `cache_timeout` | Get user info by profile URL or nickname |
| `get_user_info_by_id` | `/getUserInfoByID` | `user_id`, `region`, `cache_timeout` | Get user info by profile ID |
| `get_basic_user_info` | `/getBasicUserInfo` | `query`, `region`, `cache_timeout` | Get user info by username |
| `get_user_feed` | `/getUserFeed` | `query`, `max_cursor`, `count`, `region`, `with_pinned_posts`, `sort_type`, `cache_timeout` | Get user feed by profile URL or nickname |
| `get_user_feed_by_id` | `/getUserFeedByID` | `user_id`, `max_cursor`, `count`, `region`, `with_pinned_posts`, `sort_type`, `cache_timeout` | Get user feed by profile ID |
| `get_user_id` | `/getUserID` | `query`, `region`, `cache_timeout` | Get user ID by profile URL or nickname |
| `get_username_by_id` | `/getUsernameByID` | `user_id`, `region`, `cache_timeout` | Get username by TikTok user ID |
| `get_twitter_username` | `/getTwitterUsername` | `query`, `region`, `cache_timeout` | Get Twitter username by profile URL, nickname or TikTok user ID |
| `get_instagram_username` | `/getInstagramUsername` | `query`, `region`, `cache_timeout` | Get Instagram username by profile URL, nickname or TikTok user ID |
| `get_youtube_channel` | `/getYoutubeChannel` | `query`, `region`, `cache_timeout` | Get YouTube channel info by profile URL, nickname or TikTok user ID |
| `get_followers` | `/getFollowers` | `query`, `count`, `min_time`, `cache_timeout` | Get user followers by profile URL or nickname |
| `get_followers_by_id` | `/getFollowersByID` | `user_id`, `count`, `min_time`, `cache_timeout` | Get user followers by profile ID |
| `get_following` | `/getFollowing` | `query`, `count`, `min_time`, `cache_timeout` | Get user following by profile URL or nickname |
| `get_following_by_id` | `/getFollowingByID` | `user_id`, `count`, `min_time`, `cache_timeout` | Get user following by profile ID |
| `get_live_event_info_by_id` | `/getLiveEventInfoByID` | `event_id`, `cache_timeout` | Get live event info by ID |
| `get_hashtag_info` | `/getHashtagInfo` | `query`, `region`, `cache_timeout` | Get hashtag info by URL or tag name |
| `get_hashtag_feed` | `/getHashtagFeed` | `query`, `cursor`, `count`, `region`, `cache_timeout` | Get hashtag feed by URL or tag name |
| `get_hashtag_feed_by_id` | `/getHashtagFeedByID` | `id`, `cursor`, `count`, `region`, `cache_timeout` | Get hashtag feed by ID |
| `get_location_info_by_id` | `/getLocationInfoByID` | `location_id`, `cache_timeout` | Get location info by ID |
| `get_location_feed_by_id` | `/getLocationFeedByID` | `location_id`, `count`, `cursor`, `region`, `cache_timeout` | Get videos by location ID |
| `get_music_info` | `/getMusicInfo` | `query`, `region`, `cache_timeout` | Get music info by URL or ID |
| `get_music_feed` | `/getMusicFeed` | `query`, `cursor`, `count`, `cache_timeout`, `region` | Get music feed by URL or ID |
| `get_music_charts` | `/getMusicCharts` | `chart_type`, `cache_timeout`, `region` | Get music charts |
| `get_trending_categories_list` | `/getTrendingCategoriesList` | `region`, `offset`, `count`, `cache_timeout` | Get trending categories list |
| `get_trending_feed` | `/getTrendingFeed` | `region`, `pull_type`, `cache_timeout` | Get trending feed |
| `get_stickers_by_id` | `/getStickersByID` | `sticker_ids`, `cache_timeout` | Get effect information by IDs |
| `get_sticker_by_id` | `/getStickerByID` | `sticker_id`, `cache_timeout` | Get effect information by ID |
| `get_sticker_feed_by_id` | `/getStickerFeedByID` | `sticker_id`, `count`, `cursor`, `region`, `cache_timeout` | Get videos by effect ID |
| `get_user_stories` | `/getUserStories` | `user_id`, `count`, `min_cursor`, `region`, `cache_timeout` | Get user stories |
| `get_story_info_by_id` | `/getStoryInfoByID` | `story_id`, `region`, `cache_timeout` | Get story info by ID |
| `get_user_playlists` | `/getUserPlaylists` | `user_id`, `cursor`, `cache_timeout` | Get user playlists |
| `get_user_playlist_by_id` | `/getUserPlaylistByID` | `user_id`, `playlist_id`, `cache_timeout` | Get user playlist by ID |
| `get_video_by_playlist_id` | `/getVideoByPlaylistID` | `user_id`, `playlist_id`, `max_cursor`, `cache_timeout` | Get video by playlist ID |
| `get_available_ranking_list` | `/getAvailableRankingList` | `room_id`, `user_id`, `cache_timeout` | Get available ranking list |
| `get_ranking_info` | `/getRankingInfo` | `rank_type`, `room_id`, `user_id`, `cache_timeout` | Get ranking info |
| `get_live_info` | `/getLiveInfo` | `room_id`, `user_id`, `cache_timeout` | Get live info |
| `get_live_feed` | `/getLiveFeed` | `draw_room_id`, `max_time`, `region`, `cache_timeout` | Get live feed |
