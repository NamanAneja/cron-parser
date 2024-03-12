# cron-parser

This Python program is a simple cron expression parser that converts a cron expression into a human-readable table format. It takes a standard cron string with five time fields (minute, hour, day of month, month, and day of week) and a command, and it formats the cron expression as a table with field names in the first 14 columns and the corresponding times as space-separated lists.

Requirements:
1. Given a cli command having cron expression, return a view of the times at which it will run.


How to Run:
1. pip install .
2. python main.py "*/15 0 1,15 * 1-5 /usr/bin/find"

Features:
1. Handles step values, range of values, any value (*), and lists of values for each cron field.
2. Provides clear and human-readable output with field names and corresponding time values.