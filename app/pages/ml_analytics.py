import streamlit as st, pandas as pd, plotly.express as px
from pathlib import Path
from components.data_loader import load_classification_comparison, load_regression_comparison
ROOT=Path(__file__).resolve().parents[2]; OUTPUTS=ROOT/"outputs"
def show():
    st.markdown("## ML Analytics"); class_comp=load_classification_comparison(); reg_comp=load_regression_comparison()
    st.markdown("### Classification Model Comparison")
    if not class_comp.empty:
        st.dataframe(class_comp,width="stretch",hide_index=True); st.plotly_chart(px.bar(class_comp,x="Model",y=["Accuracy","Precision","Recall","F1 Score"],barmode="group"),width="stretch")
    else: st.warning("Train model first.")
    st.markdown("### Regression Model Comparison")
    if not reg_comp.empty:
        st.dataframe(reg_comp,width="stretch",hide_index=True); st.plotly_chart(px.bar(reg_comp,x="Model",y=["R2 Score","MAE","RMSE"],barmode="group"),width="stretch")
    cm_path=OUTPUTS/"confusion_matrix.csv"
    if cm_path.exists():
        cm=pd.read_csv(cm_path,index_col=0); st.plotly_chart(px.imshow(cm,text_auto=True,aspect="auto",title="Confusion Matrix"),width="stretch")
