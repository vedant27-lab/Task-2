# main.py
from timer_context import Timer
from log_record import LogRecord
import time


def process_logs():
    logs = [
        ("Failed to connect to server", "ERROR"),
        ("System initialized successfully", "INFO"),
        ("Retrying connection", "WARNING")
    ]

    for message, level in logs:
        log = LogRecord(
            time_stamp=time.time(),
            message=message,
            level=level,
            description="Generated during log processing"
        )

        print(log)


if __name__ == "__main__":
    with Timer("Processing logs", level="INFO"):
        process_logs()
