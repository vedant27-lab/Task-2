# Task 2 – Refactoring Python Script and Unit Testing

This is my submission for Day 2 of the internship at CyArt. The task was to refactor a basic script and improve its structure using Python's advanced concepts. I also added unit tests using `pytest` to make the solution testable and reliable.

---

## 📌 Task Objective

The original script was a simple, unstructured function that printed logs and execution time. The goal was to improve it using:

- `@dataclass` for structured log data
- Context managers using `__enter__` and `__exit__`
- SOLID principles for better code structure
- Unit testing with `pytest`

---

## 📂 Files and Their Purpose

- `log_record.py` – Defines a `LogRecord` class using `@dataclass` for storing log data.
- `timer_context.py` – A custom context manager called `Timer` that measures and logs execution time.
- `main.py` – Uses both modules to simulate a small logging process.
- `test_timer.py` – Contains a unit test to check if the timer logs time correctly.

---

## 🔧 How to Run the Code

### Run the main program:
```bash
python main.py
