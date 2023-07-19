import requests

API_KEY="305cc0d3a3f006aae458324af7bfb6a0"
def get_data(location, forecast=None):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    data_list = data["list"]
    nr_values = 8 * forecast
    data_list = data_list[:nr_values]
    return data_list


if __name__=="__main__":
    print(get_data(location="Tokyo",forecast=3))
