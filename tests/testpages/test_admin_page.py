import unittest
from source.pages.admin_page import *

# Note: Write assertions for each major steps

class TestAdminPage(unittest.TestCase):

    def test_surya_code(self):
        config()

    def test_anitha_code(self):
        admin()
        job_title()
        pay_grade()
        employment_status()
        job_categories()

    def test_deepka_code(self):
        app_base()
        app_Organization()
        app_locations()
        app_Structure()
        app_nationality()

    def test_manohar_code(self):
        pass

unittest.main()