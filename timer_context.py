# timer_context.py
import time
from log_record import LogRecord


class Timer:
    def __init__(self, message: str = "Execution completed", level: str = "INFO"):
        self.message = message
        self.level = level
        self.start_time = 0.0

    # Assign start time
    def __enter__(self):
        self.start_time = time.time()
        return self

    # Ending duration time
    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        self.duration = end_time - self.start_time

        log = LogRecord(
            time_stamp=end_time,
            message=self.message,
            level=self.level,
            description=f"Time taken: {self.duration:.4f} seconds"
        )

        print(log)
