import requests

API_KEY = "dc8e93233bd017a27a294fc3582b7b48"

def get_data(place,forecast_days=None, kind=None):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__=="__main__":
    print(get_data(place="Tokyo"))
