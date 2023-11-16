from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import requests
import csv
from io import StringIO

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing) for the FastAPI app
origins = [
    "http://localhost",
    "http://localhost:5172",  # Replace with your React app's URL during development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

lichess_api = "https://lichess.org/api"

@app.get("/top-players", response_model=dict)
def get_top_players():
    try:
        top_players_url = f"{lichess_api}/player/top/50/classical"
        top_players_response = requests.get(top_players_url)
        top_players_data = top_players_response.json().get("users")
        top_player_usernames = [user.get("username") for user in top_players_data]

        return {"top_players": top_player_usernames}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching top players: {e}")

@app.get("/player/{username}/rating-history", response_model=dict)
def get_rating_history(username: str):
    try:
        rating_history_url = f"{lichess_api}/user/{username}/rating-history"
        rating_history_response = requests.get(rating_history_url)
        rating_history_data = rating_history_response.json()

        return {"username": username, "rating_history": rating_history_data}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching rating history for {username}: {e}")

@app.get("/players/rating-history-csv", response_class=Response)
def get_rating_history_csv():
    try:
        top_players_url = f"{lichess_api}/player/top/50/classical"
        top_players_response = requests.get(top_players_url)
        top_players_data = top_players_response.json().get("users")

        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)
        csv_writer.writerow(["Username", "Rating 30 Days Ago", "Rating Today"])

        for user in top_players_data:
            username = user.get("username")
            rating_history_url = f"{lichess_api}/user/{username}/rating-history"
            rating_history_response = requests.get(rating_history_url)
            rating_history_data = rating_history_response.json()

            rating_30_days_ago = (
                rating_history_data[-30].get("rating", "N/A")
                if len(rating_history_data) >= 30
                else "N/A"
            )
            rating_today = rating_history_data[-1].get("rating", "N/A")

            csv_writer.writerow([username, rating_30_days_ago, rating_today])

        response = Response(content=csv_data.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=rating_history.csv"

        return response

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {e}")
