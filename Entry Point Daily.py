import requests
from bs4 import BeautifulSoup
import webbrowser

URL = "https://entry-point.fandom.com/wiki/Entry_Point_Wiki"

with requests.Session() as session:
    response = session.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)

if response.status_code != 200:
    print("Failed to retrieve the page.")
    exit()

soup = BeautifulSoup(response.text, "lxml")
challenge_table = soup.find("table", class_="article-table")

if not challenge_table:
    print("Failed to retrieve the Daily Challenge.")
    exit()

mission_info = challenge_table.find("th", colspan="3")
mission_text = mission_info.get_text(strip=True) if mission_info else "Unknown"

modifiers = [
    mod.get_text(strip=True)
    for mod in challenge_table.find_all("th", style="text-align:center;")
    if mod.get_text(strip=True) != mission_text
]

# Special case correction
if mission_text == "The Scientist" and modifiers == ["No Suppressors", "Hidden UI", "No Knockouts"]:
    modifiers = ["Fog", "No Suppressors", "Hidden UI"]
elif mission_text == "The Scientist" and "No Suppressors" in modifiers[:2] and len(modifiers) == 3 and modifiers[2] == "No Knockouts":
    modifiers[2] = "Hidden UI"

print("\n=== Daily Challenge ===")
print(f"🎯 Mission: {mission_text}")
print(f"⚠️ Modifiers: {', '.join(modifiers) if modifiers else 'None'}")

if input("\nDo you want to launch Entry Point in Roblox? (y/n): ").strip().lower() == "y":
    webbrowser.open("roblox://placeId=740581508")
    print("Launching Entry Point...")
else:
    print("Exiting script.")
