"""Unittests for main.py"""

from freezegun import freeze_time
from unittest.mock import patch, call

import unittest
import datetime

import main, inputs


class TestMain(unittest.TestCase):

    @patch("main.helpers.get_today_and_day_name")
    @patch("main.sys.exit")
    @patch("builtins.print")
    @patch("main.inputs")
    def test_no_deploy_on_friday(self, mock_inputs, mock_print, mock_sys_exit, mock_get_today_and_day_name):
        """Test no deploy on Friday."""
        # assign
        mock_inputs.NO_DEPLOYMENT_DAYS = "Friday, Saturday, Sunday"
        mock_inputs.TZ = "MST"
        mock_inputs.COUNTRY = "US"
        mock_inputs.HOLIDAYS = "false"
        mock_get_today_and_day_name.return_value = (datetime.datetime(2021, 8, 28), "Friday")
        
        # act
        main.main()

        # assert
        mock_print.assert_has_calls([
            call('::set-output name=reason::Do not deploy today (Friday). We do not deploy on Friday, Saturday, and Sunday.'),
            call('::set-output name=deployment::false')
        ], any_order=False)

        mock_sys_exit.assert_has_calls([call(1)], any_order=False)

    @patch("main.helpers.get_today_and_day_name")
    @patch("main.sys.exit")
    @patch("builtins.print")
    @patch("main.inputs")
    def test_deploy_on_monday(self, mock_inputs, mock_print, mock_sys_exit, mock_get_today_and_day_name):
        """Test deploy on Tuesday."""
        # assign
        mock_inputs.NO_DEPLOYMENT_DAYS = "Friday, Saturday, Sunday"
        mock_inputs.TZ = "MST"
        mock_inputs.COUNTRY = "US"
        mock_inputs.HOLIDAYS = "false"
        mock_get_today_and_day_name.return_value = (datetime.datetime(2021, 9, 30), "Monday")
        
        # act
        main.main()

        # assert
        mock_print.assert_has_calls([
            call('::set-output name=deployment::true'),
            call('::set-output name=reason::Deploying today (Monday). We deploy on Monday, Thursday, Tuesday, and Wednesday.'),
            call('::set-output name=deployment::true'),
            call('::set-output name=reason::Deploying today (Monday). We allow deployments on US holidays.')
        ], any_order=False)

        mock_sys_exit.assert_has_calls([call(0)], any_order=False)
    

    @patch("main.helpers.get_today_and_day_name")
    @patch("main.sys.exit")
    @patch("builtins.print")
    @patch("main.inputs")
    def test_deploy_on_holiday(self, mock_inputs, mock_print, mock_sys_exit, mock_get_today_and_day_name):
        """Test deploy on holiday."""
        # assign
        mock_inputs.NO_DEPLOYMENT_DAYS = "Friday, Saturday, Sunday"
        mock_inputs.TZ = "MST"
        mock_inputs.COUNTRY = "US"
        mock_inputs.HOLIDAYS = "false"
        mock_get_today_and_day_name.return_value = (datetime.datetime(2021, 9, 6), "Monday") # Labor Day Holiday
        
        # act
        main.main()

        # assert
        mock_print.assert_has_calls([
            call('::set-output name=deployment::true'),
            call('::set-output name=reason::Deploying today (Monday). We deploy on Monday, Thursday, Tuesday, and Wednesday.'),
            call('::set-output name=deployment::true'),
            call('::set-output name=reason::Deploying today (Monday). We allow deployments on US holidays.')
        ], any_order=False)

        mock_sys_exit.assert_has_calls([call(0)], any_order=False)


    @patch("main.helpers.get_today_and_day_name")
    @patch("main.sys.exit")
    @patch("builtins.print")
    @patch("main.inputs")
    def test_no_deploy_on_holiday(self, mock_inputs, mock_print, mock_sys_exit, mock_get_today_and_day_name):
        """Test no deploy on holiday."""
        # assign
        mock_inputs.NO_DEPLOYMENT_DAYS = "Friday, Saturday, Sunday"
        mock_inputs.TZ = "MST"
        mock_inputs.COUNTRY = "US"
        mock_inputs.HOLIDAYS = "true"
        mock_get_today_and_day_name.return_value = (datetime.datetime(2021, 9, 6), "Monday") # Labor Day Holiday
        
        # act
        main.main()

        # assert
        mock_print.assert_has_calls([
            call('::set-output name=deployment::true'),
            call('::set-output name=reason::Deploying today (Monday). We deploy on Monday, Thursday, Tuesday, and Wednesday.'),
            call('::set-output name=deployment::false'),
            call('::set-output name=reason::Do not deploy today (Monday). We do not deploy on US holidays.')
        ], any_order=False)

        mock_sys_exit.assert_has_calls([call(1)], any_order=False)


if __name__ == "__main__":
    unittest.main()
