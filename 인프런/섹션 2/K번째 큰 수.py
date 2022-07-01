import sys

n, k = map(int, sys.stdin.readline().split())
llist = list(map(int, sys.stdin.readline().split()))
set_llist = set()      # set은 중복을 제거하는 자료구조

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            set_llist.add(llist[i]+llist[j]+llist[m])       # set 자료구조는 appand가 아니라 add로 써야한다.

set_llist = list(set_llist)     # set 자료구조는 sort 개념이 없다. 그래서 다시 list화
set_llist.sort(reverse=True)
print(set_llist[k-1])