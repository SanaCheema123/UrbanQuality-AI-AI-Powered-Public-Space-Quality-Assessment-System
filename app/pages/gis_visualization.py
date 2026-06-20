import streamlit as st, plotly.express as px
from components.data_loader import load_data
def show():
    st.markdown("## GIS Visualization"); df=load_data()
    if df.empty: st.warning("Dataset not available."); return
    if {"latitude","longitude","public_space_quality"}.issubset(df.columns):
        fig=px.scatter_map(df,lat="latitude",lon="longitude",color="public_space_quality",size="quality_of_life_index" if "quality_of_life_index" in df.columns else None,zoom=2,height=560,title="Public Space Quality Map")
        st.plotly_chart(fig,width="stretch")
    else: st.info("Latitude and longitude columns are not available.")
