from game import Game

game = Game()

game.status()
player_move = input("Enter a move (e.g. NW/SE): ").strip().split("/")
try:
    game.make_move(*player_move)
except Exception:
    print("Invalid move")
forced_move = game.next_tile

while True:

    # Next player's turn
    game.player_turn = (game.player_turn + 1) % 2

    game.status()

    # Validate player's move
    while True:
        player_move = input("Enter a move (e.g. NW/SE): ").strip().split("/")
        if player_move[0] not in forced_move:
            pass
        
        try:
            if game.make_move(*player_move):
                forced_move = game.next_tile
                break
        except Exception:
            print("Invalid move")

    # Check for win
    if game.check_win(game.board[Game.map_tile[player_move[0]]]):
        tick = "X" if game.player_turn == 0 else "O"
        game.win_status[Game.map_tile[player_move[0]]] = tick
        if game.check_win(game.win_status):
            break


game.status()
print(f"Player {game.player_turn + 1} won!!!")
