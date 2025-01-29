import requests
from bs4 import BeautifulSoup
import webbrowser

# URL of the Entry Point Wiki page
URL = "https://entry-point.fandom.com/wiki/Entry_Point_Wiki"

# Send a GET request to the website
response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "lxml")

# Locate the Daily Challenge table
challenge_table = soup.select_one(".content-box-content table.article-table")

if challenge_table:
    # Extract mission name and type (inside the first <th> element of the table)
    mission_info = challenge_table.find("th", colspan="3")
    mission_text = mission_info.get_text(strip=True) if mission_info else "Unknown"

    # Extract all modifier names (inside the second row of <th> elements)
    modifier_row = challenge_table.find_all("th", style="text-align:center;")
    modifiers = [mod.get_text(strip=True) for mod in modifier_row]

    # Remove mission name from modifiers (if it's accidentally included)
    modifiers = [mod for mod in modifiers if mod != mission_text]

    # Display the extracted information
    print("\n=== Daily Challenge ===")
    print(f"🎯 Mission: {mission_text}")
    print(f"⚠️ Modifiers: {', '.join(modifiers) if modifiers else 'None'}")

else:
    print("Failed to retrieve the Daily Challenge.")

# Ask the user if they want to launch Entry Point
choice = input("\nDo you want to launch Entry Point in Roblox? (y/n): ").strip().lower()

if choice == "y":
    game_id = 740581508
    roblox_url = f"roblox://placeId={game_id}"
    print("Launching Entry Point...")
    webbrowser.open(roblox_url)
else:
    print("Exiting script.")
