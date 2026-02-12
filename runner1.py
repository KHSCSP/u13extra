"""
    Total Valuation: Calculate the total value of the entire warehouse 
    (Price $\times$ Stock for every item).

    Restock Alert: Print the names of all items where stock is less than 5.

    Discount Day: Apply a 10% discount to every item in the list by updating 
    the price key within the loop.
"""


# get all data into a dictionary
all_data = []

f = open("u13_SOLNS/u13extra_dataSOLN/data1.txt")
for line in f:
    temp = line.strip().split()
    name = temp[0]
    cost = temp[1]
    quantity = temp[2]
    all_data.append({"item name":name, "cost":cost, "quantity":quantity})
f.close()

print(all_data)


# process data





