from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_URL.format(
                simple_collectible.address, simple_collectible.tokencounter() - 1
            )
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
