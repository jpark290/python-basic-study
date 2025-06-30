name = input("Enter your name: ")

print(name)

print(len(name))  # Length of the string


print(type(int("1234"))) # class int
print(type(str(1234))) # class str

num = [1, 100, -9, 54, -4]

print(max(num))  # Maximum value in the list
print(min(num))  # Minimum value in the list
#숫자 뿐만아니라 `문자열도 가능

num = ["A", "z", "t", "u", "Y"]
       
print(max(num))  # Maximum value in the list
print(min(num))  # Minimum value in the list

num = "asdaTAXH"

print(max(num))  # Maximum value in the string
print(min(num))  # Minimum value in the string

#list를 정렬할 수 있는 함수도 있음
num = [1, 100, -9, 54, -4]
print(sorted(num))  # Sorted list of characters in the string

num = ["A", "z", "t", "u", "Y"]
print(sorted(num))  # Sorted list of characters in the list

print(sorted(num, reverse=True))  # Sorted list of characters in the list in reverse order

range(1, 11) # Range object from 1 to 10
temp = list(range(1, 11))  # Convert range object to a list

print(temp)
# 일일히 리스트로 만들기 어려운 것을, range를 활용해서 만들수 있음