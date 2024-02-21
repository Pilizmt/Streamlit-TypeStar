# Application interface with Streamlit
import os
import joblib
# pylint: disable=E0401
import streamlit as st

# Load the previously trained model
model_path = os.path.join("models", "RandomForestClass_100_71")
model = joblib.load(model_path)


def main():
    st.title("Star type prediction")

    # Introductory message
    st.write("Welcome. Please enter the following data to predict the type of star.")
    # User input
    temperature = st.slider(
        "Temperature (K)",
        min_value=2000,
        max_value=40000,
        value=15000)

    luminosity = st.slider(
        "Luminosity (L/Lo)",
        min_value=0.00001,
        max_value=100000.0,
        value=1.0)

    radius = st.slider(
        "Radio (R/Ro)",
        min_value=0.01,
        max_value=100.0,
        value=1.0)

    absolute_magnitude = st.slider(
        "Absolute Magnitude (Mv)",
        min_value=-10,
        max_value=20,
        value=10)

    # Create a button for prediction
    if st.button("Predict"):
        # Call a function to perform prediction
        prediction_result = perform_prediction(temperature, luminosity, radius, absolute_magnitude, model)
        
        # Display the prediction result
        st.success(f"Type of star: {prediction_result}")

    # Create a dictionary with the user's entries
    user_input = {
        "temperature": temperature,
        "luminosity": luminosity,
        "radius": radius,
        "absolute_magnitude": absolute_magnitude
    }

    # Display the dictionary in the application
    st.write("User input:", user_input)

def perform_prediction(temperature, luminosity, radius, absolute_magnitude, model):
    input_data = [[temperature, luminosity, radius, absolute_magnitude]]

    # Make prediction using the model
    prediction = model.predict(input_data)[0]

    # Map the numerical result to labels
    star_types = {
        0: "Brown Dwarf",
        1: "Red Dwarf",
        2: "White Dwarf",
        3: "Main Sequence",
        4: "Supergiant",
        5: "Hypergiant"
    }

    # Returns the type and description corresponding to the predicted star type
    return star_types.get(prediction)

if __name__ == "__main__":
    main()

