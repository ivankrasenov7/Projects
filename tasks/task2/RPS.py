'''
Author:     Ivan Kirov
Date:       16.07.23
Description: Rock, Paper, Scissors Game
Version:     1.0
'''

import random

class RPS:
    """
        Rock Paper Scissors (RPS) object class

        Attributes
        ----------
        player1_file : str
            File that captures the choices of player 1
        player2_file : str
            File that captures the choices of player 2
        player1_choices: list
            List that captures the choices of player 1
        player2_choices: list
            List that captures the choices of player 2

        Methods
        -------
        create_file(filename)
            Create a file with randomised player choices
        verify_file(filename)
            Verify and read the choices from a file
        calculate_results()
            Calculate the RPS GAME results
        write_results_to_file(filename, player1_wins, player2_wins, draws)
            Write the game results to a file
        play()
            Play the RPS GAME

    """


    def __init__(self):
        '''
        A constructor for ROCK PAPER SCISSORS (RPS) CLASS
        Initialised the players' files, create and go through(verify) player choices.
        '''
        self.player1_file = "player1.txt"
        self.player2_file = "player2.txt"
        self.create_file(self.player1_file)
        self.create_file(self.player2_file)
        self.player1_choices = self.veirfy_file(self.player1_file)
        self.player2_choices = self.veirfy_file(self.player2_file)


    def create_file(self, filename):
        '''
        Create a file that randomly selectes the players choices

        :param filename (str): name of the file to be created

        :return:
        NONE
        '''

        choices = ['R', 'P', 'S']
        with open(filename, 'w') as f:
            for _ in range(100):
                choice = random.choice(choices)
                f.write(choice + '\n')


    def veirfy_file(self, filename):
        '''
        Verify and read choices from the files

        :param filename (str): Name of the file to read

        :return:
        - list of the choices raed from the file
        '''

        try:
            with open(filename, 'r') as f:
                choices = [line.strip().upper() for line in f if line.strip().upper() in ['R', 'P', 'S']]
                return choices
        except ValueError:
            return "Not a valid letter or not all letter are uppercase"


    def calculate_results(self):
        '''
        Calculating the game result

        :return:
        -player1_wins (int) - > wins for the first player
        -player2_wins (int) - > wins for the second player
        -draws - > (int) draws between the two players
        '''

        total_games = len(self.player1_choices)
        player1_wins = 0
        player2_wins = 0
        draws = 0

        for i in range(total_games):
            player1_choice = self.player1_choices[i]
            player2_choice = self.player2_choices[i]

            if player1_choice == player2_choice:
                draws += 1
            elif (
                (player1_choice == 'R' and player2_choice == 'S') or
                (player1_choice == 'S' and player2_choice == 'P') or
                (player1_choice == 'P' and player2_choice == 'R')
            ):
                player1_wins += 1
            else:
                player2_wins += 1

        return player1_wins, player2_wins, draws

    def write_results_to_file(self, filename, player1_wins, player2_wins, draws):
        '''
        Committing the result(output) to a final file
        :param filename(str): Name to the file where the results go
        :param player1_wins (int): File that stores the wins of player1
        :param player2_wins (int): File that stores the wins of player2
        :param draws(int): File that stores the draws between two players
        :return:
        None
        '''

        try:
            with open(filename, 'w') as f:
                f.write(20 * "-" + "\n")
                f.write(f"Player1 wins: {player1_wins}\n")
                f.write(f"Player2 wins: {player2_wins}\n")
                f.write(f"Draws: {draws}\n")
                f.write(20 * "-" + "\n")
        except ValueError:
            print("An error occurred while writing the results to file.")

    def play(self):
        if len(self.player1_choices) != 100 or len(self.player2_choices) != 100:
            print("Error: Both players must submit exactly 100 valid choices.")
        else:
            player1_wins, player2_wins, draws = self.calculate_results()
            self.write_results_to_file("result.txt", player1_wins, player2_wins, draws)
            print("Results have been saved to result.txt file.")

if __name__ == '__main__':

    game = RPS()
    game.play()
