from brownie import network, accounts, config, MockV3Aggregator , FundMe
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev", "mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 18
STARTING_VALUE = 2000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"the active netwokr is {network.show_active()}")
    print("deploying mock ....")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_VALUE, "ether"), {"from": get_account()}
        )
    print("mocks deployed")

def getPaid():
    fund_me = FundMe[-1]
    account = get_account_info()
    fund_me.withdrow({"from": account})

def Deposit():
    fund_me = FundMe[-1]
    account = get_account_info()
    starting_price = fund_me.getEntranceFee() + 50
    printf(starting_price)
    printf("Actual price is {starting_price}")
    fund_me.fund({"from": account, "": starting_price})

def main():
    getPaid()
    Deposit()