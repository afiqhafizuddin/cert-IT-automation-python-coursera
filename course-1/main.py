#string modification
def getDouble(word):
  return str(word) + str(word) + str(len(word+word))
print(getDouble("Hello"))
print(getDouble("ABC"))
print(getDouble(""))

#string indexing

name = "Afiq Hafizuddin Bin Zainal"
name = "Afiq Hafizuddin Bin Zainal"
name = "Afiq Hafizuddin Bin Zainal"
print(name[0])
print(name[-8])
print(name[8])

#checks whether the first and last character in a string identical or otherwise
def firstAndLast(message):
    if not message:
      return True
    return message[0] == message [-1]

print(firstAndLast("else"))
print(firstAndLast("tree"))
print(firstAndLast(""))

#editting a string (strign are immutable, slicing is a technique where we can modify a string
errorMessage = "A kong string with a silly errata"

newMessage = errorMessage[0:2] + "l" + errorMessage[3:]
print(newMessage)

#assigning strings to a variable (dynamic assignment)
newMessage = "This is new message"
print(newMessage)
newMessage = "This is the second new message"
print(newMessage)

#checks the index position of a specific character in a string 
pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("Dogs"))
print(pets.index("s"))
print(pets.index("t"))

#creating new string by using indexing method

def replaceDomain(email, oldDomain, newDomain):
  if "@" + oldDomain in email:
    index = email.index("@" + oldDomain)
    newEmail = email[:index] + "@" + newDomain
    return newEmail
  return email

print(replaceDomain("afiqhafizuddin@gmail.co", "gmail.co", "gmail.com"))
print(replaceDomain("afiq@yaho.mail", "yaho.mail", "yahoo.mail"))

#changing all the characters in a string to capital/lower case
print("Mountains".upper())
print("MOUNTAINS".lower())

#modifying replies to a specific format
answer = "YES"
if answer.lower() == "yes":
  print("User said yes")

#strip() function lets you strip the white spaces that there is a string

print(' yes '.strip())
print('YES '.rstrip())
print(' YES'.lstrip())

#counting the occurence of a specific characters in a string
print("The number of times e occurs in this string is".count("e"))

#checking whether a string ended with a substring/characters
print("Forest".endswith("st"))

#checking whether a string contains only a number or not
print("Forest".isnumeric())
print("123241241241243".isnumeric())

#joining a set of of string in a set to be in one string
print(" ".join(["this", "is", "a", 'string', "joined", "by", "a", "space"]))
#splitting a string into a list of substring
print("This is another example".split())

#getting the acronym of a phrase
def getAcronym(phrase):
  words = phrase.split() #spilitting the string into substrings of individual words
  result = " "
  for word in words: #fr loops for iterating the elements over the sequence
    result += word[0] #extracting the character at index 0 in every word
  return result.upper() #return the result and make it uppercase

print(getAcronym("Universal Serial Bus"))
print(getAcronym("National Disaster Management Agency"))
print(getAcronym("Kementerian Kesihatan Malaysia"))
print(getAcronym("Auto Teller Maachine "))
print(getAcronym("Tenaga Nasional Berhad"))
print(getAcronym("U N I T Enaga Nasional"))



#formatting strings
#format() method lets you modify a string but putting a variable postion inside a string and assigned the parameter that corresponds to the variable place/position

number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}".format(number=number))

#formatting a string that contains float number to return float with specific decimal places

price = 7.5
withTax = price * 1.09
print(price, withTax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, withTax))

def fahrenheitToCelcius(fahr):
  return (fahr-32)*5/9

#alligning the output by using the <, > signs to indicate the number of spaces from the left
for fahr in range(0, 250, 10):
  print("{:>3} F | {:>6.2f} C".format(fahr, fahrenheitToCelcius(fahr)))

#converting miles to kilometers and formatting the output to return float with 2 decimal places
def convertDistance(miles):
  km = miles * 1.6
  result = "{} miles equals {:.2f} km".format(miles, km)
  return result

print(convertDistance(12))
print(convertDistance(1.5))
print(convertDistance(23.89))

weather = "Rainfall"
print(weather[:4])

#foramtting the input from responders and giving the format firstName[ ]initialLastName
def nametage(firstName, lastName):
  return("{} .{[0]}".format(firstName, lastName))

print(nametage("Jane", "Smith"))
print(nametage("Afiq Hafizuddin", "Zainal"))


#replacing the ending of a string with a new substring if the length of old substring and the new substring is equal
def replaceEnding(sentence, old, new):
  if sentence.endswith(old):
    i = len(old)
    newSentence = sentence[:-i] + new
    return newSentence
  return sentence
