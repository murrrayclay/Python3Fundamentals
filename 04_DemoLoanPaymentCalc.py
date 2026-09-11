# Get details of loan
money_owed = float(input('How many $ do you owe?\n')) #50,000
apr = float(input('what is the annual percentage rate of the loan?\n')) #3
payment = float(input('how much $ will u pay each month?\n')) #1,000
months = int(input("How many months do you want tpo see the results for?\n")) #24

monthly_rate = apr/100/12

for i in range(months):
    # calc interest to pay
    interest_paid = money_owed*monthly_rate
    # Add in interest
    money_owed = money_owed + interest_paid
    
    if (money_owed - payment < 0):
        print('last payment ', f"{money_owed:.2f}")
        print('loan paid in ', i+1, 'months')
        break  
    
    # make payment
    money_owed = money_owed - payment

    print('paid ', payment, ' of which ', f"{interest_paid:.2f}", ' was interest', end=' ')
    print('now i owe ', f"{money_owed:.2f}" )
