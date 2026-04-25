# =============================================================================
# Final Project - Utah Cities Weather Analysis
# Author: Andre Louis
# Description: Fetches current weather data for 10 major Utah cities using
#              the OpenWeatherMap API, stores data in CSV files, and analyzes
#              which city is hottest, coldest, windiest, and most humid.
# =============================================================================

import requests
import csv
import json
import os
from datetime import datetime

# =============================================================================
# CONFIGURATION - a7dd66652a6a867804cf054595e687b1
# =============================================================================
API_KEY = "a7dd66652a6a867804cf054595e687b1"   # 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# The 10 Utah cities we will analyze
UTAH_CITIES = [
    "Salt Lake City",
    "St. George",
    "Provo",
    "Ogden",
    "Cedar City",
    "Moab",
    "Logan",
    "Park City",
    "Vernal",
    "Richfield"
]

# File paths
DATA_FILE = "weather_data.csv"
RESULTS_FILE = "results.json"


# =============================================================================
# STEP 1: FETCH WEATHER DATA FROM API
# =============================================================================

def get_weather(city):
    """
    Calls the OpenWeatherMap API and returns weather data for a single city.
    Returns a dictionary with the data, or None if the call fails.
    """
    # Build the request parameters
    params = {
        "q": city + ",US",       # City name + country code
        "appid": API_KEY,         # Your API key
        "units": "imperial"       # Use Fahrenheit for temperature
    }

    try:
        response = requests.get(BASE_URL, params=params)

        # Check if the request was successful (status code 200 = OK)
        if response.status_code == 200:
            data = response.json()

            # Pull out the specific fields we want
            weather_info = {
                "city": city,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "time": datetime.now().strftime("%H:%M:%S"),
                "temp_f": data["main"]["temp"],
                "feels_like_f": data["main"]["feels_like"],
                "temp_min_f": data["main"]["temp_min"],
                "temp_max_f": data["main"]["temp_max"],
                "humidity_pct": data["main"]["humidity"],
                "wind_speed_mph": data["wind"]["speed"],
                "description": data["weather"][0]["description"]
            }
            return weather_info

        else:
            print(f"  Warning: Could not get data for {city} (Status: {response.status_code})")
            return None

    except Exception as e:
        print(f"  Error fetching data for {city}: {e}")
        return None


def fetch_all_cities():
    """
    Loops through all Utah cities and fetches weather data for each one.
    Returns a list of weather dictionaries.
    """
    print("Fetching weather data from OpenWeatherMap API...")
    all_weather = []

    for city in UTAH_CITIES:
        print(f"  Getting weather for {city}...")
        weather = get_weather(city)
        if weather:
            all_weather.append(weather)

    print(f"  Successfully fetched data for {len(all_weather)} cities.\n")
    return all_weather


# =============================================================================
# STEP 2: SAVE DATA TO CSV FILE (appends new rows, never overwrites old data)
# =============================================================================

