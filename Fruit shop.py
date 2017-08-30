prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pearl" : 3
}

purchased_items = {
    "banana" : 5,
    "orange" : 3
}

for key in purchased_items:
    print(key, "quantity :",purchased_items[key],"unit price :", prices[key])

Total = 0

for key in purchased_items:
    key_cost = (purchased_items[key] * prices[key])
    Total = key_cost + Total

print(Total)



