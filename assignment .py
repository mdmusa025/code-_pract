def merge_alternately(list1, list2):
    merged_list = [] 
    for i in range(len(list1)):  
        merged_list.append(list1[i])  
        merged_list.append(list2[i])  
    return merged_list  


list1 = ['a', 'b','c', 'd']
list2 = [2, 4, 6, 8]

print(merge_alternately (list1,list2))

# number=(1,2,3,5,6,7,8....n)

# for i in the range (1)


ans=list1+list2
# print(ans)

# this is for missing number

def find_missing_number(numbers):
    n = len(numbers) + 1  
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(numbers) 
    missing_number = expected_sum - actual_sum  
    return missing_number


numbers = [1, 2, 4, 5]  
print("Missing Number:", find_missing_number(numbers))

user_name={}
user_name['name']=input("enter the your nmae:")
user_name['age']=int(input("enter the age:"))
user_name['height']=float(input("enter the height:"))
user_name['student']=input("are you student yes/no")

print(user_name)

x = 5
y = x
x = 10
print(y)

a = "5"
b = 2
print(a * b)
a = 10
b = 20
if a > b:
    print(a)
else:
    print(b)