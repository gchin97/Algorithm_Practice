# # n = 4
# # m = 3
# # array = [[0]*m]*n
# # print(array)

# n = int(input())
# data = list(map(int, input().split()))

# data.sort(reverse=True)
# print(data)

# 파이썬은 문자열과 정수형 데이터를 + 수행할 수 없기 때문에 항시 "I am" + str(answer)+ "." 써줘야함

# answer = 7
# # print(f"{answer} thank you ")

# i = 1
# sum = 0

# for i in range(1,10):
#     if i % 2== 0:
#         continue
#     sum+=1
# print(sum)

# score = [90, 85, 77, 29, 95]
# cheated = {2, 4}

# for i in range(5):
#     if i+1 in cheated:
#         continue
#     if score[i] >= 80:
#         print(i+1, "학생 합격입니다")

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i, "X", j, "=", i*j)

# def operator(i, j):
#     add = i+j
#     sub = i-j
#     mul = i*j
#     div = i/j
#     return add, sub, mul, div


# i, j, c, d = operator(3, 7)
# print(i, j, c, d)

# print((lambda a,b= a+b))(3,7))

# array = [('홍길동',5),('진성은',20),('진성연',30)]

# def operator(x):
#     return x[1]


# print(sorted(array, key = operator))
# print(sorted(array, key = lambda x:x[1]))

# 조합: 서로다른 N개에서 r개를 선택하는 것
# {A,B,C} 에서 순서를 고려하지 않고 두개를 뽑는 경우: AB, AC, BC

# from itertools import combinations
# data = ['A', 'B', 'C']
# result = list(combinations(data, 2))
# print(result)

# 중복순열을 구할때는 combinations 가 아닌 product 나 combinations_with_replacement

# n = 1250
# count = 0
# array = [500, 100, 50, 10]
# for coin in array:
#     count = count + n // coin  # 1260원이 됨
#     # 처음으로는
#     n = n % coin  # 260
# print(count)

# 그리디 문제 2
# n, k = map(int, input().split())
# count = 0
# while True:
#     target = (n//k)*k
#     count = count + (n-target)
#     n = target
#     if n < k:
#         break
#     count = count + 1
#     n = n//k

# count = count + (n-1)
# print(count)

# 문자열을 더해서 가장 큰 정수를 만드는 프로그램

# data = input()
# # 각 숫자를 문자열로 바꿔주는 것
# result = int(data[0])
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result = result + num
#     else:
#         result = result * num
# print(result)

# data = input()
# # 각 숫자를 문자열로 바꿔주는 것
# result = int(data[0])
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result = result + num
#     else:
#         result = result * num
# print(result)

# 모험가 공포도
# 5

from collections import deque
n = int(input())
number = list(map(int, input().split()))
for i in number:
    count = 0
    for j in number:
        if abs(number[i]) == abs(number[j]):
            a = number[i]
            b = number[j]
            if a+b == 0:
                count += 1
            else:
                count += 1
    print(count)
print(count)


n = int(input())
array = [500, 100, 50, 10]

price = int(input())
count = 0

for i in array:
    count = count + price//i
    price = price % i


n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    result = result + (n-target)
    n = target
    if n < k:
        break
    result = result+1

result = result + (n-1)
print(Result)

data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result = num + result
    else:
        result = result * num
print(result)

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count = count + 1
    if count = >i:
        result = result + 1
        count = 0
print(result)


for i

n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
x, y = dx, dy

for i in range(h+1):
    for j in range():
        count = count + 1

        int(ord(input[0])) + int(ord('a')) + 1

data = input()
result = []
value = 0

for x in data:
    if x.isapha():
        result.append(x)
    else:
        value = value + int(X)\
            result.sort()
if value != 0:
    result.append(str(value))

print('', join(result))


def bfs(graph, start, visited):
    queue = deque[start]
    visited[start] = True
    while True:
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i):
                    visited[i] = True
                    visited = True


for true visited[i] = True
