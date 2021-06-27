# string concatenation (how to put string togather)
# suppose we want to create a string that says "subscribe to____"
#
# youtuber = "Tapu Roy"  # some string variable
#
# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}" .format(youtuber))  # .format method
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("Famous Person: ")


madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}." \
         f"Stay hydrate and {verb2} like you are {famous_person}!"

print(madlib)