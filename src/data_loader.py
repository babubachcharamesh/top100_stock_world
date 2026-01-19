import pandas as pd
import json
import streamlit as st

@st.cache_data
def load_company_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    
    # Preprocessing
    df['employees'] = df['employees'].fillna(0).astype(int)
    
    # Calculate Cap per Employee (in millions USD)
    df['cap_per_employee'] = (df['market_cap_billion'] * 1e9 / df['employees'].replace(0, 1)) / 1e6
    df['cap_per_employee'] = df['cap_per_employee'].where(df['employees'] > 0, 0)
    
    # Calculate P/S (Price to Sales) ratio using synthetic revenue
    df['ps_ratio'] = df['market_cap_billion'] / df['revenue_billion']
    
    return df

def format_market_cap(value):
    if value >= 1000:
        return f"${value / 1000:.2f}T"
    else:
        return f"${value:.2f}B"

def filter_data(df, search_term, country_filter, sector_filter, min_cap):
    filtered_df = df.copy()
    if search_term:
        filtered_df = filtered_df[filtered_df['name'].str.contains(search_term, case=False)]
    if country_filter:
        filtered_df = filtered_df[filtered_df['country'].isin(country_filter)]
    if sector_filter:
        filtered_df = filtered_df[filtered_df['sector'].isin(sector_filter)]
    
    filtered_df = filtered_df[filtered_df['market_cap_billion'] >= min_cap]
    return filtered_df
