import os
import streamlit as st

# --- CLOUD SECRETS INJECTION ---
# When deployed to Streamlit Cloud, pull secure keys from the dashboard vault
# and inject them into the system environment so the backend can read them!
try:
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    if "ALCHEMY_SEPOLIA_URL" in st.secrets:
        os.environ["ALCHEMY_SEPOLIA_URL"] = st.secrets["ALCHEMY_SEPOLIA_URL"]
except:
    pass # If testing locally, it will just use your .env file normally

from agent.wallet_monitor import get_recent_transactions, get_wallet_balance
from agent.risk_analyzer import analyze_wallet_risk
from web3 import Web3

# Configure the page layout
st.set_page_config(page_title="DeFi AI Watchown", page_icon="🛡️", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ About Project")
    st.info("DeFi AI Watchown is an autonomous Web3 Agent that analyzes Ethereum wallets and generates AI security reports.")
    st.subheader("🛠️ Tech Stack:")
    st.write("🔹 **Frontend:** Streamlit\n🔹 **Blockchain:** Web3.py & Alchemy\n🔹 **AI Engine:** Groq (Llama 3.1)")

# --- MAIN DASHBOARD ---
st.markdown("<h1 style='text-align: center;'>🛡️ DeFi AI Watchown</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 18px;'>Autonomous Web3 Security Agent</p>", unsafe_allow_html=True)
st.write("---")

# Layout for the search bar (centered)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    wallet_input = st.text_input("🔍 Enter Ethereum Wallet Address:", "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
    analyze_btn = st.button("🚀 Run AI Analysis", use_container_width=True)

# When the button is clicked
if analyze_btn:
    if not wallet_input:
        st.warning("⚠️ Please enter a valid wallet address.")
    else:
        try:
            # Format address
            wallet_address = Web3.to_checksum_address(wallet_input.strip().lower())
            
            # Animated Status Box
            with st.status("🕵️‍♂️ Agent is investigating...", expanded=True) as status:
                st.write("📡 Connecting to Ethereum blockchain...")
                balance = get_wallet_balance(wallet_address)
                
                st.write("🔎 Scanning blocks for transactions...")
                txs = get_recent_transactions(wallet_address, count=300)
                
                st.write("🧠 Feeding data to Llama 3.1 AI Model...")
                report = analyze_wallet_risk(wallet_address, balance, txs)
                
                status.update(label="✅ Analysis Complete!", state="complete", expanded=False)

            # --- RESULTS DASHBOARD ---
            st.subheader("📊 Wallet Overview")
            
            # Big Metric Cards
            m1, m2, m3 = st.columns(3)
            m1.metric(label="💰 Current Balance", value=f"{balance:.4f} ETH")
            m2.metric(label="🔄 Recent Transactions", value=len(txs))
            m3.metric(label="🌐 Network", value="Ethereum Mainnet")

            st.divider()

            # AI Report formatted naturally!
            st.subheader("🤖 AI Security Report")
            st.markdown(report)

            # Expandable section for developers to see raw data
            st.write("")
            with st.expander("👀 View Raw Transaction Data (JSON)"):
                if txs:
                    st.json(txs)
                else:
                    st.write("No transactions found in the scanned blocks.")

        except Exception as e:
            st.error(f"❌ Error validating address or fetching data. Details: {e}")
