import os
import unittest
from unittest.mock import patch

from main import get_student_info, render_page


class TestStudentApp(unittest.TestCase):

    def test_default_student_info(self):
        with patch.dict(os.environ, {
            "STUDENT_NAME": "Daniyar",
            "STUDENT_SURNAME": "Namet",
            "STUDENT_GROUP": "IT2-2312 SE",
            "STUDENT_ID": "37056"
        }):
            student = get_student_info()

            self.assertEqual(student["name"], "Daniyar")
            self.assertEqual(student["surname"], "Namet")
            self.assertEqual(student["group"], "IT2-2312 SE")
            self.assertEqual(student["id"], "37056")

    def test_environment_variables(self):
        with patch.dict(os.environ, {
            "STUDENT_NAME": "Test",
            "STUDENT_SURNAME": "User",
            "STUDENT_GROUP": "TEST-01",
            "STUDENT_ID": "12345"
        }):
            student = get_student_info()

            self.assertEqual(student["name"], "Test")
            self.assertEqual(student["id"], "12345")

    def test_html_page(self):
        page = render_page()

        self.assertIn("DevOps Student Application", page)
        self.assertIn("Student Information", page)
        self.assertIn("Application is running successfully!", page)


if __name__ == "__main__":
    unittest.main()
