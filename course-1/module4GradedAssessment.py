#1 

#The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
def formatAddress(addressString):
    houseNum = 0
    houseStr = []

    addressList = addressString.split()
    for number in addressList:
        if number.isnumeric():
            houseNum = number
        else: 
            houseStr.append(number)
        return "house number {} on street named {}".format(houseNum, " ".join(houseStr))

print(formatAddress("71 Jalan Rizab 1"))

#2 The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?

def highlightWord(sentence, word):
    return(sentence.replace(word, word.upper()))

print(highlightWord("Have a nice day", "nice"))
print(highlightWord("Shhhhh, don't be so loud", "loud"))
print(highlightWord("Automating with Python is fun", "Python"))

#3 Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

jamiesList = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
drewsList = ["Mike", "Carol", "Greg", "Marcia"]

def combineList(list1, list2):
    list1.reverse()
    list2.append(list1)
    return list2
print(combineList(jamiesList, drewsList))

#4 Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively.For example, squares(2, 3) should return [4, 9].


def squares (start, end):
    return [ start*start for start in range(start, end + 1)]

print(squares(2, 3))
print(squares(1, 5))
print(squares(0, 10))

#5 Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

def carListing(carPrice):
    result = "" #empty list
    for carList, carModel in carPrice.items():
        result += "{} cost {} dollars".format(carList, carModel) + "\n"
    return result
print(carListing({"Kia Seoul":19000, "Lamborghini":55000, "Ford Fiesta": 13000, "Toyota Prius": 240000}))

#6 


def combineGuests(guest1, guest2):
    guest2.update(guest1)
    return guest2

rorysGuest = {"Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotee":2, "Terry":1, "Robert":4}
taylorsGuest = {"David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris": 5}

print(combineGuests(rorysGuest, taylorsGuest))

#7

def countLetter(text):
    result = {}
    text = text.lower()

    for letter in text:
        if letter.isalpha():
            count = text.count(letter)
            result[letter] = count

    return result

print(countLetter("AaBbCc"))
print(countLetter("Math is fun! 2 + 2 = 4"))


