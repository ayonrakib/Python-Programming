import itertools

iterTuple = zip([1, 2, 3], ['a', 'b', 'c'])
for pair in iterTuple:
    print(pair)


for number in itertools.count(5,5):
    if number == 15:
        break
    print(number)

count = 0
for character in itertools.cycle("Ayon"):
    count += 1
    print(character,end=" ")
    if count == 6:
        break