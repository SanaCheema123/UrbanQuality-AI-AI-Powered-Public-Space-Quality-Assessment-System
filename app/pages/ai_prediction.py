import streamlit as st
from src.predict import predict_public_space
def show():
    st.markdown("## AI Scenario Prediction Center")
    safety=st.slider("Safety Index",0,100,65); pollution=st.slider("Pollution Index",0,100,40); green=st.slider("Green Space Index",0,100,60); access=st.slider("Accessibility Index",0,100,58); comfort=st.slider("Comfort Index",0,100,62)
    input_data={"city":"Scenario City","country":"Planning Region","safety_index":safety,"healthcare_index":70,"climate_index":65,"purchasing_power_index":70,"cost_of_living_index":65,"traffic_commute_index":45,"pollution_index":pollution,"green_space_index":green,"walkability_index":65,"accessibility_index":access,"comfort_index":comfort,"latitude":40.0,"longitude":30.0}
    if st.button("Run Scenario Prediction"):
        try:
            r=predict_public_space(input_data); st.success(f"Predicted Scenario Quality: {r['quality_class']}"); st.info(f"Quality Score: {r['quality_score']}")
        except Exception as e: st.error(str(e))
