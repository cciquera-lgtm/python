import datetime
import time

#list_of_numbers = [10, 15, 3, 7]
#k = 17

#list_of_numbers = [2,3,4,5]
#k = 5

list_of_numbers = [1,10,20,50]
k = 70

result = 0

def two_pass_method():
    for number in list_of_numbers:
        for next_number in list_of_numbers:
            result = number + next_number
        
            if result == k:
                print("True")
                break
        else:
            continue

        break  

def one_pass_method():
    seen = set()
    for num in list_of_numbers:
        if k - num in seen:
            print("True")
            break
        seen.add(num)

print(datetime.datetime.now())
two_pass_method()
print(datetime.datetime.now())

time.sleep(2)

print(datetime.datetime.now())
one_pass_method()
print(datetime.datetime.now())
