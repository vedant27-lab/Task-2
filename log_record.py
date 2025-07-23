# log_record.py
from dataclasses import dataclass
from typing import Literal


@dataclass
class LogRecord:
    time_stamp: float
    message: str
    level: Literal["INFO", "WARNING", "ERROR", "DEBUG"]
    description: str

    # The Following method put log records in dictonary form.
    def to_dict(self) -> dict:
        return {
            "time_stamp": self.time_stamp,
            "message": self.message,
            "level": self.level,
            "description": self.description
        }
