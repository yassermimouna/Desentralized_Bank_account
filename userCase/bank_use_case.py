from scripts.deploy_desentralizedBank import fund
from scripts.pay_getPayed import (
    get_account_info,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    FORKED_LOCAL_ENVIRONMENTS,
)
from scripts.deployment import deploy_desentralizedBank
from brownie import network, accounts, exceptions
import pytest


def test_my_bank():
    account = get_account_info()
    fund_me = deploy_desentralizedBank()
    entrance_fee = fund_me.getEntranceFee() + 80
    txs = fund_me.fund({"from": account, "value": entrance_fee})
    txs.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    txsAux = fund_me.withdrow({"from": account})
    txsAux.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0