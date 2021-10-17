import unittest
from source.pages.PIM_windows import *

# Note: Write assertions for each major steps

class TestPIMPage(unittest.TestCase):

    def test_priya_code(self):
        r = pim_config()
        cust_field()

    def test_latha_code(self):
        add_employee()

    def test_kishore_code(self):
        driver = launch()
        navigate_reports()
        add_report()

    def test_srikanth_code(self):
        clicking_view_pim()
        click_termination()

    def test_pardhu_code(self):
        pim_hrm()


unittest.main()