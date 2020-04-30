buy = 0
while True:
    product = input("Buy an Food, Water or Guns Type Cancel to Cancel")
    if product == "Food":
        print ("Sold")
        buy = buy + 200
    if product == "Water":
        print ("Sold")
        buy = buy + 100
    if product == "Guns":
        print ("Sold")
        buy = buy + 70
    if product == "Cancel":
        break
print (buy)