print(replaceEnding("abcabc", "abc", "xyz"))
print(replaceEnding("the cats and the cats", "cats", "dogs"))


#checking the class of the data sequence
x = ["now", "we", "are", "cookign!"]
type(x) 
x = ("we", "are", "cooking!!")
type(x)

#using indexing method to get the elements that sits on the specific index
def getWord(sentence, n):
  if n > 0:
    words = sentence.split(" ") #splitting all the words in the string
    if n <= len(words): #checks if n is within the range of the number of the elements in the sequence
      return(words[n-1]) #returns the elements that in the [n-1] index
    return(" ") # return empty string if n > len(sequence)
    
print(getWord("This is not a drill", 2))

#using .append() fucntion to append the list.
fruits = ["banana", "pineapple", "apple", "watermelon"]
fruits.append("Kiwi") #.append() funtion receives only one parameter and by default return it at the end of the list
fruits.append("Durian")
fruits.append("Rambutan")
fruits.append("Pulasan")

print(fruits)

#inserting an element in a string in the specified index without replacing the prev 
fruits.insert(4, "Orange")
print(fruits)

#removea an element in a string
fruits.remove("Pulasan")
print(fruits)

#remove an element by stating its index
fruits.pop(3)
print(fruits)

#inserting an element by using indexing
fruits[2] = "Strawberry"
print(fruits)

#skipping an element in a list
def skipElements(elements):
  newList = [] #assignign an empty list
  i = 0 #assigning a counter

  for i in range(len(elements)): #i is to be iterated over the length of the list
    if i % 2 == 0: #determining whether it's an even number or not; if yes, execute the  next line
      newList.append(elements[i]) #appending the newList list with the elements
      i += 1 #incremented the i counter
  return newList

print(skipElements(["a", "b", "c", "d", "e", "f", "g", "h", "i"]))

#appending a list
python = ["Python", "is"]
python.append("Great!!")

print(python)

#tuples (sequence of data of any type, and immutable)

def convertSeconds(seconds):
   hours = seconds // 3600
   minutes = (seconds - hours * 3600)//60
   remainingSeconds = seconds - hours * 3600 - minutes * 60
   return hours, minutes, remainingSeconds

result = convertSeconds(5000)
type(result)
print(result)

#unpacking a tuple
hours, minutes, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convertSeconds(6000)
print(hours, minutes, seconds)

hours, minutes, seconds = convertSeconds(1000)
print(hours, minutes, seconds)

#iterating over lists and tuples

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animals in animals: #for the the sequence is to be iterated over the length of the list
  chars += len(animals) #counting the number of the characters; chars = chars + len(animals)
print("Total characters: {}, average length: {:.2f}".format(chars, chars/len(animals)))

#iterates over a list, takes the list/elements as parameter and return it as tuple
winners = ['Ashley', "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))

#enumerate method
def skipElements(elements):
  list = []
  for index, element in enumerate(elements):
    if index % 2 == 0:
      list.append(element)
  return list

print(skipElements(["a", "b", "c", "d", "e", "f", "g"]))
print(skipElements(["Apple", "Orange", "Tembikai", "Lemon", "Rambutan"]))

#formatting inputs in a specific order
def fullEmails(people):
  results = [] #assigning an empty list
  for email, name in people: #for loop for iterating over two parameters in a sequence of data
    results.append("{} <{}>".format(name, email)) #foramtting the output

  return results

print(fullEmails([("afiq@example.com", "Afiq Hafizuddin"), ('shay@example.com', "Shay Brandt")]))

mutliples = []
for x in range(1, 11):
  mutliples.append(x*7)

print(mutliples)

#list comprehension
mutliples = [ x*7 for x in range(0, 101, 10)] #x in the range 0-100 with step size 10 is multplied with 7 for each iterations
print(mutliples)

languages = ["Python", "Perl", "Ruby", "C++", "JavaScript"]
lengths = [len(language) for language in languages] #language is the element; iterated the element over the element itself in the sequence(languages)x
print(lengths)

multipleOf3 = [x for x in range(0, 101) if x % 3 == 0]
print(multipleOf3)


#dictionaries

fileCounts = {"jpg": 10, "txt":14, "csv":2, "py":23}

print(fileCounts)

print(fileCounts["txt"])
print("html" in fileCounts)

# adding element into the dictionary

fileCounts["xlsx"]= 67
print(fileCounts)

fileCounts["xlsx"] = 10
print(fileCounts)

#delete an element from a dictionary

del fileCounts["txt"]
print(fileCounts)






