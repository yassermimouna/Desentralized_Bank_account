from brownie import FundMe
from scripts.helpful_scripts import get_account

def getPaid():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdrow({"from": account})

def Deposit():
    fund_me = FundMe[-1]
    account = get_account()
    starting_price = fund_me.getEntranceFee() + 50
    printf(starting_price)
    printf("Actual price is {starting_price}")
    fund_me.fund({"from": account, "": starting_price})

def main():
    getPaid()
    Deposit()