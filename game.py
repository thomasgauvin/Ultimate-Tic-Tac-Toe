import numpy as np


class Game:

    map_tile = {
        "NW": 0,
        "N": 1,
        "NE": 2,
        "W": 3,
        "C": 4,
        "E": 5,
        "SW": 6,
        "S": 7,
        "SE": 8,
    }

    def __init__(self):
        self.board = np.array([[str(x) for x in range(9)] for _ in range(9)])
        self.win_status = np.array([None] * 9)
        self.player_turn = 0
        self.next_tile = ", ".join(Game.map_tile.keys())

    def _show_board(self):
        for i in range(3):
            print("-" * 25)
            for j in range(3):
                print(
                    "| "
                    + " ".join(self.board[i * 3][j * 3 : (j * 3) + 3])
                    + " | "
                    + " ".join(self.board[(i * 3) + 1][j * 3 : (j * 3) + 3])
                    + " | "
                    + " ".join(self.board[(i * 3) + 2][j * 3 : (j * 3) + 3])
                    + " |"
                )
        print("-" * 25)

    def status(self):
        print(f"Turn: Player {self.player_turn + 1}\nPossible tile: {self.next_tile}")
        self._show_board()

    def _check_win(player, tile):
        def _win_tile():
            tile[:] = player
            self.win_status = player

        # Horizontal
        for i in range(3):
            if all(player == x for x in tile[i * 3 : (i * 3) + 3]):
                _win_tile()
                return Truer

        # Vertical
        for i in range(3):
            if all(player == x for x in tile[i * 3, (i * 3) + 1, (i * 3) + 2]):
                _win_tile()
                return True

        # Diagonal
        if all(player == x for x in tile[0, 4, 5]) or all(
            player == x for x in tile[2, 4, 6]
        ):
            _win_tile()
            return True

        return False

    def make_move(player, outer_tile, inner_tile):
        self.board[outer_tile][inner_tile] = player

        # Determine next playable outer tile(s)
        if self.win_status[map_tile[inner_tile]] is None:
            self.next_tile = inner_tile
        else:
            self.next_tile = ", ".join(
                [
                    tile
                    for tile in Game.map_tile.keys()
                    if win_status[Game.map_tile[tile]] is None
                ]
            )

        return self.next_tile


game = Game()
game.status()
