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

  # 그리디 문제 2
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

data = input()
# 각 숫자를 문자열로 바꿔주는 것
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result = result + num
    else:
        result = result * num
print(result)
