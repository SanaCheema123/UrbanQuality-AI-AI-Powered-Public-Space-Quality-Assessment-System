import streamlit as st
from components.data_loader import load_data, load_classification_comparison, load_regression_comparison
def show():
    st.markdown("## Reports"); df=load_data(); c=load_classification_comparison(); r=load_regression_comparison()
    if not df.empty: st.download_button("Download Processed Dataset",df.to_csv(index=False),"processed_urban_quality.csv","text/csv")
    if not c.empty: st.download_button("Download Classification Report",c.to_csv(index=False),"classification_report.csv","text/csv")
    if not r.empty: st.download_button("Download Regression Report",r.to_csv(index=False),"regression_report.csv","text/csv")
