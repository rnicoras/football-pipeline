import requests, logging
from ingestion.utils.config import Config
from ingestion.utils.azure_uploader import AzureUpload

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)
BASE_URL = "https://v3.football.api-sports.io"
LEAGUE_ID = 2
SEASON = 2024

def get_headers() -> dict:
    return {
        "x-apisports-key": Config.API_FOOTBALL_KEY
    }

def fetch_standings() -> dict:
    url = f"{BASE_URL}/standings"
    params = {"league": LEAGUE_ID, "season": SEASON}
    res = requests.get(url, headers = get_headers(), params = params)
    res.raise_for_status()
    data = res.json()
    logger.info(f"standings: {len(data.get('response', []))} records")
    return data

def fetch_fixtures() -> dict:
    url = f"{BASE_URL}/fixtures"
    params = {"league": LEAGUE_ID, "season": SEASON}
    res = requests.get(url, headers = get_headers(), params = params)
    res.raise_for_status()
    data = res.json()
    logger.info(f"fixtures: {len(data.get('response', []))} records")
    return data

def fetch_topscorers() -> dict:
    url = f"{BASE_URL}/players/topscorers"
    params = {"league": LEAGUE_ID, "season": SEASON}
    res = requests.get(url, headers = get_headers(), params = params)
    res.raise_for_status()
    data = res.json()
    logger.info(f"top scorers: {len(data.get('response', []))} records")
    return data

def fetch_topassisters() -> dict:
    url = f"{BASE_URL}/players/topassists"
    params = {"league": LEAGUE_ID, "season": SEASON}
    res = requests.get(url, headers = get_headers(), params = params)
    res.raise_for_status()
    data = res.json()
    logger.info(f"top assisters: {len(data.get('response', []))} records")
    return data

def run():
    Config.validate()
    upload = AzureUpload()

    standings = fetch_standings()
    upload.json_to_azure(standings, "api-football", "standings")

    fixtures = fetch_fixtures()
    upload.json_to_azure(fixtures, "api-football", "fixtures")

    topscorers = fetch_topscorers()
    upload.json_to_azure(topscorers, "api-football", "topscorers")

    topassisters = fetch_topassisters()
    upload.json_to_azure(topassisters, "api-football", "topassisters")

if __name__ == "__main__":
    run()