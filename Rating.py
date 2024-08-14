import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
st.image(r"th (1).jpeg")
model = pickle.load(open(r"sv.pkl","rb"))

import streamlit as st

# Title of the app
st.title("Predicting Sustainability Ratings Based on Lifestyle Factors")




# Load the data

df = pd.read_csv(r"C:\Users\laxmi\Rating2.csv")  # Use 'xlrd' for .xls files



X = df.drop(["Rating", "Unnamed: 0"], axis=1)
y = df["Rating"]

    # Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=23)

    # Define input features    
   

text1 = {1:"Urban", 2:"Suburban",3:"Rural"}

Location = st.selectbox("Choose the Location", text1.keys())
st.markdown(f"<h4 style='font-size:20px;'>Location: {text1[Location]}</h4>", unsafe_allow_html=True)

text2 = {1:"Often",2:"Sometimes",3:"Rarely",4:"Always"}
LocalFoodFrequency = st.selectbox("Choose the LocalFoodFrequency", text2.keys())
st.markdown(f"<h4 style='font-size:20px;'>LocalFoodFrequency: {text2[LocalFoodFrequency]}</h4>", unsafe_allow_html=True)
#st.write(text2.values())

text3 = {1:"Renewable", 2:"Mixed", 3:"Non-Renewable"}
EnergySource = st.selectbox("Choose the EnergySource", text3.keys())
st.markdown(f"<h4 style='font-size:20px;'> EnergySource Type: {text3[EnergySource]}</h4>", unsafe_allow_html=True)

text4 = {1:"Apartment", 2:"House", 3:"Other"}
HomeType = st.selectbox("Choose the HomeType", text4.keys())
st.markdown(f"<h4 style='font-size:20px;'> Home Type: {text3[HomeType]}</h4>", unsafe_allow_html=True)



text5 = {1:"Rarely", 2:"Sometimes",3:"Often",4:"Always"}
ClothingFrequency = st.selectbox("Choose the ClothingFrequency", text5.keys())
st.markdown(f"<h4 style='font-size:20px;'>ClothingFrequency Type: {text5[ClothingFrequency]}</h4>", unsafe_allow_html=True)

text6 = {5:"High",3:"Moderate",1:"Low"}
CommunityInvolvement = st.selectbox("Choose the Community Involvement Level", text6.keys())
st.markdown(f"<h4 style='font-size:20px;'> Community Involvemente: {text6[CommunityInvolvement]}</h4>", unsafe_allow_html=True)

#EnvironmentalAwareness = st.slider("Environmental Awareness", min_value=1, max_value=5, value=3)
#MonthlyElectricityConsumption = st.slider("Monthly Electricity Consumption", min_value=0, max_value=1000, value=200)
text7 = {1:"Rarely",2: "Sometimes",3: "Often", 4:"Never"}
UsingPlasticProducts = st.selectbox("choose the usingplasticproducts",text7.keys())
st.markdown(f"<h4 style ='font-size:20px;'>UsingPlasticProducts:{text7[UsingPlasticProducts]}</h4>",unsafe_allow_html= True)

text8 = {1:"Composting",2: "Recycling",3: "Landfill",4: "Combination"}
DisposalMethods = st.selectbox("choose the DisposalMethods",text8.keys())
st.markdown(f"<h4 style = 'font-size:20px;'>DisposalMethods:{text8[DisposalMethods]}</h4>",unsafe_allow_html= True)
    
text9 = {1:"High", 2:"Moderate",3: "Low"}
PhysicalActivities = st.selectbox("choose the PhysicalActivities",text9.keys())
st.markdown(f"<h4 style='font-size:20px;'>PhysicalActivities:{text9[PhysicalActivities]}</h4>",unsafe_allow_html= True)

text10 = {1:"Bike",2: "Public Transit",3: "Car", 4:"Walk"}
TransportationMode = st.selectbox("choose the TransportationMode",text10.keys())
st.markdown(f"<h4 style ='font-size:20px;'> TransportationMode:{text10[TransportationMode]}</h4>",unsafe_allow_html= True)

#features = np.array([[Location,LocalFoodFrequency,EnergySource,HomeType,ClothingFrequency,CommunityInvolvement,UsingPlasticProducts,DisposalMethods,PhysicalActivities]])#,additional_feature]])
#model = sv()
#model.fit(X_train, y_train)



features = [Location,LocalFoodFrequency,EnergySource,HomeType,ClothingFrequency,CommunityInvolvement,UsingPlasticProducts,DisposalMethods,PhysicalActivities,TransportationMode]


# Convert features to a numpy array and reshape to 2D
features = np.array(features).reshape(1, -1)

# Button to trigger prediction
if st.button("Submit"):
    try:
        # Predict the rating
        rating = model.predict(features)[0]

        # Classify the rating
        if 4 <= rating <= 5:
            classification = "High"
        elif 2.5 <= rating < 4:
            classification = "Average"
        else:
            classification = "Low"

        # Display the result
        st.write(f"Predicted Rating: {rating:.2f}")

        # Generate star rating
        full_stars = int(rating)  # Number of full stars
        half_star = int(rating % 1 >= 0.5)  # Check if half star is needed
        empty_stars = 5 - full_stars - half_star  # Number of empty stars

        star_rating = '⭐' * full_stars + ('½' if half_star else '') + '☆' * empty_stars

        st.markdown(f"Star Rating: {star_rating}")

        # Display classification
        if classification == "High":
            st.write("This rating is considered High.")
        elif classification == "Average":
            st.write("This rating is Average.")
        else:
            st.write("This rating is Low.")

    except Exception as e:
        st.write(f"Error during prediction: {e}")
