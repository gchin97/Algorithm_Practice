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
# n= input()
# num_of_people =sort(input().split)
# # 각 숫자를 문자열로 바꿔주는 것
# result = 0
# for i in range(1, len(data)):
#     num = int(num_of_people[i])
#     if num[i] > num[i+1]:
#  #       select num less than highest one
#         count += 1
#     else:
#         count +=1
#         result = result * num
# print(result)

# 모험가 길드 문제 풀이
# - 오름차순으로 저렬해서 항상 최소한의 모함가의 수만 포함해서 그룹을 결성하면 됨
# n = int(input())  # 3
# data = list(map(int, input().split()))  # 1 2 2
# data = data.sort()
# result = 0  총 그룹 수
# count = 0  그룹에 포함된 모험가의 수

# for i in data:
#     공포도가 낮은 것부터 하나씩 확인
#     count = count + 1 현재 그룹에 해당 모험가를 포함시키기
#     if result >= i:
#         현재 그룹에 포함된 모험가의 수가 공포도 이상이면 그룹 결성
#         result = result + 1 총 그룹의 수 증가시키기
#         count = 0 현재 그룹에 포함된 모험가의 수 초기화
# print(result) 총 그룹의 수 출력

# n = int(input())  # 5
# plans = input().split()  # R R R U D
# x, y = 1, 1

# dx = [0, 0, 1, -1]
# dy = [-1, 1, 0, 0,]
# move_types = ['L', 'R', 'U', 'D']
# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny <1 or nx >x or ny >y
#     x, y = nx, ny
# print(x, y)


# h = int(input())
# count = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k):
#                 count = count+1
# print(count)

# #시뮬레이션 완전탐색 구현 유형
# input_data= input() #a1 -> 2
# row = int(input_data[1])
# column = int(ord(input_data[0]))- int(ord('a')) + 1

# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if next_row >=1 or next_row <=8 or next_column >=1 or next_column <=8:
#         result = result + 1
# print(result)

# #6. 그리디- 시뮬레이션
# data = input()
# result = []
# value = 0

# for x in data:
#     if x.isalpha():
#         result.append(x)
#     else:
#         value = value + int(x)
# result.sort()
# if value != 0:
#     result.append(str(value))

# print(''.join(result))


# # DFS & BFS

# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.popleft()
# print(queue)
# queue.reverse()

# def factorial(n):
#     result = 1
#     for i in range(n+1):
#         result = result * i
#     return result

# #유클리드 호제법
# def gcb(a,b):
#     if a%b == 0:
#         return b
#     else:
#         gcb(a,a%b)

# 가장 인접해 있는 노드에서 가장 숫자가 적은 것을 선택하는 방식  v= starting point
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8]
    [1, 4, 5]
    [3, 5]
    [3, 4]
    [7]
    [2, 6, 8]
    [1, 7]
]
# 방문처리를 위해서 하나의 리스트를 만듦 모든 노드를 하나도 방문하지 않은 것으로 만들어야 함 인덱스 0은 사용하지 않도록 하나 더 큰 크기로 9 만듦
visited = [False] * 9

dfs(graph, 1, visited)
