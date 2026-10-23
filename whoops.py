import psutil
import time
import os
from datetime import datetime

def format_bytes(bytes_value):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_value < 1024:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024
    return f"{bytes_value:.2f} PB"

def main():
    previous = psutil.net_io_counters()
    try:
        while True:
            time.sleep(1)
            current = psutil.net_io_counters()
            upload_speed = current.bytes_sent - previous.bytes_sent
            download_speed = current.bytes_recv - previous.bytes_recv
            previous = current
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 45)
            print("     PYTHON NETWORK USAGE MONITOR")
            print("=" * 45)
            print("Time:", datetime.now().strftime("%H:%M:%S"))
            print("\nUPLOAD")
            print("  Speed:", format_bytes(upload_speed), "/s")
            print("  Total:", format_bytes(current.bytes_sent))
            print("\nDOWNLOAD")
            print("  Speed:", format_bytes(download_speed), "/s")
            print("  Total:", format_bytes(current.bytes_recv))
            print("\nNETWORK INTERFACES")
            for name, stats in psutil.net_if_stats().items():
                print(f"  {name}: {'UP' if stats.isup else 'DOWN'}")
            print("\nPress Ctrl+C to stop.")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        final = psutil.net_io_counters()
        print("Total uploaded:", format_bytes(final.bytes_sent))
        print("Total downloaded:", format_bytes(final.bytes_recv))

if __name__ == "__main__":
    main()
