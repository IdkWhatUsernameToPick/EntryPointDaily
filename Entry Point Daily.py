import requests
from bs4 import BeautifulSoup
import webbrowser

URL = "https://entry-point.fandom.com/wiki/Entry_Point_Wiki"

response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "lxml")

challenge_table = soup.select_one(".content-box-content table.article-table")

if challenge_table:
    mission_info = challenge_table.find("th", colspan="3")
    mission_text = mission_info.get_text(strip=True) if mission_info else "Unknown"

    modifier_row = challenge_table.find_all("th", style="text-align:center;")
    modifiers = [mod.get_text(strip=True) for mod in modifier_row]
    modifiers = [mod for mod in modifiers if mod != mission_text]

    if mission_text == "The Scientist" and modifiers == ["No Suppressors", "Hidden UI", "No Knockouts"]:
        modifiers = ["Fog", "No Suppressors", "Hidden UI"]
    elif mission_text == "The Scientist" and "No Suppressors" in modifiers[:2] and len(modifiers) == 3 and modifiers[2] == "No Knockouts":
        modifiers[2] = "Hidden UI"

    print("\n=== Daily Challenge ===")
    print(f"🎯 Mission: {mission_text}")
    print(f"⚠️ Modifiers: {', '.join(modifiers) if modifiers else 'None'}")
else:
    print("Failed to retrieve the Daily Challenge.")

choice = input("\nDo you want to launch Entry Point in Roblox? (y/n): ").strip().lower()

if choice == "y":
    game_id = 740581508
    roblox_url = f"roblox://placeId={game_id}"
    print("Launching Entry Point...")
    webbrowser.open(roblox_url)
else:
    print("Exiting script.")
