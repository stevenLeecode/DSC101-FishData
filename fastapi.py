import requests
import pandas as pd


#Starter code to test the API
def main():
    try:
        day = "05/02/2025"
        hour = "12 PM"

        #Split string to pass to the API URI
        day = day.split("/")[1]
        hour = hour.split(" ")[0]

        url = f"http://34.171.12.183:8080/live_fish/?day={day}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)

        print(df.head())
        df.to_csv("fish_data.csv", index=False)
    except requests.exceptions.RequestException as e:
        print(f"API is probably offline. Exception:  {e}")

main()