def amount_a(amount):
    new_amount = (amount) + 100
    return new_amount

amount = int(input("enter amount: "))

if amount > 1000:
    print("where did you see money?")
else:
    print(amount_a(amount))