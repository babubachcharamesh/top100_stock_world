import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    :root {
        --primary-neon: #00f2ff;
        --secondary-neon: #7000ff;
        --bg-dark: #0a0a12;
        --card-bg: rgba(255, 255, 255, 0.05);
        --text-bright: #ffffff;
    }
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #0a0a12 100%);
        color: var(--text-bright);
    }
    
    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        background: linear-gradient(to right, var(--primary-neon), var(--secondary-neon));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .stMetric {
        background: var(--card-bg);
        border: 1px solid rgba(0, 242, 255, 0.2);
        padding: 15px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease;
    }
    
    .stMetric:hover {
        transform: translateY(-5px);
        border-color: var(--primary-neon);
    }
    
    .highlight-card {
        background: var(--card-bg);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 20px;
        backdrop-filter: blur(15px);
        margin: 10px 0;
    }
    
    .neon-text {
        color: var(--primary-neon);
        text-shadow: 0 0 10px rgba(0, 242, 255, 0.5);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: var(--card-bg);
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .stTabs [aria-selected="true"] {
        border-bottom: 2px solid var(--primary-neon) !important;
        background: rgba(0, 242, 255, 0.1) !important;
    }
    
    /* Custom Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0d0d1a !important;
        border-right: 1px solid rgba(0, 242, 255, 0.1);
    }
    
    </style>
    """, unsafe_allow_html=True)
