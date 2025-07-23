# test_timer.py
# Execution program for test_log_record.py
from timer_context import Timer
import time


def test_timer_execution_time():
    with Timer("Testing", level="DEBUG") as t:
        time.sleep(0.1)
    assert 0.09 < t.duration < 0.2
