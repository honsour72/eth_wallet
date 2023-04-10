from eth_account import Account
import secrets


def create_web3_wallet() -> tuple:
    """
    Source:
    https://www.quicknode.com/guides/ethereum-development/wallets/how-to-generate-a-new-ethereum-address-in-python/
    :return:
    """
    private_key = secrets.token_hex(32)
    private_key = "0x" + private_key
    account = Account.from_key(private_key)
    return private_key, account.address

