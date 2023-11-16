from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import requests
import csv
from io import StringIO

app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing) settings
origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

lichess_top_players_url = "https://lichess.org/api/player/top/50/classical"
lichess_rating_history_url = "https://lichess.org/api/user/{username}/rating-history"

@app.get("/top-players", response_model=dict)
def get_top_players():
    try:
        # Fetch top 50 classical chess players from Lichess API
        top_players_response = requests.get(lichess_top_players_url)
        top_players_data = top_players_response.json().get("users")
        top_player_usernames = [user.get("username") for user in top_players_data]
        return {"top_players": top_player_usernames}
    except requests.exceptions.RequestException as e:
        # Handle exceptions when fetching top players
        raise HTTPException(status_code=500, detail=f"Error fetching top players: {e}")

@app.get("/player/{username}/rating-history", response_model=dict)
def get_rating_history(username: str):
    try:
        # Fetch 30-day rating history for a specific player from Lichess API
        player_rating_history_url = lichess_rating_history_url.format(username=username)
        rating_history_response = requests.get(player_rating_history_url)
        rating_history_data = rating_history_response.json()
        return {"username": username, "rating_history": rating_history_data}
    except requests.exceptions.RequestException as e:
        # Handle exceptions when fetching rating history for a player
        raise HTTPException(status_code=500, detail=f"Error fetching rating history for {username}: {e}")

@app.get("/players/rating-history-csv", response_class=Response)
def get_rating_history_csv():
    try:
        # Fetch top 50 players and their rating history, then generate a CSV file
        top_players_response = requests.get(lichess_top_players_url)
        top_players_data = top_players_response.json().get("users")
        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)
        csv_writer.writerow(["Username", "Rating 30 Days Ago", "Rating Today"])

        for user in top_players_data:
            username = user.get("username")
            player_rating_history_url = lichess_rating_history_url.format(username=username)
            rating_history_response = requests.get(player_rating_history_url)
            rating_history_data = rating_history_response.json()
            rating_30_days_ago = rating_history_data[-30].get("rating", "N/A") if len(rating_history_data) >= 30 else "N/A"
            rating_today = rating_history_data[-1].get("rating", "N/A")
            csv_writer.writerow([username, rating_30_days_ago, rating_today])

        # Prepare and return a CSV file as a response
        response = Response(content=csv_data.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=rating_history.csv"
        return response

    except requests.exceptions.RequestException as e:
        # Handle exceptions when fetching data for CSV generation
        raise HTTPException(status_code=500, detail=f"Error fetching data: {e}")
