# UrbanQuality AI: AI-Powered Public Space Quality Assessment System

## Project Overview

UrbanQuality AI is an intelligent urban analytics and decision-support platform designed to assess, monitor, and predict the quality of public spaces using Artificial Intelligence, GIS concepts, and urban quality indicators.

The system helps urban planners, municipalities, researchers, and policymakers evaluate the livability and sustainability of cities by analyzing multiple dimensions of public-space quality, including safety, accessibility, comfort, healthcare, pollution, mobility, and environmental conditions.

The platform combines machine learning, geospatial analysis, and interactive dashboard visualizations to support data-driven urban planning decisions.

---

# Project Objectives

The main objectives of this project are:

* Assess public-space quality using AI models.
* Analyze urban livability indicators.
* Predict quality scores for cities and urban areas.
* Identify high-quality and low-quality urban zones.
* Support smart-city planning initiatives.
* Improve sustainability and urban well-being.
* Provide interactive GIS-based visual analytics.
* Generate reports for decision-makers.

---

# Dataset

## Dataset Used

**World Cities Quality of Life Dataset**

Dataset includes urban indicators such as:

* City
* Country
* Quality of Life Index
* Safety Index
* Healthcare Index
* Climate Index
* Purchasing Power Index
* Cost of Living Index
* Traffic Commute Index
* Pollution Index
* Green Space Index
* Walkability Index
* Accessibility Index
* Comfort Index
* Latitude
* Longitude

---

# AI Tasks

The project performs two major AI tasks:

## 1. Public Space Quality Classification

Predicts:

* Excellent
* Good
* Moderate
* Poor

using urban quality indicators.

### Algorithms

* Random Forest Classifier
* Decision Tree Classifier

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 2. Public Space Quality Score Prediction

Predicts:

Quality of Life Score (0–100)

### Algorithms

* Random Forest Regressor
* Decision Tree Regressor

### Evaluation Metrics

* R² Score
* Mean Absolute Error (MAE)
* Root Mean Square Error (RMSE)

---

# Project Workflow

```text
World Cities Dataset
        │
        ▼
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Missing Value Handling
        │
        ▼
Feature Engineering
        │
        ▼
Quality Class Creation
        │
        ▼
Train/Test Split
        │
        ▼
Machine Learning Models
        │
 ┌──────┴───────┐
 ▼              ▼
Classification  Regression
 ▼              ▼
Model Evaluation
        │
        ▼
Save Best Models
        │
        ▼
Interactive Dashboard
        │
        ▼
Urban Planning Insights
```

---

# Dashboard Modules

## Dashboard

Provides:

* Total Cities
* Countries Covered
* Average Quality Score
* ML Accuracy
* Regression Performance
* Urban Quality Distribution
* Urban Indicator Trends
* Urban Quality Map
* AI Insights
* Recent Reports

---

## Public Space Assessment

Users can enter:

* Safety
* Comfort
* Accessibility
* Pollution
* Green Space
* Healthcare
* Climate
* Walkability

The system predicts:

* Quality Class
* Quality Score
* Confidence Level

---

## Urban Analytics

Provides:

* Histograms
* Indicator Distribution
* Scatter Analysis
* Correlation Matrix
* Urban Trend Analysis

---

## AI Prediction

Scenario-based simulation system.

Allows planners to modify:

* Safety
* Pollution
* Accessibility
* Comfort
* Green Space

and instantly see predicted impacts.

---

## GIS Visualization

Displays:

* City Locations
* Quality Categories
* Spatial Distribution
* Urban Quality Mapping

---

## ML Analytics

Provides:

* Model Comparison
* Accuracy Scores
* R² Scores
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Reports

Export:

* Dataset Reports
* Classification Reports
* Regression Reports
* Planning Summaries

---

# Project Structure

```text
urban_public_space_ai_project
│
├── app
│   ├── assets
│   │   └── style.css
│   │
│   ├── components
│   │   └── data_loader.py
│   │
│   ├── pages
│   │   ├── dashboard.py
│   │   ├── public_space_assessment.py
│   │   ├── urban_analytics.py
│   │   ├── ai_prediction.py
│   │   ├── gis_visualization.py
│   │   ├── ml_analytics.py
│   │   ├── reports.py
│   │   └── about.py
│   │
│   └── app.py
│
├── data
│   ├── raw
│   ├── processed
│   └── reports
│
├── models
│
├── outputs
│
├── src
│   ├── generate_sample_data.py
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── predict.py
│
├── docs
├── notebooks
├── requirements.txt
└── README.md
```

---

# Installation

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

---

# Generate Sample Dataset

```bash
py src/generate_sample_data.py
```

---

# Train Models

```bash
py src/train_model.py
```

---

# Run Dashboard

```bash
py -m streamlit run app/app.py
```

---

# Technologies Used

## Programming

* Python

## Data Processing

* Pandas
* NumPy

## Machine Learning

* Scikit-Learn

## Visualization

* Plotly
* Matplotlib

## Dashboard Development

* Streamlit

## GIS & Urban Analytics

* Spatial Analysis Concepts
* Urban Quality Indicators
* Geospatial Decision Support

---

# Applications

* Smart City Planning
* Public Space Evaluation
* Urban Development
* Sustainable Cities
* Livability Assessment
* Infrastructure Planning
* Environmental Monitoring
* Quality of Life Analysis
* Urban Policy Design
* AI-Based Urban Decision Support

---

# Future Enhancements

* Real GIS Maps using Folium
* Satellite Imagery Integration
* Deep Learning Models
* Smart City Digital Twin
* Urban Growth Forecasting
* Traffic Prediction
* Sustainability Scoring Engine
* Real-Time Sensor Integration
* Urban Heat Island Analysis
* AI Urban Planning Assistant

---

# Author

UrbanQuality AI

AI-Powered Public Space Quality Assessment using Machine Learning and Urban Analytics.
