import requests

API_KEY = 'f91d1d304950deffbb9e0fdf327c20da'

def get_data(place,forecast_days=None,type=None):
    url = (f'http://api.openweathermap.org/data/2.5/forecast?q={place}'
           f'&appid={API_KEY}')
    response = requests.get(url)
    data = response.json()
    sections = 8 * forecast_days
    filtered_data = data["list"]
    filtered_data = filtered_data[:sections]
    if type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
        return filtered_data
    if type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
        return filtered_data


    return data

if __name__ == "__main__":
    testdata = get_data(place="London",forecast_days=3,type="Temperature")
    print(testdata)
