lst = input().split(';')
print([j for i in lst for j in i.split(',') if int(j) >= 1e9])
