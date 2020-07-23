import unittest

from compound_interest import CompoundInterest


class CompoundInterestTest(unittest.TestCase):
    
    # Tests
    def test_compound_interest_return_73281_on_100_10percent_20_years(self):
        calculator = CompoundInterest(100,10,20)
        result = calculator.calculate_compound_interest()
        self.assertEqual(732.81, result)

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    
    def test_compound_interest_return_18194_on_100_6percent_10_years(self):
        calculator = CompoundInterest(100,6,10)
        result = calculator.calculate_compound_interest()
        self.assertEqual(181.94, result)
    # Should return 181.94 given 100 principal, 6 percent, 10 years

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years

    # Should return 0.00 given 0 principal, 10 percent, 1 year

    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month


if __name__ == "__main__":
    unittest.main()
