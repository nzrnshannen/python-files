numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
wordList = ["Shannen", "Nazareno", "cat", "apple", "Accenture"]

evenNums = [num for num in numbers if num % 2 == 0]
squareNums = [num * num for num in numbers]
uppercaseWords = [word.upper() for word in wordList]
startingLetterA = [word for word in wordList if word[0].lower() == 'a']

def printFunc(list_name, list):
    print(f"{list_name}: ", end=" ")
    for item in list:
        print(item, end= " ")
    print()
        
printFunc("Even numbers", evenNums)
printFunc("Squared Numbers", squareNums)
printFunc("Uppercase Words", uppercaseWords)
printFunc("Words starting with letter 'a'", startingLetterA)
