from brownie import FundMe, MockV3Aggregator, network, config
from scripts.pay_getPayed import (
    get_account_info,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_desentralizedBank(): 
    compte = get_account_info()
   """  check for active networks """
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][ "etherium_to_usd_price" ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": compte},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    printf("Contract deployed successfuly")
    return fund_me

def main():
    deploy_desentralizedBank()