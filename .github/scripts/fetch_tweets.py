#!/usr/bin/env python3
"""
Refresh assets/data/tweets.json for the homepage's "X / Twitter timeline" card.

X removed every free way to read a *timeline* without login, but a single tweet's
live content is still fetchable for free via the syndication CDN. So this script
reads a hand-curated list of tweet URLs/IDs from .github/featured_tweets.txt and
fetches each tweet's current text, photo and like count. You only touch that list
(paste a URL when you post something worth featuring); the counts/photos stay live.

Design notes:
  * Standard library only — no `pip install` on the runner.
  * Defensive: a deleted/failed tweet is skipped; if nothing is fetched, the
    existing tweets.json is left untouched so the card never goes blank.

Run:  python .github/scripts/fetch_tweets.py [ids_file]
Env:  TWEETS_OUT=<path>  override output (used by tests)
"""

import os
import re
import sys
import json
import math
import html
import datetime
import urllib.request
import urllib.error

HERE = os.path.dirname(__file__)
IDS_PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "featured_tweets.txt")
OUT_PATH = os.environ.get("TWEETS_OUT", os.path.join(HERE, "..", "..", "assets", "data", "tweets.json"))

DISPLAY_NAME = "RebelsNLU@JAIST"
HANDLE = "rebelsnlu_jaist"
MAX_TWEETS = 4  # the card shows the newest 3; keep a small buffer
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def log(msg):
    print(f"[fetch_tweets] {msg}")


def read_ids(path):
    ids = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                m = re.search(r"status(?:es)?/(\d+)", line) or re.fullmatch(r"(\d+)", line)
                if m:
                    tid = m.group(1)
                    if tid not in ids:
                        ids.append(tid)
    except FileNotFoundError:
        log(f"no ids file at {path}")
    return ids


def syndication_token(tid):
    """Replicate the widget's token = ((id/1e15)*PI).toString(36) minus 0s and '.'"""
    n = (int(tid) / 1e15) * math.pi
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    intpart = int(n)
    frac = n - intpart
    out = ""
    if intpart == 0:
        out = "0"
    while intpart > 0:
        out = digits[intpart % 36] + out
        intpart //= 36
    res = out + "."
    for _ in range(24):
        frac *= 36
        d = int(frac)
        res += digits[d]
        frac -= d
    return re.sub(r"(0+|\.)", "", res)


def http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def parse_date(raw):
    if not raw:
        return None
    try:
        return datetime.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        pass
    for fmt in ("%a %b %d %H:%M:%S %z %Y", "%Y-%m-%dT%H:%M:%S.%f%z"):
        try:
            return datetime.datetime.strptime(raw, fmt)
        except ValueError:
            continue
    return None


def photo_of(d):
    for key in ("mediaDetails", "photos"):
        for m in d.get(key) or []:
            if isinstance(m, dict):
                u = m.get("media_url_https") or m.get("url")
                if u and m.get("type", "photo") == "photo":
                    return u
    return None


def fetch_tweet(tid):
    url = f"https://cdn.syndication.twimg.com/tweet-result?id={tid}&token={syndication_token(tid)}&lang=en"
    try:
        d = http_json(url)
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError, TimeoutError) as e:
        log(f"  id={tid} failed: {e}")
        return None
    text = html.unescape(d.get("text") or d.get("full_text") or "")
    text = re.sub(r"\s*https://t\.co/\w+\s*$", "", text).strip()
    if not text:
        return None
    user = d.get("user") or {}
    screen = user.get("screen_name") or HANDLE
    dt = parse_date(d.get("created_at"))
    return {
        "id": str(d.get("id_str") or tid),
        "url": f"https://x.com/{screen}/status/{d.get('id_str') or tid}",
        "date": dt.date().isoformat() if dt else "",
        "_sortkey": dt.timestamp() if dt else 0,
        "text": text,
        "photo": photo_of(d),
        "likes": int(d.get("favorite_count") or 0),
        "retweets": int(d.get("retweet_count") or 0),
        "replies": int(d.get("conversation_count") or 0),
    }


def main():
    ids = read_ids(IDS_PATH)
    if not ids:
        log("featured_tweets.txt is empty — leaving tweets.json untouched. "
            "Add tweet URLs to activate live updates.")
        return 0

    log(f"fetching {len(ids)} tweet(s)")
    tweets = [t for t in (fetch_tweet(i) for i in ids) if t]
    if not tweets:
        log("no tweets fetched — leaving existing tweets.json untouched.")
        return 0

    tweets.sort(key=lambda x: x["_sortkey"], reverse=True)
    tweets = tweets[:MAX_TWEETS]
    for t in tweets:
        t.pop("_sortkey", None)

    payload = {
        "handle": HANDLE,
        "name": DISPLAY_NAME,
        "updated": datetime.datetime.now(datetime.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "source": "syndication-tweet",
        "tweets": tweets,
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    log(f"wrote {len(tweets)} tweet(s) to {os.path.normpath(OUT_PATH)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # never fail the workflow on a scraping hiccup
        log(f"unexpected error: {e}")
        sys.exit(0)
