#Tip Calc
print("Welcome to the Tip Calculator")
bill = input("Please enter the total bill: $ ")
tip = input("What percentage tip would you like to give? 10, 15 or 20? ")
people = input("How many people to split the bill? ")
final = (float(bill) * ((float(tip)/100)+1))/int(people)
print("Each person will need to contribute " + format(final,".2f"))