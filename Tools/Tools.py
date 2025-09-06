from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PIL import Image
import time
import random
from agents import function_tool
from typing import List, Dict
import requests
import os
from dotenv import load_dotenv
load_dotenv()


# Make tools for Agents
@function_tool
def get_info():
    """
    Collects trip-related information from the user.
    """
    print("Please provide the following information for your trip planning:\n")

    location = input("1. What is your current location? ")
    date = input("2. What is the date of your trip? ")
    trip_type = input("3. What type of location do you want to go to? ")
    budget = input("4. What is your budget? ")
    companions = input("6. Who is accompanying you? (Family/Friends) ")

    print(f"""
Confirm Your Information:

- Current Location: {location}
- Date of Trip: {date}
- Type of Trip: {trip_type}
- Budget: {budget}
- Companions: {companions}

Thank you for providing your trip details!
""")

    # Store the collected information for use by other tools
    return {
        "location": location,
        "date": date,
        "trip_type": trip_type,
        "budget": budget,
        "companions": companions
    }

@function_tool
def get_location_details(location: str, trip_type: str):
    """
    Retrieves information about a specific location, including its features and food options,
    using the Serper.dev API.
    """
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError("SERPER_API_KEY environment variable not set.")

    # Define the search query
    query = f"{trip_type} in {location}"

    # Set up the request headers and payload
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "q": query,
        "gl": "pk",  # Geolocation (Pakistan)
        "hl": "en"   # Language (English)
    }

    # Make the POST request to the Serper.dev API
    response = requests.post("https://google.serper.dev/search", headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        return

    # Parse the JSON response
    results = response.json()

    # Extract and display relevant information
    print("\nTop Search Results:")
    for idx, result in enumerate(results.get("organic", []), start=1):
        title = result.get("title", "No title")
        link = result.get("link", "No link")
        snippet = result.get("snippet", "No snippet")
        print(f"{idx}. {title}\n   {link}\n   {snippet}\n")


@function_tool

def take_map_screenshot(location_name: str):
    search = location_name.replace(" ", "+")
    maps_url = f"https://www.google.com/maps/place/{search}/"

    # Set up browser options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")  # Remove browser UI for full map

    # Launch browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(maps_url)
    
    # Allow map to load
    time.sleep(6)

    # Try to collapse side panel if exists
    try:
        collapse_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Collapse side panel"]')
        collapse_button.click()
        time.sleep(2)
    except:
        pass

    # Screenshot path
    filename = f"{location_name.replace(' ', '_')}_{random.randint(1000,9999)}.png"
    filepath = os.path.join(os.getcwd(), filename)

    # Take screenshot
    driver.save_screenshot(filepath)

    print(f"✅ Screenshot saved: {filepath}")
    print(f"🔗 Maps Link: {maps_url}")

    driver.quit()
    return filepath, maps_url

