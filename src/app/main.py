"""The Main Github action workflow."""

import holidays
import sys

import helpers
import inputs

WEEKDAYS = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}

NO_DEPLOYMENT_DAY_LIST = [day.strip().capitalize() for day in inputs.NO_DEPLOYMENT_DAYS.split(",")]
DEPLOYMENT_DAY_LIST = sorted(list(WEEKDAYS.difference(set(NO_DEPLOYMENT_DAY_LIST))))


def main():
    """The Main entrypoint."""

    today, day_name = helpers.get_today_and_day_name()

    is_today_a_no_deployment_day = day_name.lower() in inputs.NO_DEPLOYMENT_DAYS.lower()
    is_today_a_holiday = inputs.HOLIDAYS.lower() == "true" and today in holidays.CountryHoliday(
        inputs.COUNTRY
    )

    if is_today_a_no_deployment_day:

        print(
            f"Do not deploy today ({day_name}). We do not deploy on {helpers.comma_separator(NO_DEPLOYMENT_DAY_LIST)}."
        )
        sys.exit(1)

    elif is_today_a_holiday:

        print(f"Do not deploy today ({day_name}). We do not deploy on {inputs.COUNTRY} holidays.")
        sys.exit(1)

    else:

        additional_reason = (
            " and on {inputs.COUNTRY} holidays." if inputs.HOLIDAYS.lower() == "true" else ""
        )
        print(
            f"Deploying today ({day_name}). We deploy on {helpers.comma_separator(DEPLOYMENT_DAY_LIST)}{additional_reason}"
        )
        sys.exit(0)


if __name__ == "__main__":
    main()
