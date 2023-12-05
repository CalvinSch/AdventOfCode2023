import re

doc = open("input.txt","r")
nums_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

sum = 0 #Keep track of total of all calibration values

#Find each line's calibration value
#PART TWO: Need to account for numbers that are spelled out
    #ex:
    #two1nine -> 219 -> 29
for line in doc:
    '''
    #Replace spelled out numbers with integers
    for num, value in nums_dict.items():
        line = line.replace(num,value)
    '''
    #Need to use regex for Positive Lookahead Assertion (?=)
        #ex:
        #xtwone3four -> x2ne34 not xtw134

    #Compile search pattern
    search_pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
    numbers = search_pattern.findall(line) #Store list of saved numbers
    print(numbers)

    for i in range(len(numbers)):
        if numbers[i] in nums_dict:
            numbers[i] = nums_dict[numbers[i]]

    print(numbers)

    '''
    #Find and store each number in the line
    numbers = []
    for i in line:
        if i.isnumeric():
            numbers.append(i)
    '''

    #Calculate line's value by creating a two digit number with first and last number
    sum += (10*int(numbers[0]) + int(numbers[-1]))


print(sum)