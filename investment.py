print("welcome to Smart investors plc")
name = str(input("Enter your name: "))
investment = float(input("Enter investment amount: "))
rate = float(input("Enter annual rate: ")) * 100
years = int(input("Enter number of years: "))
deposit = float(input("Enter deposited amounts: "))

number_Of_Months = 12

monthly_Deposits = investment * rate * (1+ rate) * number_Of_Months / (( 1+ rate) * number_Of_Months - 1)

expected_rate = monthly_Deposits * number_Of_Months 

print(f" Your expected rate is ₦ {expected_rate:,.2f}", name)