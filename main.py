
def getDouble(word):
  return str(word) + str(word) + str(len(word+word))
print(getDouble("Hello"))
print(getDouble("ABC"))
print(getDouble(""))

print("#string indexing")

name = "Afiq Hafizuddin Bin Zainal"
print(name[0])
print(name[-8])
print(name[8])

def firstAndLast(message):
    if not message:
      return True
    return message[0] == message [-1]

print(firstAndLast("else"))
print(firstAndLast("tree"))
print(firstAndLast(""))
errorMessage = "A kong string with a silly errata"

newMessage = errorMessage[0:2] + "l" + errorMessage[3:]
print(newMessage)

newMessage = "This is new message"
print(newMessage)
newMessage = "This is the second new message"
print(newMessage)

pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("Dogs"))
print(pets.index("s"))
print(pets.index("t"))

print("#creating new string")

def replaceDomain(email, oldDomain, newDomain):
  if "@" + oldDomain in email:
    index = email.index("@" + oldDomain)
    newEmail = email[:index] + "@" + newDomain
    return newEmail
  return email

print(replaceDomain("afiqhafizuddin@gmail.co", "gmail.co", "gmail.com"))
print(replaceDomain("afiq@yaho.mail", "yaho.mail", "yahoo.mail"))

print("Mountains".upper())

answer = "YES"
if answer.lower() == "yes":
  print("User said yes")

print(' yes '.strip())

print("The number of times e occurs in this string is".count("e"))

print("Forest".endswith("st"))
print("Forest".isnumeric())
print("123241241241243".isnumeric())
print(" ".join(["this", "is", "a", 'string', "joined", "by", "a", "space"]))
print("This is another example".split())

def getAcronym(phrase):
  words = phrase.split()
  result = " "
  for word in words:
    result += word[0]
  return result.upper()

print(getAcronym("Universal Serial Bus"))
print(getAcronym("National Disaster Management Agency"))
print(getAcronym("Kementerian Kesihatan Malaysia"))
print(getAcronym("Auto Teller Maachine "))
print(getAcronym("Tenaga Nasional Berhad"))
print(getAcronym("U N I T Enaga Nasional"))


#formatting strings

number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}".format(number=number))


price = 7.5
withTax = price * 1.09
print(price, withTax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, withTax))

def fahrenheitToCelcius(fahr):
  return (fahr-32)*5/9

for fahr in range(0, 250, 10):
  print("{:>3} F | {:>6.2f} C".format(fahr, fahrenheitToCelcius(fahr)))

def convertDistance(miles):
  km = miles * 1.6
  result = "{} miles equals {:.2f} km".format(miles, km)
  return result

print(convertDistance(12))
print(convertDistance(1.5))

weather = "Rainfall"

print(weather[:4])

def nametage(firstName, lastName):
  return("{} .{[0]}".format(firstName, lastName))

print(nametage("Jane", "Smith"))
print(nametage("Afiq Hafizuddin", "Zainal"))

def replaceEnding(sentence, old, new):
  if sentence.endswith(old):
    i = len(old)
    newSentence = sentence[:-i] + new
    return newSentence
  return sentence
print(replaceEnding("abcabc", "abc", "xyz"))
print(replaceEnding("the cats and the cats", "cats", "dogs"))





