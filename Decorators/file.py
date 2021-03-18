# fname = input("Enter file name:")
fh = open("romeo.txt")
lst = list()
for line in fh:
    # print(line)
	lineWithoutSpaces = line.rstrip()
    
#     print(lineWithoutSpaces)
#     words = line.split()
#     for word in words:
#         if word not in lst:
#             lst.append(word)
# print(lst)