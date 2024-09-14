from fastapi import FastAPI
from player.entities import Game, Player
import uuid

app = FastAPI()

g = Game()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/game")
async def get_game():
    return {"message": "Game is running", "players in game": g.players_in_game, "player_number": g.player_number, "players": [player.name for player in g.players]}

@app.put("/game")
async def configure_game(number_of_players: int):
    g.player_number = number_of_players
    g.show_game_config()
    return {"message": "Game configured"}

@app.post("/game/join")
async def join_game(player_name: str):
    if g.players_in_game >= g.player_number and g.player_number != 0:
        return {"message": "Game is full"}
    else:
        p = Player(player_name)
        p.id = uuid.uuid4()
        g.add_player(p)
        for player in g.players:
            print(player.name)
        return {"message": "Player joined game", "player_id": p.id}




@app.delete("/game/join")
async def leave_game(player_id: str):
    g.remove_player(player_id)
    return {"message": "Player left game, ciao..."}

