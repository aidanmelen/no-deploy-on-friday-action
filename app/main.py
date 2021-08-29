"""The Main Github action workflow."""

# from zoneinfo import ZoneInfo

# import datetime
import holidays
import sys

import helpers
import inputs

WEEKDAYS = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}

NO_DEPLOYMENT_DAY_LIST = [day.strip().capitalize() for day in inputs.NO_DEPLOYMENT_DAYS.split(",")]
DEPLOYMENT_DAY_LIST = sorted(list(WEEKDAYS.difference(set(NO_DEPLOYMENT_DAY_LIST))))


def is_today_a_no_deployment_day(today, day_name):
    """Returns True if todau is a no deployment day."""

    is_today_a_no_deployment_day = day_name.lower() in inputs.NO_DEPLOYMENT_DAYS.lower()
    
    if is_today_a_no_deployment_day:
        reason = f"Do not deploy today ({day_name}). We do not deploy on {helpers.comma_separator(NO_DEPLOYMENT_DAY_LIST)}."

        print(f"::set-output name=reason::{reason}")
        print(f"::set-output name=deployment::false")
    else:
        reason = f"Deploying today ({day_name}). We deploy on {helpers.comma_separator(DEPLOYMENT_DAY_LIST)}."

        print(f"::set-output name=deployment::true")
        print(f"::set-output name=reason::{reason}")
    
    return is_today_a_no_deployment_day


def is_today_a_holiday(today, day_name):
    """Return True if today is a holiday."""

    is_today_a_holiday = inputs.HOLIDAYS.lower() == "true" and today in holidays.CountryHoliday(inputs.COUNTRY)
    
    if is_today_a_holiday:
        reason = f"Do not deploy today ({day_name}). We do not deploy on {inputs.COUNTRY} holidays."

        print(f"::set-output name=deployment::false")
        print(f"::set-output name=reason::{reason}")

    else:
        reason = f"Deploying today ({day_name}). We allow deployments on {inputs.COUNTRY} holidays."

        print(f"::set-output name=deployment::true")
        print(f"::set-output name=reason::{reason}")

    return is_today_a_holiday


def main():
    """The Main entrypoint."""

    today, day_name = helpers.get_today_and_day_name()

    if is_today_a_no_deployment_day(today, day_name):
        sys.exit(1)

    elif is_today_a_holiday(today, day_name):
        sys.exit(1)

    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
