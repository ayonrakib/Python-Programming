import re

# all of these are case sensitive. newline at last
text = """It is raining in 10 Spain, heavily raining_-+=!@#$%^&*()?/.,';\][]    
"""
foundWords = re.search("^It.*Spain$", text)

# print(foundWords)
# print(type(foundWords))

# findall returns a list with matched characters/strings. if none, returns []

# sob gula te r hobe. regular expression e r boshe.

print("all characters between a and m: ",re.findall("[a-m]", text))

print("all digit: ",re.findall("\d", text))

print("Find sequence which starts with It and then 2 char and then is:",re.findall("It.is", text))

print("start with It:",re.findall("^It",text))

print("end with Spain:",re.findall("Spain$",text))

print("repeat ai:",re.findall("ai*",text))

print("ai followed by characters:",re.findall("ai+",text))

print("a followed by i happening 2 times:",re.findall("ai{1}",text))

print("either spain or rain:",re.findall("rain|spain",text))

print("if the entire string start with It:",re.findall("\AIt",text))

print("If a word starts with rai: ",re.findall(r"\brai", text))

print("If a word ends with ing: ",re.findall(r"ing\b", text))

print("If a word contains ain but not at the beginning: ",re.findall(r"\Bain", text))

print("If a word contains ain but not at the end: ",re.findall(r"ain\B", text))

print("All non digits: ",re.findall("\D", text))

print("All white space characters: ",re.findall("\s", text))

print("All non white space characters: ",re.findall("\S", text))

print("match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character: ",re.findall(r"\w", text))

# ^ whats the point of this

print("match at every non word character - all characters except above mentioned ",re.findall("\W", text))

# ^ whats the point of this

print("Chekc if string ends with \n: ",re.findall("\\nZ", text))

# ^ doesnt work. use \n$ instead that works

print("string contains a i n: ",re.findall("[ain]", text)) 

print("string contains characters between a and n: ",re.findall("[a-n]", text)) 

print("string contains a i n: ",re.findall("[ain]", text)) 

print("string contains anything except a i n: ",re.findall("[^ain]", text)) 

print("string contains 0 1 2: ",re.findall("[012]", text)) 

print("string contains between 0 and 2: ",re.findall("[0-2]", text)) 

print("string contains between 00 and 25: ",re.findall("[0-2][0-5]", text))

# ^ contains as a whole string. 1st elements of list consist 0 0 so make 00, 2nd elements of list 2 5, so 25

print("string contains between a-z and A-Z: ",re.findall("[a-zA-Z]", text)) 

print("string contains + = -: ",re.findall("[+=-]", text)) 

x = re.search("\s", text)

print("Type of \s for re.search: ", type(x))

print("value of \s for re.search: ", x)

print("The first white-space character is located in position:", x.start())

print("split at each white space character: ",re.split("\s", text))

print("split at 1st white space character: ",re.split("\s", text, 1))

print("replace all white space with 6: ",re.sub("\s", "9", text))

print("replace first 2 white space with 6: ",re.sub("\s", "9", text, 2))

# ^ 2nd parameter string hobe, 4th ta hobe first koyta replace korbe. -ve hobe na.

print("replace all white space with 6: ",re.sub("\s", "9", text))

# Search for an upper case "S" character in the beginning of a word, and print its position:

x = re.search(r"\bS\w+", text)
print("Type of return value of search method: ",type(x))
print("value of x: ", x)
print("span, returns a tuple: ",x.span())

# The string property returns the search string
x = re.search(r"\bS\w+", text)
print("Entire string:",x.string)

# looks for any words that starts with an upper case "S": only prints as string
print("looks for any words that starts with an upper case S: ",x.group())