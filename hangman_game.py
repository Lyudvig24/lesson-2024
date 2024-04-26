# import random

# def random_words():
#     with open('randomwords.txt','r') as file:
#         words = file.read().split()
#         rand = random.choice(words)
#         return rand


# def hangman_game(maxTries, word):
#     letters = []
#     output = []

#     for _ in word:
#         output.append('*')
    
#     print('initial output', ''.join(output))

#     alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     for i in range(1, maxTries + 1):
#         answer = input("Write Letter from " + ','.join(alphabet) + ' :' ).upper()

#         if answer in alphabet:
#             alphabet.remove(answer)

#         if answer in word:
#             letters.append(answer)
        
#         hasWon = True

#         for k, w in enumerate(word):
#             if w not in letters:
#                 hasWon = False

#             if w == answer:
#                 output[k] = w

#         print('output', ''.join(output))
         
#         if hasWon:
#             print("You Win")
#             break

#         elif i == maxTries:
#             print('You Lose, the word is: ', word)
    

# word = random_words().upper()
# maxTries = 7

# if(len(word) > maxTries):
#     maxTries = len(word) + 1

# hangman_game(maxTries, word)