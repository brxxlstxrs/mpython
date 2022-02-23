def glances(*args: str, kindly=None, large=None, order=None):
    indifferent = []
    reproachful = []
    offended = []
    if kindly == None:
        kindly = 'ae' 
    for i in args:
        if kindly not in i:
            if large == None:
                if len(i) <= 7:
                    indifferent.append(i)
        if i.istitle():
            if large != None:
                if len(i) <= large:
                    reproachful.append(i)
            else:
                reproachful.append(i)
    for i in args:
        if i not in indifferent and i not in reproachful:
            offended.append(i)
    if order:
        indifferent = sorted(indifferent, key=order)
        reproachful = sorted(reproachful, key=order)
        offended = sorted(offended, key=order)
    return {'indifferent': indifferent, 'reproachful': reproachful, 'offended': offended}
        
