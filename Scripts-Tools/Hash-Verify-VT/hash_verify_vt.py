#!/usr/bin/env python3

import requests
import sys
import json

# =========================
# CONFIGURATION
# =========================
API_KEY = "YOUR_API_KEY_HERE"
VT_URL = "https://www.virustotal.com/api/v3/files/"

HEADERS = {
    "x-apikey": API_KEY
}

# =========================
# FUNCTIONS
# =========================
def analyze_hash(file_hash):
    """
    Query VirusTotal API with a file hash and return analysis results
    """
    response = requests.get(VT_URL + file_hash, headers=HEADERS)

    if response.status_code == 404:
        print("❌ Hash not found on VirusTotal.")
        sys.exit(1)

    if response.status_code != 200:
        print(f"❌ API Error: {response.status_code}")
        sys.exit(1)

    data = response.json()
    stats = data["data"]["attributes"]["last_analysis_stats"]

    return stats


def verdict(stats):
    """
    Decide verdict based on VirusTotal detections
    """
    if stats["malicious"] > 0:
        return "🚨 MALICIOUS"
    elif stats["suspicious"] > 0:
        return "⚠️ SUSPICIOUS"
    else:
        return "✅ CLEAN"


# =========================
# MAIN
# =========================
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 hash_verify_vt.py <file_hash>")
        sys.exit(1)

    file_hash = sys.argv[1]

    print("=" * 40)
    print("🔍 VirusTotal Hash Analysis")
    print("=" * 40)

    stats = analyze_hash(file_hash)
    result = verdict(stats)

    print(f"Malicious     : {stats['malicious']}")
    print(f"Suspicious    : {stats['suspicious']}")
    print(f"Undetected    : {stats['undetected']}")
    print(f"Harmless      : {stats['harmless']}")
    print(f"Total Engines : {sum(stats.values())}")
    print("-" * 40)
    print(f"Verdict       : {result}")
    print("=" * 40)


if __name__ == "__main__":
    main()
