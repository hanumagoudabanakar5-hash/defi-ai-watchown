from web3 import Web3
from wallet_monitor import get_recent_transactions, get_wallet_balance
from risk_analyzer import analyze_wallet_risk

# Auto-format the address to pass the checksum validation
WALLET_RAW = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
WALLET = Web3.to_checksum_address(WALLET_RAW)

def run():
    print(f"\n🔍 Monitoring wallet: {WALLET}\n")
    
    balance = get_wallet_balance(WALLET)
    print(f"💰 Balance: {balance} ETH")
    
    print("📡 Fetching recent transactions...")
    txs = get_recent_transactions(WALLET, count=100)
    print(f"✅ Found {len(txs)} transactions\n")
    
    print("🤖 Running AI Risk Analysis...\n")
    report = analyze_wallet_risk(WALLET, balance, txs)
    
    print("=" * 50)
    print("📊 RISK REPORT")
    print("=" * 50)
    print(report)
    print("=" * 50)

if __name__ == "__main__":
    run()
