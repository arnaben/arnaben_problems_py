n = int(input("Input a number: "))

first_number = 1
second_number = 2
third_number = 3

for i in range (1, n+1):
    if i <= 3:
        print(i)
    
    else:
        new_number = first_number + second_number + third_number
        first_number = second_number
        second_number = third_number
        third_number = new_number
        print(new_number)

