import unittest

from high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self):
        self.scores = [100,30,4,1]
    
    def test_latest_score_is_1(self):
        result = latest(self.scores)
        self.assertEqual(1,result)
    # Tests

    # Test latest score (the last thing in the list)


    # Test personal best (the highest score in the list)

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    

if __name__ == "__main__":
    unittest.main()
