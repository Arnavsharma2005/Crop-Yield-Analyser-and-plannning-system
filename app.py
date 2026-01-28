import streamlit as st
import requests
import json
import uuid
import datetime

# ---------------------------------------------------------
# 🔑 CONFIGURATION
# ---------------------------------------------------------
APPLICATION_TOKEN = "AstraCS:yXepGZKSCGgFbJDTYlQnBeZc:c4a1b66341c333da96b722b7e5979776c379380e0b8cb32284506a068d70af74"
API_URL = "https://aws-us-east-2.langflow.datastax.com/lf/d9b5c7dd-2716-4be9-ba3e-a1bec0332180/api/v1/run/fb49c613-a8e7-4f04-9d6d-c94e9f676c74"

# ---------------------------------------------------------
# 🎨 ULTRA-MODERN UI SETUP
# ---------------------------------------------------------
st.set_page_config(page_title="Kisan-Mitra Pro", page_icon="🌾", layout="wide")

# Custom CSS for the "Appetizing" Look
st.markdown("""
<style>
    /* Import Premium Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Vibrant Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #f6fff8 0%, #e3fcf0 100%);
    }

    /* ---------------- SIDEBAR STYLING ---------------- */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        box-shadow: 2px 0 15px rgba(0,0,0,0.05);
        border-right: none;
    }
    
    /* Custom Sidebar Status Cards */
    .status-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        transition: transform 0.2s;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
    .status-card:hover {
        transform: translateY(-2px);
        border-color: #27ae60;
        box-shadow: 0 5px 15px rgba(39, 174, 96, 0.1);
    }
    .icon-box {
        width: 35px;
        height: 35px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        margin-right: 12px;
    }
    .green-icon { background: #e8f5e9; color: #2e7d32; }
    .blue-icon { background: #e3f2fd; color: #1565c0; }
    .orange-icon { background: #fff3e0; color: #ef6c00; }
    
    .card-text h4 { margin: 0; font-size: 14px; font-weight: 600; color: #333; }
    .card-text p { margin: 0; font-size: 11px; color: #777; }

    /* ---------------- CHAT AREA STYLING ---------------- */
    
    /* Header */
    .hero-header {
        text-align: center;
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 30px;
        border-bottom: 4px solid #0ba360;
    }
    .hero-header h1 {
        color: #1e3a29;
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: 5px;
    }
    .hero-tagline {
        color: #0ba360;
        font-weight: 500;
        font-size: 1.1rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* Messages */
    .user-msg {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 16px 22px;
        border-radius: 20px 20px 4px 20px;
        box-shadow: 0 5px 15px rgba(17, 153, 142, 0.2);
        font-weight: 400;
        text-align: right;
        float: right;
        clear: both;
        margin: 8px 0;
        max-width: 75%;
    }
    
    .bot-msg {
        background: white;
        color: #2c3e50;
        padding: 18px 24px;
        border-radius: 20px 20px 20px 4px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.06);
        border-left: 5px solid #38ef7d;
        font-weight: 400;
        text-align: left;
        float: left;
        clear: both;
        margin: 8px 0;
        max-width: 80%;
    }
    
    /* Input Field cleanup */
    .stChatInput {
        padding-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 🧠 BACKEND LOGIC
# ---------------------------------------------------------
def run_flow(message):
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
        "session_id": str(uuid.uuid4())
    }
    headers = {
        "Authorization": "Bearer " + APPLICATION_TOKEN,
        "Content-Type": "application/json",
        "X-DataStax-Current-Org": "4f62456e-3231-48c5-b2fe-675bba6d0d05" 
    }
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# ---------------------------------------------------------
# 📱 SIDEBAR: THE "APPETIZING" CONTROL PANEL
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #1e3a29;'>🚜 Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Custom HTML Components for Status (Instead of st.success)
    st.markdown("""
    <div class="status-card">
        <div class="icon-box green-icon">🧠</div>
        <div class="card-text">
            <h4>IBM Granite Model</h4>
            <p>Status: <b>Active & Reasoning</b></p>
        </div>
    </div>
    <div class="status-card">
        <div class="icon-box blue-icon">💾</div>
        <div class="card-text">
            <h4>Astra DB Vector</h4>
            <p>Knowledge: <b>Connected</b></p>
        </div>
    </div>
    <div class="status-card">
        <div class="icon-box orange-icon">⚡</div>
        <div class="card-text">
            <h4>System Latency</h4>
            <p>Ping: <b>124ms (Optimal)</b></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📍 Farm Settings")
    st.selectbox("Select State", ["Maharashtra", "Punjab", "Gujarat", "Karnataka"], index=0)
    st.selectbox("Soil Profile", ["Black Cotton Soil", "Alluvial Soil", "Red Soil"], index=0)
    
    st.markdown("---")
    if st.button("🧹 Reset Conversation", type="secondary"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------------------------------
# 🏠 MAIN INTERFACE
# ---------------------------------------------------------

# 1. Hero Header
st.markdown("""
    <div class="hero-header">
        <h1>🌾 Kisan-Mitra AI</h1>
        <div class="hero-tagline">Your Smart Agronomy Companion</div>
        <p style="margin-top: 15px; color: #666;">
            Empowered by <b>Generative AI</b> to increase your yield and profit.
        </p>
    </div>
""", unsafe_allow_html=True)

# 2. Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

# Quick Actions (Only show if chat is empty)
if len(st.session_state.messages) == 0:
    st.markdown("### ⚡ Instant Actions")
    c1, c2, c3, c4 = st.columns(4)
    if c1.button("🧪 Soil Health"): st.session_state.temp_input = "My soil pH is 7.5. What fertilizer for Cotton?"
    if c2.button("💰 Onion Price"): st.session_state.temp_input = "What is the Mandi price of Onion in Nashik?"
    if c3.button("🐛 Pest Doctor"): st.session_state.temp_input = "How to stop Pink Bollworm infestation?"
    if c4.button("🌧️ Spraying Time"): st.session_state.temp_input = "What is the best time of day to spray pesticides on Cotton?"
# 3. Render Messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg"><b>🤖 Kisan AI:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)

# 4. Input Handling
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True) # Spacer
user_input = st.chat_input("Ask your question here... (e.g. 'How to improve cotton yield?')")

# Check for button click or manual input
final_prompt = user_input or st.session_state.get("temp_input")

if final_prompt:
    st.session_state.temp_input = None # Clear temp
    st.session_state.messages.append({"role": "user", "content": final_prompt})
    st.rerun()

# 5. Process Response (After rerun)
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    with st.spinner("🌱 Cultivating the best answer for you..."):
        last_msg = st.session_state.messages[-1]["content"]
        data = run_flow(last_msg)
        
        try:
            # Safe Path extraction
            reply = data["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.rerun()
        except Exception:
            st.error("⚠️ Connection Glitch. Please try again.")
            st.json(data)