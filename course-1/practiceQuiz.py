#Week 4

#1 Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

fileNames =["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
#generate newFileNames as a list containing the new fileNames

newFileNames = [files.replace(" .hpp", " .h") if files.endswith(" .hpp") else files for files in fileNames] #using list comprehension; replacing " .hpp" with " .h"

print(newFileNames)

#2 Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

def pigLatin(text): 
    say = " " #assigning string variable
    words = text.split() # splitting the text string
    pigWordsList = [] #assigning empty list

    for word in words: #iterating word over words
        word = word[1:] + word[0] + "ay" #adding the modification
        pigWordsList.append(word) # appending the word in the list
    return " ".join(pigWordsList) # # joining all the word in a single string

print(pigLatin("Hello how are you"))
print(pigLatin("Programming in Python is Fun"))

#3 The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#For example:  

#640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
#755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"

#Fill in the blanks to make the code convert a permission in octal format into a string format.

def octalToString(octal): 
    result = "" #string assignment

    valueLetters = [(4, "r"), (2, "w"), (1, "x")] #list assignment

    for number in [int(digit) for digit in str(octal)]: #iterating the number over the list of the digit in the string
        for value, letters in valueLetters: #iterating value and letters over the sequence
            if number >= value: #checks if the number is greater than or equal to the value 
                result += letters #results = results + letters
                number -= value # number = number - value 
            else:
                result += "-" # result = result + -
    return result

print(octalToString(755))
print(octalToString(644))
print(octalToString(750))
print(octalToString(777))
print(octalToString(655))
print(octalToString(600))

#5 The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

def groupLists(group, users):
    members = ", ".join(users)
    return "{}: {}".format(group, members)

print(groupLists("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
print(groupLists("Engineering", ["Kim", "Jay", "Tom"]))
print(groupLists("Users", "")) 


#6 The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that. 


def guestLists(guests):
    for guest in guests:
        name, age, role = guest
        print("{} is {} years and works as {}".format(name, str(age), role))

guestLists([("Ken", 30, "Chef"), ("Pat", 35, "Lawyer"), ("Amanda", 25, "Engineer")])

