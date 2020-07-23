import unittest

from high_scores import (
    latest,
    personal_best,
    personal_top_three,
    sorted_descending_order,
    top_three
)

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [100, 30, 100, 1, 40, 3]

    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score_is_1(self):
        result = latest(self.scores)
        self.assertEqual(3, result)

    # Test personal best (the highest score in the list)
    def test_personal_best_is_100(self):
        result = personal_best(self.scores)
        self.assertEqual(100, result)

    # Test top three from list of scores
    def test_top_3_100_100_40(self):
        result = personal_top_three(self.scores)
        the_list = [100, 100, 40]
        self.assertEqual(the_list, result)

    # Test ordered from highest tp lowest
    def test_order_from_highest_to_lowest(self):
        result = sorted_descending_order(self.scores)
        the_list = [100, 100, 40, 30, 3, 1]
        self.assertEqual(the_list, result)

    # Test top three when there is a tie
    def test_top_3_when_tied_for_first(self):
        result = top_three(self.scores)
        the_list = [100,100,40]
        self.assertEqual(the_list, result)
    # Test top three when there are less than three

    # Test top three when there is only one


if __name__ == "__main__":
    unittest.main()
