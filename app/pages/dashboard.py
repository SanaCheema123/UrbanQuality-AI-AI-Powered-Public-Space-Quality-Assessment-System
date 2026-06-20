import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from components.data_loader import load_data, load_metadata


def metric_card(icon, title, value, sub, color):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon" style="background:{color};">{icon}</div>
            <div>
                <p>{title}</p>
                <h2>{value}</h2>
                <span>{sub}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show():
    df = load_data()
    meta = load_metadata()

    if df.empty:
        st.warning("Dataset not found. Run: py src/generate_sample_data.py and py src/train_model.py")
        return

    avg_quality = (
        f"{df['quality_of_life_index'].mean():.2f}"
        if "quality_of_life_index" in df.columns
        else "-"
    )

    accuracy = f"{meta.get('classification_accuracy', 0) * 100:.2f}%"
    r2 = f"{meta.get('regression_r2', 0) * 100:.2f}%"

    country_count = df["country"].nunique() if "country" in df.columns else "-"
    total_cities = f"{len(df):,}"

    st.markdown(
        """
        <div class="urban-hero">
            <div>
                <h4>Welcome back, Admin! 👋</h4>
                <h1>Urban Intelligence Dashboard</h1>
                <p>
                    AI-powered public space quality assessment for evaluating
                    livability, safety, comfort, accessibility, sustainability,
                    and urban well-being.
                </p>
                <div class="hero-actions">
                    <span class="hero-btn-primary">Explore Analytics →</span>
                    <span class="hero-btn-outline">Generate Report 📄</span>
                </div>
            </div>
            <div class="hero-city">🏙️✨🌳</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        metric_card("🏙️", "Total Cities", total_cities, "Urban samples", "#dbeafe")

    with c2:
        metric_card("🌍", "Countries", country_count, "Global coverage", "#dcfce7")

    with c3:
        metric_card("⭐", "Avg Quality Score", avg_quality, "Out of 100", "#fef3c7")

    with c4:
        metric_card("🎯", "ML Accuracy", accuracy, "Classifier performance", "#d1fae5")

    with c5:
        metric_card("📈", "Score R²", r2, "Regressor score", "#ede9fe")

    st.markdown("<br>", unsafe_allow_html=True)

    row1_left, row1_mid, row1_right, row1_side = st.columns([1.15, 1.15, 1.1, 0.85])

    with row1_left:
        st.markdown('<div class="chart-card"><h3>Quality Class Distribution</h3>', unsafe_allow_html=True)

        if "public_space_quality" in df.columns:
            counts = df["public_space_quality"].value_counts().reset_index()
            counts.columns = ["Quality Class", "Cities"]

            fig = px.pie(
                counts,
                names="Quality Class",
                values="Cities",
                hole=0.52,
                color="Quality Class",
                color_discrete_map={
                    "Excellent": "#16a34a",
                    "Good": "#2563eb",
                    "Moderate": "#f59e0b",
                    "Poor": "#ef4444"
                }
            )

            fig.update_layout(
                height=310,
                margin=dict(l=5, r=5, t=10, b=10),
                showlegend=True,
                font=dict(color="#0f172a")
            )

            st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)

    with row1_mid:
        st.markdown('<div class="chart-card"><h3>Urban Quality Indicators</h3>', unsafe_allow_html=True)

        indicators = [
            "accessibility_index",
            "comfort_index",
            "safety_index",
            "green_space_index",
            "walkability_index",
            "healthcare_index"
        ]

        labels = ["Accessibility", "Comfort", "Safety", "Green Space", "Walkability", "Healthcare"]

        values = [
            df[col].mean() if col in df.columns else df["quality_of_life_index"].mean()
            for col in indicators
        ]

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=labels,
                y=values,
                mode="lines+markers",
                fill="tozeroy",
                line=dict(color="#2563eb", width=3),
                marker=dict(size=8)
            )
        )

        fig.update_layout(
            height=310,
            margin=dict(l=10, r=10, t=15, b=10),
            plot_bgcolor="white",
            paper_bgcolor="white",
            yaxis=dict(gridcolor="#e5e7eb"),
            font=dict(color="#0f172a")
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)

    with row1_right:
        st.markdown(
            """
            <div class="chart-card">
                <h3>Urban Quality Map</h3>
                <div class="urban-map">
                    <div class="city-grid"></div>

                    <div class="map-dot excellent" style="left:18%; top:22%;"></div>
                    <div class="map-dot good" style="left:42%; top:35%;"></div>
                    <div class="map-dot moderate" style="left:68%; top:28%;"></div>
                    <div class="map-dot poor" style="left:55%; top:62%;"></div>
                    <div class="map-dot excellent" style="left:28%; top:70%;"></div>
                    <div class="map-dot good" style="left:78%; top:75%;"></div>
                    <div class="map-dot moderate" style="left:35%; top:52%;"></div>

                    <div class="map-legend">
                        <b>Quality</b><br>
                        🟢 Excellent<br>
                        🔵 Good<br>
                        🟠 Moderate<br>
                        🔴 Poor
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with row1_side:
        st.markdown(
            """
            <div class="insight-card">
                <h3>AI Insights</h3>

                <div class="insight-item">
                    <div class="insight-icon">📈</div>
                    <div>
                        <b>Quality improving</b>
                        <p>Overall urban quality has improved based on safety and green space indicators.</p>
                    </div>
                </div>

                <div class="insight-item">
                    <div class="insight-icon">🛡️</div>
                    <div>
                        <b>Safety warning</b>
                        <p>Some cities show low safety and high pollution values.</p>
                    </div>
                </div>

                <div class="insight-item">
                    <div class="insight-icon">🏆</div>
                    <div>
                        <b>Top performers</b>
                        <p>High-quality cities show strong comfort, access, and green-space scores.</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    row2_left, row2_mid, row2_right, row2_side = st.columns([1.0, 1.2, 1.2, 0.85])

    with row2_left:
        st.markdown('<div class="chart-card"><h3>AI Prediction Overview</h3>', unsafe_allow_html=True)

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=float(meta.get("classification_accuracy", 0)) * 100,
                title={"text": "Prediction Accuracy"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#2563eb"},
                    "steps": [
                        {"range": [0, 50], "color": "#fee2e2"},
                        {"range": [50, 75], "color": "#fef3c7"},
                        {"range": [75, 100], "color": "#dcfce7"}
                    ]
                }
            )
        )

        fig.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)

    with row2_mid:
        st.markdown('<div class="chart-card"><h3>Pollution Index Trend</h3>', unsafe_allow_html=True)

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        pollution_values = [120, 132, 118, 110, 98, 90]

        fig = px.bar(
            x=months,
            y=pollution_values,
            labels={"x": "Month", "y": "Average AQI"},
            text=pollution_values
        )

        fig.update_traces(marker_color="#7c3aed", textposition="outside")

        fig.update_layout(
            height=260,
            margin=dict(l=10, r=10, t=10, b=10),
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(color="#0f172a")
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)

    with row2_right:
        st.markdown(
            """
            <div class="chart-card">
                <h3>Recent Reports</h3>
                <div class="insight-item">📄 Global Urban Quality Report 2026</div>
                <div class="insight-item">📄 Public Space Assessment Summary</div>
                <div class="insight-item">📄 AI Prediction Analysis Report</div>
                <div class="insight-item">📄 Urban Livability Index Report</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with row2_side:
        st.markdown(
            """
            <div class="action-card">
                <h3>Quick Actions</h3>
                <div class="quick-btn">☁ Upload New Data</div>
                <div class="quick-btn">⚙ Build ML Model</div>
                <div class="quick-btn">📄 Export Report</div>
                <div class="quick-btn">🔗 Share Dashboard</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.markdown("### Dataset Preview")

    show_cols = [
        c for c in [
            "city",
            "country",
            "quality_of_life_index",
            "safety_index",
            "pollution_index",
            "traffic_commute_index",
            "green_space_index",
            "public_space_quality"
        ]
        if c in df.columns
    ]

    st.dataframe(
        df[show_cols].head(10),
        width="stretch",
        hide_index=True
    )

    st.markdown("</div>", unsafe_allow_html=True)