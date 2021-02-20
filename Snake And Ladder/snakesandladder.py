import time
import random
import sys

# just for effects. Adds a delay of 1 second before performing any action
SLEEP_BETWEEN_ACTIONS = 1
MAX_VAL = 100
DICE_FACE = 6

# snake takes you down from 'key' to 'value'
snakes = {8: 4,18: 1,26: 10,39: 5,51: 6,54: 36,56: 1,60: 23,75: 28,83: 45,85: 59,90: 48,92: 25,97: 87,99: 63}

# ladder takes you up from 'key' to 'value'
ladders = {3: 20, 6: 14, 11: 28, 15: 34, 17: 74,22: 37, 38: 59, 49: 67, 57: 76,61: 78,73: 86,81: 98, 88: 91}

player_turn_text = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
]

snake_bite = [
    "boohoo",
    "bummer",
    "snake bite",
    "oh no",
    "dang"
]

ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy"
]

class snakes_and_ladder():

    def __init__(self):
        pass
    
    def Welcome(self):
        msg = """
               Welcome to Snake and Ladder Game.

               Rules:
              1. Initally both the players are at starting position i.e. 0. 
                 Take it in turns to roll the dice. 
                 Move forward the number of spaces shown on the dice.
              2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
              3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
              4. The first player to get to the FINAL position is the winner.
              5. Hit enter to roll the dice.

               """
        print(msg)

       

    def Player_Names(self):
        player1_name = None
        while not player1_name:
            player1_name = input("Please enter a valid name for first player: ").strip()

        player2_name = None
        while not player2_name:
            player2_name = input("Please enter a valid name for second player: ")
        print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
        return player1_name, player2_name


    def Dice_Values(self):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        dice_value = random.randint(1, DICE_FACE)
        print("Its a " + str(dice_value))
        return dice_value

    @classmethod
    def Snake_Bite(cls,old_value, current_value, player_name):
        print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
        print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))

    @classmethod
    def Ladder_Jump(cls,old_value, current_value, player_name):
        print("\n" + random.choice(ladder_jump).upper() + " ########")
        print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


    def snake_ladder(self,player_name, current_value, dice_value):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        old_value = current_value
        current_value = current_value + dice_value
        if current_value > MAX_VAL:
            print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
            return old_value

        print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
        if current_value in snakes:
            final_value = snakes.get(current_value)
            snakes_and_ladder.Snake_Bite(current_value, final_value, player_name)

        elif current_value in ladders:
            final_value = ladders.get(current_value)
            snakes_and_ladder.Ladder_Jump(current_value, final_value, player_name)

        else:
            final_value = current_value

        return final_value


    def check_win(self,player_name, position):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        if MAX_VAL == position:
            print("\n\n\nThats it.\n\n" + player_name + " won the game.")
            print("Congratulations " + player_name)
            print("\nThank you for playing the game.")
            sys.exit(1)



if __name__ == "__main__":
    s1=snakes_and_ladder()
    s1.Welcome()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player1_name, player2_name =s1.Player_Names()
    time.sleep(SLEEP_BETWEEN_ACTIONS)

    player1_current_position = 0
    player2_current_position = 0
    while True:
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = s1.Dice_Values()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(player1_name + " moving....")
        player1_current_position = s1.snake_ladder(player1_name, player1_current_position, dice_value)

        s1.check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = s1.Dice_Values()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(player2_name + " moving....")
        player2_current_position = s1.snake_ladder(player2_name, player2_current_position, dice_value)

        s1.check_win(player2_name, player2_current_position)
    

