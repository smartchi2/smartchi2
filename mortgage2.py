print("Welcome")
name = str(input("Enter name: "))
loanAmount = int(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate: ")) / 100
years = int(input("Enter duration of years: "))


numberofmonth = 12

monthlypaymentcost = loanAmount * rate 
* (1 + rate) * numberofmonth 
/ (( 1+ rate) * numberofmonth - 1)
   

seperate the process of the formula



mortgage = monthlypaymentcost * numberofmonth





print(f" mortgage = ${mortgage:,.2f}")
