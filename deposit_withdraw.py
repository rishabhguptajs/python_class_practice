ops = input("Enter D for deposit, W for Withdraw, E for Exit: ")
total_amount = 0

while True:
    if ops == 'D':
        deposit_amount = int(input())
        total_amount += deposit_amount
        ops = input("Enter D for deposit, W for Withdraw, E for Exit: ")
    if ops == 'W':
        withdraw_amount = int(input())
        total_amount -= withdraw_amount
        ops = input("Enter D for deposit, W for Withdraw, E for Exit: ")
    if ops == 'E':
        print("Total Amount is: ", total_amount)
        break

