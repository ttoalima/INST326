import unittest
from unittest.mock import patch
from io import StringIO
import random
import time
from INST326_FinalProj import Student, match_score, find_study_partner, suggest_study_times, set_break_reminder, set_study_session, study_tips


class TestStudent(unittest.TestCase):
    def setUp(self):
        """Set up sample Student objects for testing."""
        self.student1 = Student(
            name="Alice",
            grade="10th",
            interests=["Math", "Science"],
            availability={"Monday": "6-8pm", "Wednesday": "4-6pm"},
            study_goals={"Math": 5, "Science": 3}
        )
        self.student2 = Student(
            name="Bob",
            grade="10th",
            interests=["Math", "History"],
            availability={"Monday": "6-8pm", "Tuesday": "4-6pm"},
            study_goals={"Math": 4, "History": 2}
        )

    def test_getters(self):
        """Test getters for Student attributes."""
        self.assertEqual(self.student1.get_name(), "Alice")
        self.assertEqual(self.student1.get_grade(), "10th")
        self.assertEqual(self.student1.get_interests(), ["Math", "Science"])
        self.assertEqual(self.student1.get_availability(), {"Monday": "6-8pm", "Wednesday": "4-6pm"})
        self.assertEqual(self.student1.get_study_goals(), {"Math": 5, "Science": 3})

    def test_progress_report(self):
        """Test the progress report generation."""
        report = self.student1.get_progress_report()
        expected_report = {
            "Math": {"Target Hours": 5, "Actual Hours": 0, "Status": "Falling Behind"},
            "Science": {"Target Hours": 3, "Actual Hours": 0, "Status": "Falling Behind"}
        }
        self.assertEqual(report, expected_report)

    def test_match_score(self):
        """Test the compatibility score calculation."""
        score = match_score(self.student1, self.student2)
        self.assertEqual(score, 100)  # Same grade + shared interest

    def test_find_study_partner(self):
        """Test finding a study partner."""
        best_partner, best_score = find_study_partner(self.student1, [self.student2], criteria=["interests", "grade"])
        self.assertEqual(best_partner, self.student2)
        self.assertEqual(best_score, 100)

    def test_suggest_study_times(self):
        """Test suggesting common study times."""
        common_times = suggest_study_times(self.student1, self.student2)
        self.assertEqual(common_times, ["Monday: 6-8pm"])

    def test_set_study_session(self):
        """Test scheduling a study session."""
        set_study_session(self.student1, self.student2, "Monday: 6-8pm")
        self.assertEqual(len(self.student1.get_scheduled_sessions()), 1)
        self.assertEqual(len(self.student2.get_scheduled_sessions()), 1)

    def test_update_progress(self):
        """Test updating progress."""
        self.student1.update_progress("Math", 3)
        self.assertEqual(self.student1.get_progress()["Math"], 3)
        self.assertEqual(self.student1.get_study_hours(), 3)

    def test_set_study_goal(self):
        """Test setting a study goal."""
        updated_goals = self.student1.set_study_goal("English", 2)
        self.assertIn("English", updated_goals)
        self.assertEqual(updated_goals["English"], 2)

    @patch("time.sleep", return_value=None)  # Mock sleep to speed up the test
    @patch("sys.stdout", new_callable=StringIO)
    def test_set_break_reminder(self, mock_stdout, mock_sleep):
        """Test break reminder functionality."""
        set_break_reminder(0.01)  # Minimal time for testing
        self.assertIn("Take a break!", mock_stdout.getvalue())

    @patch("random.choice", return_value="Stay hydrated and take breaks!")
    @patch("sys.stdout", new_callable=StringIO)
    def test_study_tips(self, mock_stdout, mock_random):
        """Test study tips function."""
        with patch("builtins.open", unittest.mock.mock_open(read_data="Tip 1\nTip 2\nTip 3")):
            study_tips()
        self.assertIn("Here's a tip!: 'Stay hydrated and take breaks!'", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_study_tips_file_not_found(self, mock_stdout):
        """Test study tips function when the file is missing."""
        with patch("builtins.open", side_effect=FileNotFoundError):
            study_tips()
        self.assertIn("File is missing! Please ensure tips.txt is in the same folder.", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
