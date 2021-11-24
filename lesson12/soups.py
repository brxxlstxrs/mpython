s = ('щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански')
print(*tuple(s[i % len(s)] for i in range(int(input()))), sep='\n')
