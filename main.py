import streamlit as st
import os
from src.styles import apply_custom_css
from src.data_loader import load_company_data, filter_data
from src.components import (
    render_summary_metrics, 
    render_sector_analysis, 
    render_geographic_map, 
    render_roi_calculator, 
    render_productivity_chart,
    render_data_table
)

# Page configuration
st.set_page_config(
    page_title="Ultra Modern Stock Dashboard 2026",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Styles
apply_custom_css()

# Load Data
DATA_PATH = os.path.join("data", "companies.json")
df = load_company_data(DATA_PATH)

# Sidebar - Filter Logic
st.sidebar.image("https://img.icons8.com/nolan/128/bar-chart.png", width=100)
st.sidebar.title("Dashboard Controls")

search_term = st.sidebar.text_input("🔍 Search Company", "")
country_filter = st.sidebar.multiselect("🌍 Filter by Country", options=sorted(df['country'].unique()))
sector_filter = st.sidebar.multiselect("🏗️ Filter by Sector", options=sorted(df['sector'].unique()))
min_cap = st.sidebar.slider("💰 Minimum Market Cap ($B)", min_value=0, max_value=5000, value=0)

# Filter Data
filtered_df = filter_data(df, search_term, country_filter, sector_filter, min_cap)

# Main Content
st.markdown("<h1 class='main-title'>Top 100 Global Market Leaders</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Live Intelligence Feed • January 2026</p>", unsafe_allow_html=True)

# Summary Row
render_summary_metrics(filtered_df)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Global Market View", 
    "📈 Sector & Efficiency", 
    "🗺️ Geographic Heatmap", 
    "💸 ROI Simulator"
])

with tab1:
    render_data_table(filtered_df)
    
    # Download button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button("📥 Export Market Data", csv, "market_leaders_2026.csv", "text/csv")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        render_sector_analysis(filtered_df)
    with col2:
        render_productivity_chart(filtered_df)

with tab3:
    render_geographic_map(filtered_df)

with tab4:
    render_roi_calculator(filtered_df)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; opacity: 0.6;'>"
    "Data Intelligence by CompaniesMarketCap • AI Analysis Engine v4.0 • © 2026 Dashboard Ultra"
    "</div>", 
    unsafe_allow_html=True
)