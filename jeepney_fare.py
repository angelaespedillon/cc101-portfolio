distance = int(input("Distance in km: "))
discount = input("Discount? (Y or N): ")
if distance <=4:
    fare = 13.00
else:
    fare = 13.00 + (distance - 4) * 1.80
if discount == "Y" or discount == "y" :
    fare = fare * 0.80
print(f"Fare: PHP {fare:.2f} ")
