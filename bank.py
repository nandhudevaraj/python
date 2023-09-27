def main():
    bank_name = input('Enter bank name: ')
    bank = Bank(bank_name)
    print('Bank', bank_name, 'created successfully')
    while True:
        print('1. Create Account')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            acc_number = input('Enter account number: ')
            acc_owner = input('Enter account owner name: ')
            acc_balance = float(input('Enter opening balance: '))
            account = Account(acc_number, acc_owner, acc_balance)
            bank.add_account(account)
            print('Account created successfully')
        elif choice == 2:
            acc_number = input('Enter account number: ')
            amount = float(input('Enter amount to deposit: '))
            account = find_account(bank.accounts, acc_number)
            if account:
                account.deposit(amount)
                print('Deposit successful')
            else:
                print('Account not found')
        elif choice == 3:
            acc_number = input('Enter account number: ')
            amount = float(input('Enter amount to withdraw: '))
            account = find_account(bank.accounts, acc_number)
            if account:
                account.withdraw(amount)
                print('Withdrawal successful')
            else:
                print('Account not found')
        elif choice == 4:
            print('Thank you for using the Bank Management System')
            break
        else:
            print('Invalid choice')

def find_account(accounts, number):
    for account in accounts:
        if account.number == number:
            return account
    return None

if __name__ == '__main__':
    main()
