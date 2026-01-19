import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def render_summary_metrics(df):
    col1, col2, col3, col4 = st.columns(4)
    total_market_cap = df['market_cap_billion'].sum()
    total_employees = df['employees'].sum()
    avg_pe = df['pe_ratio'].dropna().mean()
    
    with col1:
        st.metric("Total Market Cap", f"${total_market_cap/1000:.2f}T")
    with col2:
        st.metric("Total Employees", f"{total_employees/1e6:.1f}M")
    with col3:
        st.metric("Avg P/E Ratio", f"{avg_pe:.1f}")
    with col4:
        st.metric("Top Sector", df['sector'].mode()[0])

def render_sector_analysis(df):
    st.subheader("Sector Breakdown")
    sector_data = df.groupby('sector').agg({
        'market_cap_billion': 'sum',
        'name': 'count'
    }).reset_index().rename(columns={'name': 'company_count'})
    
    fig = px.sunburst(df, path=['sector', 'name'], values='market_cap_billion',
                  title="Sector & Company Market Cap Hierarchy",
                  color='market_cap_billion', color_continuous_scale='RdBu')
    st.plotly_chart(fig, use_container_width=True)

def render_geographic_map(df):
    st.subheader("Global Footprint")
    country_data = df.groupby('country').agg({
        'name': 'count',
        'market_cap_billion': 'sum'
    }).reset_index()
    
    fig = px.choropleth(country_data, 
                        locations="country", 
                        locationmode='country names',
                        color="market_cap_billion",
                        hover_name="country",
                        title="Market Cap by Country",
                        color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(fig, use_container_width=True)

def render_roi_calculator(df):
    st.subheader("🚀 Investment ROI Simulator")
    st.markdown("What if you invested some money 1 year ago? (Simulated based on Current Position)")
    
    col1, col2 = st.columns(2)
    with col1:
        investment = st.number_input("Investment Amount ($)", min_value=100, value=1000, step=100)
    with col2:
        selected_company = st.selectbox("Select Company", options=df['name'].tolist())
    
    company_info = df[df['name'] == selected_company].iloc[0]
    # Synthetic ROI calculation (just for fun/feature demo)
    # Using a deterministic random based on rank for simulation
    roi_factor = 1.1 + (100 - company_info['rank']) / 300.0
    final_value = investment * roi_factor
    profit = final_value - investment
    
    st.markdown(f"""
    <div class='highlight-card'>
        <h3>Simulation for <span class='neon-text'>{selected_company}</span></h3>
        <p>Estimated ROI (Past Year): <b>{ (roi_factor-1)*100 :.1f}%</b></p>
        <p>Final Portfolio Value: <b>${final_value:,.2f}</b></p>
        <p>Estimated Profit: <span style='color: #00ff00;'>+${profit:,.2f}</span></p>
    </div>
    """, unsafe_allow_html=True)

def render_productivity_chart(df):
    st.subheader("Efficiency: Market Cap per Employee")
    top_prod = df[df['employees'] > 0].nlargest(15, 'cap_per_employee')
    fig = px.bar(top_prod, x='name', y='cap_per_employee', color='sector',
                 title="Efficiency Leaders (Million USD per Employee)",
                 labels={'cap_per_employee': 'Cap/Employee (M USD)', 'name': 'Company'})
    st.plotly_chart(fig, use_container_width=True)

def render_data_table(df):
    st.subheader("Comprehensive Market Data")
    st.dataframe(
        df[['rank', 'name', 'sector', 'country', 'market_cap_billion', 'price', 'pe_ratio', 'employees']],
        use_container_width=True,
        column_config={
            "market_cap_billion": st.column_config.NumberColumn("Market Cap ($B)", format="$%.2fB"),
            "price": st.column_config.NumberColumn("Price ($)", format="$%.2f"),
            "pe_ratio": st.column_config.NumberColumn("P/E Ratio", format="%.1f"),
            "employees": st.column_config.NumberColumn("Employees", format="%d")
        }
    )
