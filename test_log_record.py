# test_log_record.py
from log_record import LogRecord
import time


# Function to test ther log records and perform unit testing.
def test_log_record_creation():
    now = time.time()
    log = LogRecord(
        time_stamp=now,
        message="Sample log",
        level="INFO",
        description="Testing the main file."
    )

    assert log.time_stamp == now
    assert log.message == "Sample log"
    assert log.level == "INFO"
    assert log.description == "Testing the main file."
