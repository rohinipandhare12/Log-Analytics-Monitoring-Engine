
import re 

from datetime import datetime

def parse_log_line(line):
    try:
        parts = line.strip().split()

        if len(parts) < 3:
            return None

        timestamp_str = parts[0] + " " + parts[1]

        level = parts[2]

        message = " ".join(parts[3:])

        timestamp = datetime.strptime(
            timestamp_str,
            "%Y-%m-%d %H:%M:%S"
        )

        return {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }

    except Exception as e:
        print("Parse error:", line)
        return None
