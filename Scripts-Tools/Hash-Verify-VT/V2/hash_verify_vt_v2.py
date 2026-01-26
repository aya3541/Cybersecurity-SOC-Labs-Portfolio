#!/usr/bin/env python3

import requests
import sys
import time
import csv
import argparse

API_KEY = "YOUR_API_KEY_HERE"
VT_URL = "https://www.virustotal.com/api/v3/files/"
HEADERS = {"x-apikey": API_KEY}

# =========================
# FUNCTIONS
# =========================
def query_vt(file_hash):
    response = requests.get(VT_URL + file_hash, headers=HEADERS)

    if response.status_code == 404:
        return None

    if response.status_code != 200:
        print(f"API Error: {response.status_code}")
        time.sleep(20)
        return None

    stats = response.json()["data"]["attributes"]["last_analysis_stats"]
    return stats


def get_verdict(stats):
    if stats["malicious"] > 0:
        return "MALICIOUS"
    elif stats["suspicious"] > 0:
        return "SUSPICIOUS"
    else:
        return "CLEAN"


# =========================
# MAIN
# =========================
def main():
    parser = argparse.ArgumentParser(description="VirusTotal Hash Verification Tool v2.0")
    parser.add_argument("-f", "--file", help="File containing hashes")
    parser.add_argument("-o", "--output", default="vt_report.csv", help="Output CSV file")
    args = parser.parse_args()

    if not args.file:
        print("❌ Please provide a hash file using -f")
        sys.exit(1)

    with open(args.file, "r") as f:
        hashes = [line.strip() for line in f if line.strip()]

    with open(args.output, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Hash", "Malicious", "Suspicious", "Undetected", "Verdict"])

        for h in hashes:
            print(f"🔍 Scanning: {h}")
            stats = query_vt(h)

            if not stats:
                print("   Hash not found or API error")
                continue

            verdict = get_verdict(stats)

            writer.writerow([
                h,
                stats["malicious"],
                stats["suspicious"],
                stats["undetected"],
                verdict
            ])

            time.sleep(16)  # Rate limit safe

    print(f"\n✅ Scan completed. Report saved to {args.output}")


if __name__ == "__main__":
    main()
