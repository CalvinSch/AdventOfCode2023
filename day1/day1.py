doc = open("input.txt","r")

sum = 0 #Keep track of total of all calibration values

#Find each line's calibration value
for line in doc:
    #Find and store each number in the line
    numbers = []
    for i in line:
        if i.isnumeric():
            numbers.append(i)
    
    #Calculate line's value by creating a two digit number with first and last number
    sum += (10*int(numbers[0]) + int(numbers[-1]))

print(sum)