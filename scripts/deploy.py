from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)

def deploy_desentralizedBank():  //deploy_fund_me
    compte = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "ethirium_to_usd_price"
        ]
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
