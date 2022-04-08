money_list = [["$20", 20, 0, "bills"],
              ["10", 10, 0, "bills"],
              ["$5", 5, 0, "bills"],
              ["$1", 1, 0, "bills"],
              ["¢25", .25, 0, "quarters"],
              ["¢10", .1, 0, "dimes"],
              ["¢5", .05, 0, "nickels"],
              ["¢1", .01, 0, "pennies"]
              ]

input_money = float(input("Please enter your money amount:"))

for money_value in money_list:
    money_value[2] = int(input_money // money_value[1])
    input_money = input_money - money_value[2] * money_value[1]

for money_value in money_list:
    if money_value[2] != 0:
        if money_value[0].__contains__("¢"):
            print(money_value[2], money_value[3])
        else:
            print(money_value[2], money_value[0], money_value[3])