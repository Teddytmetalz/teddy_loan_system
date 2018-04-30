import random

def main():

# enter year interest rate
  annualInterestRate = eval(input("Enter year interest rate, 7.25: "))

# enter the number of years
  numberOfYears = eval(input("Enter number of years as an integer: "))

# enter loan amount
  loanAmount = eval(input("Enter loan amount, 1200000: "))

# enter borrower
  borrower = input("Enter borrower's name: ")

# create a loan object
  interest= (annualInterestRate * numberOfYears * loanAmount)/100
  
  monthly_payment = ((loanAmount + interest)/numberOfYears)/12
  
  total_amount = loanAmount + interest
#display loandate, month payment and total payment
  
  print("{} the interest in cash you were charged over {} is {}!".format(borrower, numberOfYears, interest))
  
  print("{} you owe us {} to be paid in {}!".format(borrower, total_amount, numberOfYears))

  print("Mr {} your monthly payment is {}".format(borrower, monthly_payment))

# call the main function
main()
