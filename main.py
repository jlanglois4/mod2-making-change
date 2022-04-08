# Can add larger denominations of dollar bills in money_list
# [Adjective string, currency value, currency count, noun string]
money_list = [
    ["$20", 20, 0, "bills"],
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
    # Rounds up the input money to the nearest hundredths place to counteract floating point data loss
    if money_value[3].__contains__("pennies"):
        input_money = round(input_money, 2)
        money_value[2] = int(input_money // money_value[1])
        input_money = input_money - money_value[2] * money_value[1]
    else:
        money_value[2] = int(input_money // money_value[1])
        input_money = input_money - money_value[2] * money_value[1]

for money_value in money_list:
    if money_value[2] != 0:
        # Prints cents separately from dollars
        if money_value[0].__contains__("¢"):
            print(money_value[2], money_value[3])
        else:
            print(money_value[2], money_value[0], money_value[3])
