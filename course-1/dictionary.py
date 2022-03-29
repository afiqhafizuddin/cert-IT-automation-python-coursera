
tableOfContent = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3": 25, "Chapter 4":30 }

tableOfContent["Epilogue"] = 39 
tableOfContent["Chapter 3"] = 25
print(tableOfContent)
print("Chapter 5" in tableOfContent)

#iterating over the contents of a dictionary
fileCount = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in fileCount:
    print(extension)

for ext, amount in fileCount.items():
    print("There are {} files with the .{} extension".format(amount, ext))

print(fileCount.keys())
print(fileCount.values())
for value in fileCount.values():
    print(value)
    
#exercise

coolBeast = {"Octopus":"tentacles", "dolphins":"fins", "rhinocerus":"horn"}
for animal, features in coolBeast.items():
    print("{} have {}".format(animal, features))


#example of iterating over dictionary
def countLetter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(countLetter("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(countLetter("a long sentence with a long list of letters hahahahahahahhhahahahahhahahahaha"))

#exercise

wardrobe = {"shirt":["red", "blue", "yellow"], "jeans": ["blue", "black", "red"]}
for cloth, colour in wardrobe.items():
    for colour in colour:
        print("{} {}".format(colour, cloth))

#dictionary methods
print(wardrobe.get("shirt", "Not Present"))
print(wardrobe.keys())
print(wardrobe.values())
print(wardrobe.update(coolBeast))
print(wardrobe)
wardrobe.update(tableOfContent)
print(wardrobe)

#practice quiz

#1
def emailList(domains):
    emails = [] #creating an empty list
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" +domain)
    return emails
    
print(emailList({'gmail.com': ["clarkkent", "lanalang", "dianaprice", "peterparker"], "yahoo.com": ["donald.trump", "joebiden", "najibrazak"]}))

#2 
def groupPerUsers(groupDictionary):
    userGroups = {}

    for groupUsers, users in groupDictionary.items():
        for user in users:
            if user in userGroups:
                userGroups[user].append(groupUsers)
            else:
                userGroups[user] = [groupUsers]
    return(userGroups)
print(groupPerUsers({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


#3
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

#5 
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

def addPrice(basket):
    total = 0
    for groeceries, prices in basket.items():
        total += prices
    return round(total, 2)

print(addPrice(groceries    ))

