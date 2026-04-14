import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_wallet_risk(wallet_address: str, balance: float, transactions: list):
    """Send wallet data to Groq for risk analysis."""
    tx_summary = "\n".join([
        f"- TX {t['hash'][:10]}...: {t['value_eth']} ETH from {t['from'][:8]}... to {t['to'][:8] if t['to'] else 'contract'}..."
        for t in transactions
    ]) or "No recent transactions found."

    prompt = f"""
You are a DeFi security analyst. Analyze this Ethereum wallet activity.

Wallet: {wallet_address}
Balance: {balance} ETH

Recent Transactions:
{tx_summary}

Provide a short risk report covering:
1. Risk Level (LOW / MEDIUM / HIGH)
2. Suspicious patterns (if any)
3. One recommendation

Keep it under 150 words.
"""

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant", # <-- Updated to the newest supported model!
    )

    return chat_completion.choices[0].message.content
