"""The helpers fucntions for the Github action workflow."""

from zoneinfo import ZoneInfo

import datetime

import inputs


def comma_separator(seq):
    """Return a comma delimited string given a list of strings.

    Args:
        seq: A list of strings.

    Returns:
        Comma delimited string.
    """
    return ", and ".join([", ".join(seq[:-1]), seq[-1]] if len(seq) > 2 else seq)


def get_today_and_day_name():
    """Get today's date information.

    Returns:
        Return a tuple containing a timezone aware datetime for today and the day name for today.
    """
    today = datetime.datetime.now(ZoneInfo(inputs.TZ.upper()))
    day_name = today.strftime("%A")
    return today, day_name
