import streamlit as st
import pickle
import numpy as np
import plotly.express as px
import pandas as pd

# Load model, encoders, and scaler
model = pickle.load(open('health_risk_predictor.pkl', 'rb'))
encoders = pickle.load(open('label_encoders.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.set_page_config(page_title="Health Risk Predictor", page_icon="🏥", layout="centered")
st.title("🏥 Health Risk Predictor")
st.markdown("### Enter your health details to predict your health risk level")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Personal Information")
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0, format="%.1f")
    exercise_days = st.slider("Exercise Days per Week", min_value=0, max_value=7, value=3)
    sleep_hours = st.slider("Average Sleep Hours per Night", min_value=1, max_value=12, value=7)

with col2:
    st.subheader("Lifestyle Factors")
    diet = st.selectbox("Diet Type", options=["Average", "Good", "Poor"])
    smoking = st.selectbox("Smoking Status", options=["No", "Yes"])
    alcohol = st.selectbox("Alcohol Consumption", options=["High", "Low", "Medium"])
    stress = st.selectbox("Stress Level", options=["High", "Low", "Medium"])
    family_history = st.selectbox("Family History of Disease", options=["No", "Yes"])

# Prediction
if st.button("🔍 Predict Health Risk", type="primary"):
    try:
        # Scale the numerical features
        scaled_features = scaler.transform([[age, exercise_days, sleep_hours, bmi]])[0]
        
        # Encode categorical features
        diet_encoded = encoders["diet"].transform([diet])[0]
        stress_encoded = encoders["stress"].transform([stress])[0]
        
        # Create dummy variables for alcohol (only Low and Medium, High = [0,0])
        alcohol_low = 1 if alcohol == "Low" else 0
        alcohol_medium = 1 if alcohol == "Medium" else 0
        
        # Create dummy variables for other categorical features
        smoking_yes = 1 if smoking == "Yes" else 0
        family_history_yes = 1 if family_history == "Yes" else 0
        
        # Prepare model input with exact 10 features as expected by the model
        model_input = [
            scaled_features[0],    # age (scaled)
            scaled_features[1],    # exercise_days (scaled)
            scaled_features[2],    # sleep_hours (scaled)
            scaled_features[3],    # bmi (scaled)
            diet_encoded,          # diet (encoded)
            stress_encoded,        # stress (encoded)
            smoking_yes,           # smoking_Yes
            alcohol_low,           # alcohol_Low
            alcohol_medium,        # alcohol_Medium
            family_history_yes     # family_history_Yes
        ]
        
        # Make prediction
        pred = model.predict([model_input])[0]
        risk_label = encoders["risk_level"].inverse_transform([pred])[0]
        
        # Display results
        st.success("Prediction Complete!")
        
        # Color code the risk levels
        if risk_label == "Low":
            st.markdown(f"## 🟢 Risk Level: **{risk_label}**")
            st.info("Great! You have a low health risk. Keep up the healthy lifestyle!")
        elif risk_label == "Medium":
            st.markdown(f"## 🟡 Risk Level: **{risk_label}**")
            st.warning("You have a medium health risk. Consider improving some lifestyle factors.")
        else:  # High
            st.markdown(f"## 🔴 Risk Level: **{risk_label}**")
            st.error("You have a high health risk. Please consider consulting a healthcare professional.")
        
        # Create a more informative visualization
        risk_levels = ["Low", "Medium", "High"]
        colors = ["green", "orange", "red"]
        values = [1 if risk_label == level else 0.1 for level in risk_levels]
        
        fig = px.bar(
            x=risk_levels, 
            y=values, 
            title="Health Risk Assessment",
            color=risk_levels,
            color_discrete_map={"Low": "green", "Medium": "orange", "High": "red"}
        )
        fig.update_layout(
            xaxis_title="Risk Level",
            yaxis_title="Prediction Score",
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Show input summary
        st.subheader("Input Summary")
        input_data = {
            "Feature": ["Age", "BMI", "Exercise Days/Week", "Sleep Hours/Night", "Diet", "Smoking", "Alcohol", "Stress", "Family History"],
            "Value": [age, bmi, exercise_days, sleep_hours, diet, smoking, alcohol, stress, family_history]
        }
        df = pd.DataFrame(input_data)
        st.dataframe(df, use_container_width=True)
        
    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")
        st.info("Please check your inputs and try again.")

# Add some health tips
st.markdown("---")
st.subheader("💡 Health Tips")
st.markdown("""
- **Exercise regularly**: Aim for at least 150 minutes of moderate exercise per week
- **Maintain healthy BMI**: Keep your BMI between 18.5 and 24.9
- **Get enough sleep**: Adults need 7-9 hours of sleep per night
- **Eat a balanced diet**: Include fruits, vegetables, and whole grains
- **Manage stress**: Practice relaxation techniques like meditation
- **Avoid smoking**: Smoking significantly increases health risks
- **Limit alcohol**: Moderate consumption is key
""")

st.markdown("---")
st.caption("⚠️ This tool is for educational purposes only and should not replace professional medical advice.")