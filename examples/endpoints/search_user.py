#!/usr/bin/env python3
"""Search for user by keyword.

Run: python examples/endpoints/search_user.py --help
Requires an installed jsonscraper-tiktok package and JSONSCRAPER_TIKTOK_LICENSE_KEY.
The example makes one request and prints the full API envelope.
"""
import argparse
import json
import os
import sys
from pathlib import Path
from jsonscraper_tiktok import TikTok, APIError, TransportError


def main():
    parser = argparse.ArgumentParser(description='Search for user by keyword\nGET /searchUser\n\nEnvironment: JSONSCRAPER_TIKTOK_LICENSE_KEY\nCommon options: --timeout=30, --help\nQuery options:\n  --keyword=VALUE  Any text or keyword\n  --cursor=VALUE  Used for scrolling (pagination) in user items, you can get cursor value from the previous response.\n  --count=VALUE  Number of results you want to get. For example: 10.\n  --region=VALUE  Region (country) code. Default: US\n  --follower_count=VALUE  Filter by followers count, can be empty or one of: ZERO_TO_ONE_K (0 to 1k), ONE_K_TO_TEN_K (1k to 10k), TEN_K_TO_ONE_H_K(10k to 100k), ONE_H_K_PLUS(100k+)\n  --profile_type=VALUE  Filter by user profile type, can be empty or one of: VERIFIED\n  --other_pref=VALUE  Filter by other preference, can be empty or one of: USERNAME (keyword usage in username).\n  --cache_timeout=VALUE  Cache timeout in seconds. By default we use caching system with 3600 seconds window to speed up next requests to API. If you want to disable caching, you can set 0 here. \n\nValues omitted from the command use the public Postman sample defaults. Replace IDs/URLs with your own inputs. Each run makes one request; live requests may consume quota.', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--timeout", type=float, default=30, help="Request timeout in seconds")
    parser.add_argument("--retries", type=int, default=0, help="Optional retries, 0 to 5; may consume quota")
    parser.add_argument("--output", help="Save binary/JSON response to this file instead of standard output")
    parser.add_argument("--keyword", default='apple', help='Any text or keyword')
    parser.add_argument("--cursor", default=None, help='Used for scrolling (pagination) in user items, you can get cursor value from the previous response.')
    parser.add_argument("--count", default=None, help='Number of results you want to get. For example: 10.')
    parser.add_argument("--region", default=None, help='Region (country) code. Default: US')
    parser.add_argument("--follower_count", default=None, help='Filter by followers count, can be empty or one of: ZERO_TO_ONE_K (0 to 1k), ONE_K_TO_TEN_K (1k to 10k), TEN_K_TO_ONE_H_K(10k to 100k), ONE_H_K_PLUS(100k+)')
    parser.add_argument("--profile_type", default=None, help='Filter by user profile type, can be empty or one of: VERIFIED')
    parser.add_argument("--other_pref", default=None, help='Filter by other preference, can be empty or one of: USERNAME (keyword usage in username).')
    parser.add_argument("--cache_timeout", default='60', help='Cache timeout in seconds. By default we use caching system with 3600 seconds window to speed up next requests to API. If you want to disable caching, you can set 0 here.\n')
    args = parser.parse_args()
    key = os.environ.get("JSONSCRAPER_TIKTOK_LICENSE_KEY", "").strip()
    if not key:
        parser.error("Set JSONSCRAPER_TIKTOK_LICENSE_KEY before making a licensed request")
    if args.timeout <= 0 or not 0 <= args.retries <= 5:
        parser.error("Use a positive timeout and 0 to 5 retries")
    try:
        client = TikTok(key, timeout=args.timeout, retries=args.retries)
        response = client.search_user(keyword=args.keyword, cursor=args.cursor, count=args.count, region=args.region, follower_count=args.follower_count, profile_type=args.profile_type, other_pref=args.other_pref, cache_timeout=args.cache_timeout)
        if isinstance(response, bytes):
            if not args.output:
                parser.error("Binary response: provide --output=filename")
            Path(args.output).write_bytes(response)
            return 0
        if not isinstance(response, dict) or response.get("status") != "ok":
            print("The API returned an application error. Inspect the envelope below.", file=sys.stderr)
            print(json.dumps(response, ensure_ascii=False, indent=2))
            return 1
        if response.get("rate_limit_reached"):
            print("The API reports that the license rate limit was reached.", file=sys.stderr)
            return 1
        rendered = json.dumps(response, ensure_ascii=False, indent=2)
        if args.output:
            Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        else:
            print(rendered)
        return 0
    except APIError as error:
        print(f"HTTP {error.status}. Check parameters, access and quota. Retry-After: {error.retry_after or 'not provided'}", file=sys.stderr)
        return 1
    except (TransportError, ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
