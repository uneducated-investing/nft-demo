from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENV, get_contract, get_account
from brownie import network, AdvancedCollectible
import pytest
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import time


def test_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("Only for integration testing")
    # ACT
    advanced_collectible, creation_tx = deploy_and_create()
    i = 0
    while advanced_collectible.tokenCounter() == 0 and i < 360:
        time.sleep(10)
        i += 1
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
