# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
largest_integer = max(a)
a.remove(largest_integer)
second_largest_integer = max(a)
result = largest_integer * second_largest_integer
print(result)