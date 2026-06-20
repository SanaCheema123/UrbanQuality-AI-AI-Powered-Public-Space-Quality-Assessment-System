import streamlit as st, plotly.express as px
from components.data_loader import load_data
def show():
    st.markdown("## Urban Analytics"); df=load_data()
    if df.empty: st.warning("Dataset not available."); return
    num_cols=df.select_dtypes(include="number").columns.tolist()
    if num_cols:
        col=st.selectbox("Select Urban Indicator",num_cols); st.plotly_chart(px.histogram(df,x=col,color="public_space_quality",nbins=35),width="stretch")
    if {"safety_index","pollution_index","public_space_quality"}.issubset(df.columns):
        st.plotly_chart(px.scatter(df,x="safety_index",y="pollution_index",color="public_space_quality",title="Safety vs Pollution"),width="stretch")
    if len(num_cols)>1: st.plotly_chart(px.imshow(df[num_cols].corr(),text_auto=".2f",aspect="auto",title="Urban Indicator Correlation"),width="stretch")
