import requests
import sys
from datetime import datetime

API_URL = "http://ip-api.com/json/{}"

def enrich_ip(ip_address):
    try:
        response = requests.get(API_URL.format(ip_address), timeout=5)
        data = response.json()

        if data.get("status") != "success":
            print("Failed to retrieve data for the provided IP address.")
            return

        print("=" * 60)
        print("IP THREAT INTELLIGENCE REPORT")
        print(f"Report Generated: {datetime.now()}")
        print("=" * 60)

        print(f"IP Address   : {data.get('query')}")
        print(f"Country      : {data.get('country')}")
        print(f"City         : {data.get('city')}")
        print(f"ISP          : {data.get('isp')}")
        print(f"Organization : {data.get('org')}")
        print(f"ASN          : {data.get('as')}")
        print(f"Timezone     : {data.get('timezone')}")
        print("-" * 60)

        if data.get("hosting") or data.get("proxy"):
            print("Risk Assessment: POTENTIALLY SUSPICIOUS IP")
        else:
            print("Risk Assessment: No obvious threat indicators detected")

        print("=" * 60)

    except requests.exceptions.RequestException:
        print("Network error occurred while contacting the API.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 Suspicious_IP_Enricher.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    enrich_ip(ip_address)

if __name__ == "__main__":
    main()
