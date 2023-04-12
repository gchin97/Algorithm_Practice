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
- 오름차순으로 저렬해서 항상 최소한의 모함가의 수만 포함해서 그룹을 결성하면 됨
n = int(input())  # 3
data = list(map(int, input().split()))  # 1 2 2
data = data.sort()
result = 0  총 그룹 수
count = 0  그룹에 포함된 모험가의 수

for i in data:
    공포도가 낮은 것부터 하나씩 확인
    count = count + 1 현재 그룹에 해당 모험가를 포함시키기
    if result >= i:
        현재 그룹에 포함된 모험가의 수가 공포도 이상이면 그룹 결성
        result = result + 1 총 그룹의 수 증가시키기
        count = 0 현재 그룹에 포함된 모험가의 수 초기화
print(result) 총 그룹의 수 출력