def save_to_csv(weather_list):
    """
    Saves weather data to a CSV file.
    - If the file does NOT exist, it creates it with a header row.
    - If the file DOES exist, it APPENDS new rows (old data is kept).
    """
    # Define the column headers
    headers = [
        "city", "date", "time", "temp_f", "feels_like_f",
        "temp_min_f", "temp_max_f", "humidity_pct",
        "wind_speed_mph", "description"
    ]

    # Check if the file already exists to decide whether to write the header
    file_exists = os.path.isfile(DATA_FILE)

    # Open in append mode ("a") so we never overwrite existing data
    with open(DATA_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        # Only write the header if this is a brand new file
        if not file_exists:
            writer.writeheader()
            print(f"Created new file: {DATA_FILE}")

        # Write each city's weather as a new row
        writer.writerows(weather_list)
        print(f"Appended {len(weather_list)} rows to {DATA_FILE}\n")


# =============================================================================
# STEP 3: READ DATA FROM CSV (loads only today's data for analysis)
# =============================================================================

def read_todays_data():
    """
    Reads the CSV file and returns only the most recent 10 rows.
    This ensures analysis is always based on the latest fetch only.
    """
    all_rows = []

    with open(DATA_FILE, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_rows.append(row)

    # Return only the last 10 rows (most recent run)
    return all_rows[-10:]

# =============================================================================
# STEP 4: ANALYZE THE DATA
# =============================================================================

def analyze_weather(weather_list):
    """
    Analyzes the weather data and returns a results dictionary with:
    - Hottest city
    - Coldest city
    - Windiest city
    - Most humid city
    - Average temperature across all cities
    - Average humidity across all cities
    - A summary of all city conditions
    """

    if not weather_list:
        print("No data to analyze!")
        return {}

    # Convert string values from CSV back to numbers for comparison
    for row in weather_list:
        row["temp_f"] = float(row["temp_f"])
        row["humidity_pct"] = float(row["humidity_pct"])
        row["wind_speed_mph"] = float(row["wind_speed_mph"])

    # --- Find the hottest city (highest temperature) ---
    hottest = max(weather_list, key=lambda x: x["temp_f"])

    # --- Find the coldest city (lowest temperature) ---
    coldest = min(weather_list, key=lambda x: x["temp_f"])

    # --- Find the windiest city (highest wind speed) ---
    windiest = max(weather_list, key=lambda x: x["wind_speed_mph"])

    # --- Find the most humid city (highest humidity %) ---
    most_humid = max(weather_list, key=lambda x: x["humidity_pct"])

    # --- Calculate average temperature ---
    avg_temp = sum(row["temp_f"] for row in weather_list) / len(weather_list)

    # --- Calculate average humidity ---
    avg_humidity = sum(row["humidity_pct"] for row in weather_list) / len(weather_list)

    # --- Build a summary list of all cities ---
    city_summary = []
    for row in weather_list:
        city_summary.append({
            "city": row["city"],
            "temp_f": row["temp_f"],
            "humidity_pct": row["humidity_pct"],
            "wind_speed_mph": row["wind_speed_mph"],
            "description": row["description"]
        })

    # --- Package everything into a results dictionary ---
    results = {
        "analysis_date": datetime.now().strftime("%Y-%m-%d"),
        "analysis_time": datetime.now().strftime("%H:%M:%S"),
        "cities_analyzed": len(weather_list),
        "hottest_city": {
            "city": hottest["city"],
            "temp_f": hottest["temp_f"],
            "description": hottest["description"]
        },
        "coldest_city": {
            "city": coldest["city"],
            "temp_f": coldest["temp_f"],
            "description": coldest["description"]
        },
        "windiest_city": {
            "city": windiest["city"],
            "wind_speed_mph": windiest["wind_speed_mph"],
            "description": windiest["description"]
        },
        "most_humid_city": {
            "city": most_humid["city"],
            "humidity_pct": most_humid["humidity_pct"],
            "description": most_humid["description"]
        },
        "averages": {
            "avg_temp_f": round(avg_temp, 2),
            "avg_humidity_pct": round(avg_humidity, 2)
        },
        "all_cities": city_summary
    }

    return results


# =============================================================================
# STEP 5: SAVE RESULTS TO results.json
# =============================================================================

def save_results(results):
    """
    Saves the analysis results to results.json.
    This file is overwritten each time with the latest analysis results.
    """
    with open(RESULTS_FILE, "w") as jsonfile:
        json.dump(results, jsonfile, indent=4)

    print(f"Results saved to {RESULTS_FILE}\n")


# =============================================================================
# STEP 6: PRINT A READABLE SUMMARY TO THE CONSOLE
# =============================================================================

def print_summary(results):
    """
    Prints a clean, readable summary of the analysis results to the console.
    """
    print("=" * 55)
    print("       UTAH CITIES WEATHER ANALYSIS RESULTS")
    print("=" * 55)
    print(f"  Date:             {results['analysis_date']}")
    print(f"  Time:             {results['analysis_time']}")
    print(f"  Cities Analyzed:  {results['cities_analyzed']}")
    print()

    print("  --- KEY FINDINGS ---")
    h = results["hottest_city"]
    print(f"  Hottest City:   {h['city']} at {h['temp_f']}°F ({h['description']})")

    c = results["coldest_city"]
    print(f"  Coldest City:   {c['city']} at {c['temp_f']}°F ({c['description']})")

    w = results["windiest_city"]
    print(f"  Windiest City:  {w['city']} at {w['wind_speed_mph']} mph ({w['description']})")

    m = results["most_humid_city"]
    print(f"  Most Humid:     {m['city']} at {m['humidity_pct']}% humidity ({m['description']})")

    a = results["averages"]
    print()
    print("  --- UTAH AVERAGES ---")
    print(f"  Avg Temperature: {a['avg_temp_f']}°F")
    print(f"  Avg Humidity:    {a['avg_humidity_pct']}%")

    print()
    print("  --- ALL CITIES ---")
    print(f"  {'City':<18} {'Temp (°F)':<12} {'Humidity':<12} {'Wind (mph)':<12} {'Conditions'}")
    print("  " + "-" * 70)
    for city in results["all_cities"]:
        print(f"  {city['city']:<18} {city['temp_f']:<12} {city['humidity_pct']:<12} {city['wind_speed_mph']:<12} {city['description']}")

    print("=" * 55)


# =============================================================================
# MAIN PROGRAM - This runs everything in order
# =============================================================================

def main():
    print("\n" + "=" * 55)
    print("  Utah Cities Weather Analysis - Starting Up")
    print("=" * 55 + "\n")

    # Check if API key has been set
    if API_KEY == "YOUR_API_KEY_HERE":
        print("ERROR: Please replace 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API key.")
        print("Get a free key at: https://openweathermap.org/api")
        return

    # Step 1: Fetch fresh data from the API
    weather_data = fetch_all_cities()

    if not weather_data:
        print("ERROR: No data was fetched. Check your API key and internet connection.")
        return

    # Step 2: Append the new data to our CSV file
    save_to_csv(weather_data)

    # Step 3: Read today's data back from the CSV for analysis
    todays_data = read_todays_data()

    # Step 4: Analyze the data
    print("Running analysis...")
    results = analyze_weather(todays_data)

    # Step 5: Save results to results.json
    save_results(results)

    # Step 6: Print a summary to the console
    print_summary(results)

    print("\nProgram complete! Check weather_data.csv and results.json for full details.\n")


# This ensures main() only runs when you run this file directly
if __name__ == "__main__":
    main()
