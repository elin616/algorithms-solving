import sys
import heapq

n = int(sys.stdin.readline())
heap = []
#out = []

# 오름차순으로 정렬 , 참고  - https://www.daleseo.com/python-heapq/
for _ in range(n):
    num = int(sys.stdin.readline())
    if num !=0 :
        heapq.heappush(heap,(abs(num),num))
    else : 
        if len(heap)==0:
            print(0)
        else :
            print(heapq.heappop(heap)[1])
    


