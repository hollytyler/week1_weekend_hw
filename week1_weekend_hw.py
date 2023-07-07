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

def get_smallest(number):
    return number["Erik"]["lottery_numbers"][2]

print(get_smallest(users))

# WHOOP WHOOP!!!
# Again similar process to the previous one
# However this time my function returned an integar which was located on a list with the indexx 2 

# 6. Return an list of Avril's lottery numbers that are even

avril_lottery_numbers= users["Avril"]["lottery_numbers"]
even_numbers=[]

for number in avril_lottery_numbers:
    if number % 2 == 0:
      even_numbers.append(number)

print(even_numbers)

#This one was tricky for me! I got really caught up in trying to turn it into a function and couldnt wrap my head around that
# Managed to get the result in the end by assigning two variables with values
# first one being the path for the for and the second one being my print result list.
# the purpose of the empty list is so that once I pull the even list in the for loop it will populate an empty list
# the % is something I needed to google in order to find out how to get the even numbers. the .append is used to the populate the list with multiple numbers

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

def add_number(user, new_number):
    user["lottery_numbers"].append(new_number)

add_number(users["Erik"], int(7))
print(users["Erik"]["lottery_numbers"])

# In this function I needed to append a list in order to add the number 7
# here I define the function with a user and a new number
# in the next line I need to use the function .append to add the new number to the users location ie "Erik"
# in the function call I was not able to use 7 as is so i needed to use int to turn it from a str into and integar
# :)

# 8. Change Erik's hometown to Edinburgh

users["Erik"]["home_town"] = "Edinburgh"

print(users["Erik"])

# :D 
# This one was a simple modification
# List users with keys "Erik" + "home_town" and replacing the original value with "Edinburhg"
# Print check to check the answer

# 9. Add a pet dog to Erik called "fluffy"

users["Erik"]["pets"].append(
    {
      "name": "fluffy",
      "species": "dog"
    },
    )

print(users["Erik"])

# In this question I used the function .append to add a dictionary to the list users and "Erik"
# In the last line I printed to check my answer

# 10. Add another person to the users dictionary

users["holly"] = {
    
    "favourite_day": "friday",
    "favourite_numbers": [7, 13, 4, 28, 11],
    "favourite_town": "Edinburgh",
    "pets": [
    {
      "name": "simba",
      "species": "cat"
    },
    {
      "name": "nala",
      "species": "dog"
    },
    {
      "name": "codie",
      "species": "duck"
    }
  ]
}

print(users)

# SO this one was very simple in that all I need to do is add a dictionary in.
# The syntax for this is dictionary['new_key'] = _________

#Hope my notes are legible and enough infomation :)

# END -----