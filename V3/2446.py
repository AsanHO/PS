import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
n = int(input())+1
for i in range(n-2, -1, -1):
    print("*" * ((n - i)  - 1)+" " * i*2+"*" * ((n - i)  - 1))
for i in range(1,n-1,1):
    print("*" * ((n - i)  - 1)+" " * i*2+"*" * ((n - i)  - 1))
