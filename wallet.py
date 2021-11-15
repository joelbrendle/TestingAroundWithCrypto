
from hashlib import new
import math
import random

# Functions
def checkwalletid(getwalletid):
    walletfile = open('wallets.txt','r')
    allwalletids = walletfile.readlines()
    for walletid in allwalletids:
        if int(walletid) == getwalletid:
            return True
            break

    return False

def getbalance(walletid):
    transfile = open('transactions.txt','r')
    alltrans = transfile.readlines()
    balance = 0
    for transaction in alltrans:
        trans = transaction.split(' ')
        if int(trans[0]) == walletid:
            balance += int(trans[1])
    return balance

#end Functions



print('\n---WALLET---')
print('\nMenu:\n1) Enter Wallet-ID\n2) New Wallet')
print('\nInput:')
getinput = input()
if getinput == 1:
    print('Enter your wallet-id:')
    getwalletid = input()
    if checkwalletid(getwalletid) == True:
        print('Success')
        print('\n- Your Wallet -\n')
        print('Balance:')
        print(getbalance(getwalletid))
        print('\nMenu:\n1) Send coins\n2) Get coins')
        getinput = input()
        if getinput == 1:
            print('Send coins\n')
        elif getinput == 2:
            print('Get Coins\n')
            file = open('transactions.txt', 'a')
            print('Sending 6 Coins to walletid',getwalletid)
            file.write(str(getwalletid))
            file.write(' ')
            file.write('6\n')
            file.close
            print('Send 6 Coins')
    else:
        print('walletid not existing')
elif getinput == 2:
    print('Creating new wallet')
    walletfile = open('wallets.txt','a')
    newwalletid = random.randint(1000,9999)
    walletfile.write(str(newwalletid))
    walletfile.write('\n')
    walletfile.close()
    print('New Wallet created\n')
    print('Your new walletid is: ')
    print(newwalletid)
else:
    print('Wrong')






