users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
def get_twitter(name):
    return name["Jonathan"]["twitter"]

print(get_twitter(users))

# I DID IT!! :D
# my notes for this section:
# I defined a function that would look for the name of Jonathans twitter handle
# I knew my function needed to retrieve a specific string located in the dictionary for "Jonathan"
# the key that I was looking for was "twitter" as the value to that key was my answer
# As the main dictionary was named "users" I had my function call to the users dictionary to look for said key value

# 2. Get Erik's hometown

def get_erikstown(town):
    return town["Erik"]["home_town"]

print(get_erikstown(users))

# I DID IT AGAIN! :D
# Similar process to question 1
# However this time I looked in "Erik" and found the key "home_town" for my function to print

# 3. Get the list of Erik's lottery numbers

def get_erikslottery(numbers):
    return numbers["Erik"]["lottery_numbers"]

print(get_erikslottery(users))

#YAY!!!! :D
# Similar process to both previous questions
# However this time I knew my function would print a list of numbers
# It did :)

# 4. Get the species of Avril's pet Monty

def avrils_petspecies(pet):
    return pet["Avril"]["pets"][0]["species"]

print(avrils_petspecies(users))

# HURRAY!
# Slightly different events here however my function is performing the same task
# in this case my function needed to find a str within a list 
# In order to do this when my function was looking for specific location it needed an added index number
# once it had that index it also still needed a key, "species"
# So it first went to "Avril" and then to "pets" which is a list
# so in order to find the item located in the list it need the index 0 with the corresponding key for the value result.

# 5. Get the smallest of Erik's lottery numbers
# 6. Return an list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary
