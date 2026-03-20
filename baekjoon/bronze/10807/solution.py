# BOJ 10807 - 개수 세기 

a = int(input())
for _ in range(a):
    b = map(int, input().split())

c = int(input())
print(b.count(c))
