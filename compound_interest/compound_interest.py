class CompoundInterest:

    def __init__(self, principal_amount, annual_rate, years):
        self.principal_amount = principal_amount
        self.annual_rate = annual_rate
        self.years = years
    
    def calculate_compound_interest(self):
        
        p = self.principal_amount
        r = self.annual_rate/100
        t = self.years
        n = 12
        
        a = (p*(1+(r/n)) ** (n*t))
        return round(a,2)

#print("12121")


        
#         A = P(1 + r/n)

#         P is the principal amount
# - r is the annual rate of interest
# - t is the number of years the amount is invested
# - n is the number of times the interest is compounded per year
# - A is the amount at the end of the investment
