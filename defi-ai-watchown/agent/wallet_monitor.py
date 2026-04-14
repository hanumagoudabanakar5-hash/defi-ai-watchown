from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

ALCHEMY_URL = os.getenv("ALCHEMY_SEPOLIA_URL")
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

def get_recent_transactions(wallet_address: str, count: int = 5):
    """Fetch recent blocks and find transactions for a wallet."""
    latest = w3.eth.block_number
    txs = []

    for i in range(count):
        block = w3.eth.get_block(latest - i, full_transactions=True)
        for tx in block.transactions:
            if tx['to'] == wallet_address or tx['from'] == wallet_address:
                txs.append({
                    "hash": tx['hash'].hex(),
                    "from": tx['from'],
                    "to": tx['to'],
                    "value_eth": w3.from_wei(tx['value'], 'ether'),
                    "gas": tx['gas'],
                    "block": latest - i
                })
    return txs

def get_wallet_balance(wallet_address: str):
    balance_wei = w3.eth.get_balance(wallet_address)
    return w3.from_wei(balance_wei, 'ether')
