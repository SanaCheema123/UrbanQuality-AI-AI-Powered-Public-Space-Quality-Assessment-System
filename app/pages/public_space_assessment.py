import streamlit as st
from src.predict import predict_public_space
def show():
    st.markdown("## Public Space Quality Assessment")
    c1,c2,c3=st.columns(3)
    with c1:
        city=st.text_input("City","Vienna"); country=st.text_input("Country","Austria"); safety_index=st.number_input("Safety Index",0.0,100.0,78.0); healthcare_index=st.number_input("Healthcare Index",0.0,100.0,82.0)
    with c2:
        climate_index=st.number_input("Climate Index",0.0,100.0,75.0); purchasing_power_index=st.number_input("Purchasing Power Index",0.0,150.0,85.0); cost_of_living_index=st.number_input("Cost of Living Index",0.0,150.0,65.0); traffic_commute_index=st.number_input("Traffic Commute Index",0.0,100.0,35.0)
    with c3:
        pollution_index=st.number_input("Pollution Index",0.0,100.0,22.0); green_space_index=st.number_input("Green Space Index",0.0,100.0,80.0); walkability_index=st.number_input("Walkability Index",0.0,100.0,76.0); accessibility_index=st.number_input("Accessibility Index",0.0,100.0,72.0); comfort_index=st.number_input("Comfort Index",0.0,100.0,78.0)
    input_data={"city":city,"country":country,"safety_index":safety_index,"healthcare_index":healthcare_index,"climate_index":climate_index,"purchasing_power_index":purchasing_power_index,"cost_of_living_index":cost_of_living_index,"traffic_commute_index":traffic_commute_index,"pollution_index":pollution_index,"green_space_index":green_space_index,"walkability_index":walkability_index,"accessibility_index":accessibility_index,"comfort_index":comfort_index,"latitude":48.2,"longitude":16.3}
    if st.button("Assess Public Space Quality"):
        try:
            result=predict_public_space(input_data); st.success(f"Predicted Quality Class: {result['quality_class']}"); st.info(f"Predicted Quality Score: {result['quality_score']} | Confidence: {result['confidence']}%")
        except Exception as e: st.error(str(e))
