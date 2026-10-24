#!/usr/bin/env python3
"""Get live info.

Run: python examples/endpoints/get_live_info.py --help
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
    parser = argparse.ArgumentParser(description='Get live info\nGET /getLiveInfo\n\nEnvironment: JSONSCRAPER_TIKTOK_LICENSE_KEY\nCommon options: --timeout=30, --help\nQuery options:\n  --room_id=VALUE  TikTok Live Room ID.\n  --user_id=VALUE  TikTok User ID.\n  --cache_timeout=VALUE  Cache timeout in seconds. By default we use caching system with 3600 seconds window to speed up next requests to API. If you want to disable caching, you can set 0 here.\n\nValues omitted from the command use the public Postman sample defaults. Replace IDs/URLs with your own inputs. Each run makes one request; live requests may consume quota.', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--timeout", type=float, default=30, help="Request timeout in seconds")
    parser.add_argument("--retries", type=int, default=0, help="Optional retries, 0 to 5; may consume quota")
    parser.add_argument("--output", help="Save binary/JSON response to this file instead of standard output")
    parser.add_argument("--room_id", default='7620881460702087949', help='TikTok Live Room ID.')
    parser.add_argument("--user_id", default='7427227547880047662', help='TikTok User ID.')
    parser.add_argument("--cache_timeout", default='60', help='Cache timeout in seconds. By default we use caching system with 3600 seconds window to speed up next requests to API. If you want to disable caching, you can set 0 here.')
    args = parser.parse_args()
    key = os.environ.get("JSONSCRAPER_TIKTOK_LICENSE_KEY", "").strip()
    if not key:
        parser.error("Set JSONSCRAPER_TIKTOK_LICENSE_KEY before making a licensed request")
    if args.timeout <= 0 or not 0 <= args.retries <= 5:
        parser.error("Use a positive timeout and 0 to 5 retries")
    try:
        client = TikTok(key, timeout=args.timeout, retries=args.retries)
        response = client.get_live_info(room_id=args.room_id, user_id=args.user_id, cache_timeout=args.cache_timeout)
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
