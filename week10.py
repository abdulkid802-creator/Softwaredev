# for number in range(1, 10):
#     print(number)
#
# for number in range(1, 10, 2):
#     print(number)
#
# for number in range(1, 10, -1):
#     print(number)

# num_employees = 3
# total_pay = 0
#
# for number in range(3):
#     pay = float(input("enter pay for employee: " + str(number+1)+": "))
#     total_pay+= pay
# average = total_pay/num_employees
# print("Total pay €" + str(total_pay))
# print("Average pay €" + str(average))

# sentence = input("Please enter a sentence: ")
# comma_count = 0
#
# for letter in sentence:
#     if letter == ",":
#         comma_count += 1
# print("the number of commas is: ", comma_count)
# print("the length of the sentence is: ", len(sentence))

# sentence = "! !Python! !"
# sentence = sentence.strip("!")
# print(sentence)

# sentence1 = "Pyth!on"
# index_loc = sentence1.index("!")
# new_string = sentence1[:index_loc] + sentence1[index_loc + 1:]
# print(new_string)

# sentence4 = input("Enter sentence: ")
# print(len(sentence4))
# sentence4 = sentence4.strip()
# print(len(sentence4))
# space_count = 0
# counter = 0
#
# while counter < len(sentence4):
#     if sentence4[counter] == " ":
#         space_count += 1
#     counter += 1
# word_count = space_count + 1
# print("Space        ", space_count)
# print("Words        ", word_count)

# sentence4 = input("Enter sentence: ")
# print(len(sentence4))
# sentence4 = sentence4.strip()
# print(len(sentence4))
# space_count = 0
#
# for character in sentence4:
#     if character == " ":
#         space_count += 1
# word_count = space_count + 1
# print("Space        ", space_count)
# print("Words        ", word_count)

# word = input("Enter a word: ")
#
# for letter in word:
#     print(letter)

# max_limit = int(input("Enter the upper limit: "))
#
# for number in range(1,(max_limit + 1), 2):
#     print(number)

# max_limit = int(input("Enter the upper limit: "))
#
# for number in range(1,(max_limit + 1), 2):
#     if (number % 2) != 0:
#         print(number)

# sentence8 = input("Enter sentence: ")
# vowel_count = 0
#
# for character in sentence8:
#     if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
#         vowel_count += 1
# print("Vowels:      ",vowel_count)

# sentence10 = input("Enter sentence: ")
# reversed = ""
#
# for character_loc in range((len(sentence10)-1),-1, -1):
#     reversed += sentence10[character_loc]
# print(reversed)
#
# sentence11 = input("Enter sentence: ")
# reverse = ""
#
# for character in sentence11:
#     reverse = character + reverse
# print(reverse)