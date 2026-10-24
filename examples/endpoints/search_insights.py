#!/usr/bin/env python3
"""Search insights by text query.

Run: python examples/endpoints/search_insights.py --help
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
    parser = argparse.ArgumentParser(description='Search insights by text query\nGET /searchInsights\n\nEnvironment: JSONSCRAPER_TIKTOK_LICENSE_KEY\nCommon options: --timeout=30, --help\nQuery options:\n  --keyword=VALUE  Any text or keyword\n  --cursor=VALUE  Used for scrolling (pagination) in video items, you can get cursor value from the previous response.\n  --count=VALUE  Number of results you want to get. For example: 25.\n  --region=VALUE  Region (country) code. Default: US\n  --cache_timeout=VALUE  Cache timeout in seconds. By default we use caching system with 3600 seconds window to speed up next requests to API. If you want to disable caching, you can set 0 here.\n\nValues omitted from the command use the public Postman sample defaults. Replace IDs/URLs with your own inputs. Each run makes one request; live requests may consume quota.', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--timeout", type=float, default=30, help="Request timeout in seconds")
    parser.add_argument("--retries", type=int, default=0, help="Optional retries, 0 to 5; may consume quota")
    parser.add_argument("--output", help="Save binary/JSON response to this file instead of standard output")
    parser.add_argument("--keyword", default='appletv', help='Any text or keyword')
    parser.add_argument("--cursor", default=None, help='Used for scrolling (pagination) in video items, you can get cursor value from the previous response.')
    parser.add_argument("--count", default=None, help='Number of results you want to get. For example: 25.')
    parser.add_argument("--region", default=None, help='Region (country) code. Default: US')
    parser.add_argument("--cache_timeout", default='60', help='Cache timeout in seconds. By default we use caching system with 3600 seconds window to speed up next requests to API. If you want to disable caching, you can set 0 here.')
    args = parser.parse_args()
    key = os.environ.get("JSONSCRAPER_TIKTOK_LICENSE_KEY", "").strip()
    if not key:
        parser.error("Set JSONSCRAPER_TIKTOK_LICENSE_KEY before making a licensed request")
    if args.timeout <= 0 or not 0 <= args.retries <= 5:
        parser.error("Use a positive timeout and 0 to 5 retries")
    try:
        client = TikTok(key, timeout=args.timeout, retries=args.retries)
        response = client.search_insights(keyword=args.keyword, cursor=args.cursor, count=args.count, region=args.region, cache_timeout=args.cache_timeout)
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
