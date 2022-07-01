import sys

n = int(sys.stdin.readline())
meeting = []

for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))

for i in meeting:
    print(i)

cnt = 0
end = 0

for s, e in meeting:
    if s >= end:
        end = e
        cnt += 1
print(cnt)