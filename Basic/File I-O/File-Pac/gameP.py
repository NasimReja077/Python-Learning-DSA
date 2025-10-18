# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random

def game():
     print("You are playing the game")
     score = random.randint(1, 70)
     
     # fetch the high score
     with open("hiscore.txt") as f:
          hiscoreStr = f.read()
          if(hiscoreStr != ""):
               hiscoreStr = int(hiscoreStr)
          else:
               hiscoreStr = 0
     print(f"Your socreis {score}")
     if(score > hiscoreStr):
          # write the new high score to file
          with open("hiscore.txt", "w") as f:
               f.write(str(score))
     return score

game()



# The game() function in a program lets a user play a game and returns the score as an integer.
# It reads and updates the high score in 'hiscore.txt' whenever the current score breaks the record.

# import random
# import os

# def game():
#     print("\nYou are playing the game...")
#     score = random.randint(1, 70)
    
#     # Set up the file path
#     file_path = os.path.join(os.path.dirname(__file__), "hiscore.txt")
    
#     try:
#         # Fetch the high score
#         high_score = 0  # Default high score
#         if os.path.exists(file_path):
#             with open(file_path, 'r') as f:
#                 high_score_str = f.read().strip()
#                 if high_score_str:
#                     high_score = int(high_score_str)
        
#         print(f"Your score is: {score}")
#         print(f"Current high score: {high_score}")
        
#         # Update high score if necessary
#         if score > high_score:
#             with open(file_path, 'w') as f:
#                 f.write(str(score))
#             print(f"Congratulations! New high score: {score}")
        
#         return score

#     except ValueError as e:
#         print("Error: High score file contains invalid data")
#         return score
#     except IOError as e:
#         print(f"Error accessing the high score file: {e}")
#         return score
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return score

# # Run the game
# if __name__ == "__main__":
#     final_score = game()
#     print(f"\nGame ended with score: {final_score}")




     

     