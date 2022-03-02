import statistics as stss
lst = list(map(int, input().split()))
print(stss.median(lst), stss.mode(lst))
