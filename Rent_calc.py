 #input:
#total rent
#total food order
#electricity units spend
#charge per unit

#output:
#total qmount you'have to pay

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charges_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

electricity_bill = electricity_spend * charges_per_unit 
# print(electricity_bill)

total_Amount_Pay = (rent + food + electricity_bill) / persons
print("Each persons will pay is",total_Amount_Pay)