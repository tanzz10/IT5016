# def function2(word1,word2):
#     len1 = len(word1)
#     len2 = len(word2)
#     shorter_length = min(len1,len2)
#     return shorter_length

# word1 = input("Enter word1:")
# word2 = input("Enter word2:")
# print(function2(word1,word2))


def function2(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    shorter_length = min(len1, len2)
    return shorter_length

word1 = input("Enter word1:")
word2 = input("Enter word2:")
print(function2(word1,word2))