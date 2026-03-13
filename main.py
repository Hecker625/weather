import requests

url = "https://ipinfo.io/json"

response = requests.get(url)

data = response.json()

city = data["city"]
region = data["region"]
country = data["country"]

loc = data["loc"]
lat, lon = loc.split(",")

print (f"Weather for your location in {city}, {region}, {country} ({lat}, {lon})")
print ("--------------------")

# Step 2: ask NOAA what forecast grid this location belongs to
url = f"https://api.weather.gov/points/{lat},{lon}"

response = requests.get(url)

data = response.json()

# Step 3: get the forecast URL from the response
forecast_url = data["properties"]["forecast"]

# Step 4: request the forecast
forecast_response = requests.get(forecast_url)

forecast_data = forecast_response.json()

# Step 5: print the forecast periods
periods = forecast_data["properties"]["periods"]

for period in periods:
    print(period["name"])
    print(period["detailedForecast"])
    print("\n")

while True:
    correct = input("\nIs this the correct location? ").lower()
    if correct.startswith("y"):
        print("Thank you for using the weather app.")
        break

    elif correct.startswith("n"):
        coord = input("Enter the coordinates for your location (If you don't know your coordinites, go to https://latlong.net. Format is eg. 47.620422,-122.349358 ")
        lat,lon = coord.split(",")
        while True:
            try:
                print (f"The weather for the coordinates {lat}, {lon} is:")

                # Step 2: ask NOAA what forecast grid this location belongs to
                url = f"https://api.weather.gov/points/{lat},{lon}"

                response = requests.get(url)

                data = response.json()

                # Step 3: get the forecast URL from the response
                forecast_url = data["properties"]["forecast"]

                # Step 4: request the forecast
                forecast_response = requests.get(forecast_url)

                forecast_data = forecast_response.json()

                # Step 5: print the forecast periods
                periods = forecast_data["properties"]["periods"]

                for period in periods:
                    print(period["name"])
                    print(period["detailedForecast"])
                    print("\n")
                
                break

            except:
                print("Coordinites not recognized. Please enter the coordinates in this format: latitude,longitude")

    else:
        print("Invalid input. Please try again.")
