
# def select_sort():
#     with open('words.txt', 'r') as word_file:
#         sorted_word = []
#         for line in word_file:
#             words = line.split()
#             for word in words:
#                 if word.isalpha():
#                     sorted_word.append(word)
        
#     for i in range(len(sorted_word)):
#         min_ind = i
#         for j in range(i + 1, len(sorted_word)):
#             if len(sorted_word[j]) < len(sorted_word[min_ind]):
#                 min_ind = j
#         sorted_word[i], sorted_word[min_ind] = sorted_word[min_ind], sorted_word[i]
        
#     return sorted_word

# words = select_sort()
# print(words)

# def bubble_sort():
#     with open('words.txt', 'r') as file:
#         sorted_words = []
#         for line in file:
#             words = line.split()
#             for word in words:
#                 if word.isalpha():
#                     sorted_words.append(word)

    
#     for i in range(len(sorted_words)):
#         for j in range(0, len(sorted_words)-i-1):
#             if len(sorted_words[j]) > len(sorted_words[j+1]):
#                 sorted_words[j], sorted_words[j+1] = sorted_words[j+1], sorted_words[j]

#     return sorted_words

# sorted_words = bubble_sort()
# print(sorted_words)

