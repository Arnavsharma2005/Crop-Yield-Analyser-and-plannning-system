# 🌾 Kisan-Mitra AI (Farmer's Friend)

<div align="center">

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Tech](https://img.shields.io/badge/Stack-IBM_Granite_%7C_Langflow_%7C_AstraDB-blue)
![UI](https://img.shields.io/badge/UI-Streamlit-red)

**An Intelligent Multi-Agent System empowering Indian Farmers with precision agriculture, real-time market insights, and weather planning.**

*Powered by IBM watsonx.ai & Langflow*

[View Demo](#) • [Report Bug](#) • [Request Feature](#)

</div>

---

## 📖 Overview
**Kisan-Mitra AI** is a GenAI-powered agronomy advisor designed to bridge the information gap for rural farmers. unlike generic chatbots, it uses a **Multi-Agent RAG Architecture** to provide scientifically accurate answers based on localized soil data, government schemes, and live market trends.

### 🌟 Key Features
* **🌱 Yield Analysis Agent:** Uses RAG (Retrieval Augmented Generation) to analyze soil data (NPK values, pH) from `india_yield_data.csv` to recommend precise fertilizers.
* **💰 Market Trend Agent:** Provides real-time insights on crop prices (Mandi rates) to help farmers sell at the right time.
* **🌧️ Weather Planning Agent:** Suggests farming activities (spraying, sowing, harvesting) based on weather forecasts.
* **🏛️ Govt Scheme Agent:** Educates farmers about subsidies and insurance schemes relevant to their region.

---

## ⚙️ How It Works (Architecture)

The system is built using a **Low-Code/No-Code** approach with **Langflow** as the orchestrator.

1.  **Input:** Farmer asks a question via the Streamlit UI.
2.  **Orchestration (Langflow):** The query is routed to the specific agent (Soil, Market, or Weather).
3.  **Retrieval (Astra DB):** Vector search retrieves relevant context from the uploaded dataset.
4.  **Generation (IBM Granite):** The **IBM Granite-13b-chat-v2** model generates a human-like, accurate response.
5.  **Output:** The answer is displayed in the UI with strict formatting.

---

## 📸 Screenshots

### 1. The Dashboard (v2.0 UI)
![Dashboard](path/to/your/dashboard_screenshot.png)
*Professional, clean interface with Quick Action buttons.*

### 2. Langflow Orchestration
![Langflow](path/to/your/langflow_screenshot.png)
*Complex multi-agent routing logic handled visually.*

---

## 🛠️ Tech Stack

| Component | Technology | Usage |
| :--- | :--- | :--- |
| **LLM** | **IBM Granite-13b-chat-v2** | Core reasoning and response generation. |
| **Orchestration** | **Langflow** | Flow management and Agent routing. |
| **Vector Database** | **DataStax Astra DB** | Storing soil data embeddings for RAG. |
| **Frontend** | **Streamlit (Python)** | User interface and interaction. |
| **Embedding Model** | **IBM watsonx Embeddings** | Converting text to vectors. |

---

## 🚀 Installation & Setup

Follow these steps to run the project locally.

### Prerequisites
* Python 3.9+
* An IBM Cloud Account (for watsonx.ai)
* A DataStax Astra DB Account

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/kisan-mitra-ai.git](https://github.com/your-username/kisan-mitra-ai.git)
cd kisan-mitra-ai
