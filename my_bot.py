"""
This is the ONLY file you should modify.

(1) Name this file with your teamname:
    Do not include space in the filename.

(2) Send this file at the end of the tryout for submission.

"""

import random
import math

class bot:


    def __init__(self, game):
        self.map_tile = {
            0: "NW",
            1: "N",
            2: "NE",
            3: "W",
            4: "C",
            5: "E",
            6: "SW",
            7: "S",
            8: "SE",
        }
        self.team_name = "Foo"
        self.game = game

    def move(self):
        "Logic for your bot"
        num1 = math.floor(random.random() * 9)
        num2 = math.floor(random.random() * 9)


        # while self.game.board[num1][num2] == "O" or self.game.board[num1][num2] == "X":
        #     num1 = math.floor(random.random() * 9)
        #     num2 = math.floor(random.random() * 9)

        num1, num2 = self.map_tile[num1], self.map_tile[num2]

        return (""+num1+"/"+num2).split("/") #cleancode
