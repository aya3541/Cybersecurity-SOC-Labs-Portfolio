import re
import datetime
from collections import Counter

# Log-Intel-Analyzer.py
# Purpose: Professional SOC utility to analyze web server access logs.

def analyze_logs(file_path, threshold=50):
    """
    Analyze web server logs to extract IP addresses, 
    count frequency, and highlight potential threats.
    """

    # Professional Regex for valid IPv4 addresses (0–255)
    ip_pattern = (
        r'\b('
        r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.'
        r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.'
        r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.'
        r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
        r')\b'
    )

    try:
        with open(file_path, 'r') as file:
            log_content = file.read()

        # Extract and Clean IPs
        found_ips = re.findall(ip_pattern, log_content)
        found_ips = [ip[0] for ip in found_ips] 

        # Count frequency
        ip_counts = Counter(found_ips)
        
        # Get Current Timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("=" * 50)
        print(f"  SOC LOG ANALYSIS REPORT")
        print(f"Generated on: {current_time}")
        print("=" * 50)
        print(f"Total Requests Analyzed : {len(found_ips)}")
        print(f"Unique IPs Detected     : {len(ip_counts)}")
        print(f"Alert Threshold         : {threshold}+ requests")
        print("-" * 50)

        print(" High-Frequency IPs (Potentially Suspicious):")

        suspicious_found = False
        # Sorting by most common for better visibility
        for ip, count in ip_counts.most_common():
            if count >= threshold:
                print(f"IP: {ip:<15} | Requests: {count}")
                suspicious_found = True

        if not suspicious_found:
            print(" No IP addresses exceeded the defined threshold.")

        print("=" * 50)

    except FileNotFoundError:
        print(f"[ERROR] Log file '{file_path}' not found.")
    except Exception as e:
        print(f"[ERROR] Unexpected issue occurred: {e}")

if __name__ == "__main__":
    # Ensure 'access.log' exists in the same folder
    analyze_logs("access.log")
