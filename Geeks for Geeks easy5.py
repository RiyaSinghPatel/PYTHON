#Python Program for Compound Interest

#A = P(1 + R/100) t 
#Compound Interest = A – P 
#Where, 
#A is amount 
#P is the principal amount 
#R is the rate and 
#T is the time span

def compound_interest(principal, rate, time):

    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    return CI
    
print("Compound interest is", compound_interest(10000, 10.25, 5))

