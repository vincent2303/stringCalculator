import re

def extractDelimeter(string):
    delimeter = ',|\n'
    cuttedString = string
    delimeterMatch = re.search('//(.*)\n', string)
    if delimeterMatch:
        delimeter = delimeterMatch.group(1)
        cuttedString = cuttedString.replace("//{}\n".format(delimeter), '')
    return delimeter, cuttedString

def Add(string):
    if len(string)==0: return 0

    delimeter, cuttedString = extractDelimeter(string)    
    stringNumbers = re.split(delimeter, cuttedString)
    negativeNumbers = []
    total = 0
    for stringNumber in stringNumbers:
        number = int(stringNumber)
        total += number
        if(number<0): negativeNumbers.append(number)

    if len(negativeNumbers) > 0:
        negativeNumberString = map(str, negativeNumbers)
        raise Exception("Sorry, no numbers below zero, found: {}".format(', '.join(negativeNumberString)))

    return total
