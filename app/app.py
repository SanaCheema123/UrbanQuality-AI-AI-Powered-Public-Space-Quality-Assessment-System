import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT)); sys.path.append(str(Path(__file__).resolve().parent))
from pages import dashboard, public_space_assessment, urban_analytics, ai_prediction, gis_visualization, ml_analytics, reports, about

st.set_page_config(page_title="UrbanQuality AI", page_icon="🏙️", layout="wide", initial_sidebar_state="collapsed")
css_path = Path(__file__).resolve().parent / "assets" / "style.css"
st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

st.markdown("""
<div class="topbar"><div class="logo-area"><div class="logo">🏙️</div><div><h3>UrbanQuality AI</h3><p>Public Space Quality • Urban Planning • AI Analytics</p></div></div><div class="profile"><input placeholder="Search city or indicator..." /><span>🔔</span><span>👩‍💼</span></div></div>
""", unsafe_allow_html=True)

nav_items = ["Dashboard","Public Space Assessment","Urban Analytics","AI Prediction","GIS Visualization","ML Analytics","Reports","About Project"]
cols = st.columns(len(nav_items))
for col, item in zip(cols, nav_items):
    with col:
        btn_type = "primary" if st.session_state.page == item else "secondary"
        if st.button(item, key=f"nav_{item}", type=btn_type, use_container_width=True):
            st.session_state.page = item
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)
page = st.session_state.page
if page == "Dashboard": dashboard.show()
elif page == "Public Space Assessment": public_space_assessment.show()
elif page == "Urban Analytics": urban_analytics.show()
elif page == "AI Prediction": ai_prediction.show()
elif page == "GIS Visualization": gis_visualization.show()
elif page == "ML Analytics": ml_analytics.show()
elif page == "Reports": reports.show()
else: about.show()
