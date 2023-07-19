
import streamlit as st
import plotly.express as px
from weather import get_data


st.title("Weather Forecast")
location = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {location}")

if location:
    try:

        data_list = get_data(location, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in data_list]
            dates = [dict["dt_txt"] for dict in data_list]

            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in data_list]
            image_paths = [images[condition] for condition in sky_conditions]
            #print(sky_conditions)
            st.image(image_paths, width=115)
    except KeyError:
        st.write("The place you chose doesn't exist")