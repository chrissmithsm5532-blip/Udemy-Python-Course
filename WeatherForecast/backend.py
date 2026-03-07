import requests

API_KEY = 'f91d1d304950deffbb9e0fdf327c20da'

def get_data(place,forecast_days=None):
    url = (f'http://api.openweathermap.org/data/2.5/forecast?q={place}'
           f'&appid={API_KEY}')
    response = requests.get(url)
    data = response.json()
    sections = 8 * forecast_days
    filtered_data = data["list"]
    filtered_data = filtered_data[:sections]
    return filtered_data

if __name__ == "__main__":
    testdata = get_data(place="London",forecast_days=3)
    print(testdata)
