from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENV, get_contract, get_account
from brownie import network, AdvancedCollectible
import pytest
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip()
    # ACT
    advanced_collectible, creation_tx = deploy_and_create()
    request_id = creation_tx.events["requestedCollectible"]["requestId"]
    random_num = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        request_id, random_num, advanced_collectible, {"from": get_account()}
    )
    # Assert
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_num % 3
