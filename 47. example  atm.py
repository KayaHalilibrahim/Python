

#ATM
#ATM

sadikAccount = {
    'name': 'Sadık Turan',
    'account_no': '131531',
    'balance': 3000,
    'overdraft': 2000
}

aliAccount = {
    'name': 'Ali Turan',
    'account_no': '1131',
    'balance': 2000,
    'overdraft': 1000
}

def withdrawMoney(account, amount):
    print(f'Hello {account["name"]}')
    
    if account['balance'] >= amount:
        account['balance'] -= amount
        print('You can take your money.')
        
    else:
        total = account['balance'] + account['overdraft']
        
        if total >= amount:
            overdraftUse = input('Use overdraft (y/n): ')
            
            if overdraftUse == 'y':
                overdraftUsedAmount = amount - account['balance']
                account['balance'] = 0
                account['overdraft'] -= overdraftUsedAmount
                print('You can take your money.')
            else:
                print(f'Your account number {account["account_no"]} has {account["balance"]} remaining.')
        else:
            print('Sorry, insufficient funds.')
    
withdrawMoney(sadikAccount, 5000)
withdrawMoney(sadikAccount, 1000)
