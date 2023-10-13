"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

s = "12:01:00PM"

Return '12:01:00'.

s = "12:01:00AM"

Return '00:01:00'.
"""


# O(n) time | O(n) space
def timeConversion(s):
    hours, minutes, seconds = s.split(":")
    seconds, am_or_pm = seconds[:2], seconds[2:]
    if am_or_pm == "AM" and int(hours) == 12:
        hours = "00"
    elif am_or_pm == "PM" and int(hours) != 12:
        hours = str(int(hours) + 12)

    return hours+":"+minutes+":"+seconds
