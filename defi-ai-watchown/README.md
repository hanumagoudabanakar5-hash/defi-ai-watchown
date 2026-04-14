# 🛡️ DeFi AI Watchown

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Web3.py](https://img.shields.io/badge/Web3.py-Ethereum-3c3c3d.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg)
![AI](https://img.shields.io/badge/AI-Llama_3.1-00ffcc.svg)

**DeFi AI Watchown** is an autonomous Web3 security agent that monitors Ethereum wallets in real-time and uses Large Language Models (LLMs) to generate human-readable threat intelligence and risk reports.

## 🚀 Features
* **Live On-Chain Data:** Connects directly to the Ethereum Mainnet via RPC nodes (Alchemy) to fetch real-time balances and transaction history.
* **Agentic AI Analysis:** Feeds on-chain data to a Groq-powered AI (Llama 3.1) to analyze wallet behavior, detect suspicious patterns, and recommend security actions.
* **Modern Web Dashboard:** A sleek, user-friendly Streamlit frontend that allows anyone to easily input an address and view the AI's risk assessment.

## 🏗️ Architecture & Tech Stack
* **Blockchain Layer:** `Web3.py` for direct Ethereum node communication.
* **Infrastructure:** Alchemy (Ethereum RPC Provider).
* **AI Engine:** Groq API running `llama-3.1-8b-instant` for ultra-fast, low-latency inference.
* **Frontend:** Streamlit for rapid, interactive Python UI development.

## 🧠 Architectural Note: Block Scanning vs. Indexing
*Currently, this agent fetches the most recent 20 minutes of Ethereum history (approx. 33 blocks) by querying the raw RPC node block-by-block. This demonstrates a core understanding of base-layer protocol mechanics.* 
*For enterprise-scale applications requiring years of historical data (e.g., scanning all transactions from 2021 to today), this architecture would be upgraded to utilize a specialized Blockchain Indexer (like the Etherscan API or The Graph) to bypass node rate limits and reduce computational overhead.*

## 🛠️ Local Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/hanumagoudabanakar5/defi-ai-watchown.git

cd defi-ai-watchown

Install dependencies

bash
pip install -r requirements.txt

Set up Environment Variables Create a .env file in the root directory and add your API keys:

env
ALCHEMY_SEPOLIA_URL=https://eth-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY
GROQ_API_KEY=gsk_YOUR_GROQ_KEY

Run the Web Application

bash
streamlit run app.py
The app will be available at http://localhost:8501

📝 Usage
Enter any Ethereum wallet address (e.g., 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045).
The agent will fetch the live balance and recent transactions.
The AI will process the data and output a structured risk report.
