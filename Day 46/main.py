import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

from google.auth.transport.requests import Request            # refreshes stale tokens
from google.oauth2.credentials import Credentials             # reads token.json back in
from google_auth_oauthlib.flow import InstalledAppFlow        # the browser dance
from googleapiclient.discovery import build    

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
YOUTUBE_URL = "https://www.googleapis.com/youtube/v3/channels"
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# date = input("What year would you like to travel to ? Type the date in this format YYYY-MM-DD")

DATE = "2006-03-23"
URL = f"https://www.billboard.com/charts/hot-100/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")
# print(soup.title)

list_class = soup.select("li ul li h3")

all_songs = [item.getText(strip=True) for item in list_class]
# print(all_songs)

# --- constants ---
# SCOPES = ["TODO-1: you've seen this exact URL twice in this chat. Write it here."]
CLIENT_SECRETS_FILE = "./Day 46/client_secret.json"   # the file you downloaded in Phase 1
TOKEN_FILE = "./Day 46/token.json"                    # your local cache — never commit this


def authenticate():
    """Returns valid credentials, using the cache if possible."""
    creds = None

    # 1. Do we have a cached token from a previous run?
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # 2. No token, or a dead one → refresh it or do the browser dance
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())   # silent renew — no browser needed
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)   # 0 = "pick any free port"

        # 3. Save it so next run skips the browser entirely
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())

    return creds


# --- the object that "didn't exist" until now ---
creds = authenticate()
youtube = build("youtube", "v3", credentials=creds)

# --- checkpoint: who am I? ---
request = youtube.channels().list(part="snippet", mine=True)
response = request.execute()  # remember the two-step rule — building the request sends NOTHING

# TODO-3: print(response), find where the channel name is buried, then print ONLY that
print(response)