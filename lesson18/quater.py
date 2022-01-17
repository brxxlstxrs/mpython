def quarter(xcoord, ycoord):
    if ycoord > 0:
        if xcoord > 0:
            print('I четверть')
        else:
            print('II четверть')
    else:
        if xcoord < 0:
            print('III четверть')
        else:
            print('IV четверть')
