"""Inputs from the Github Action workflow."""

import os

NO_DEPLOYMENT_DAYS = str(os.getenv("NO_DEPLOYMENT_DAYS", "Friday, Saturday, Sunday"))
TZ = str(os.getenv("TZ", "UTC"))
COUNTRY = str(os.getenv("COUNTRY"))
HOLIDAYS = str(os.getenv("HOLIDAYS", "True"))
