#! python3
#Marc Leon
#box printer from automate the boring stuff


'''


****************
*              *
*              *
*              *
*              *
*              *
***************
'''

def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("'Symbol' needs to be a string length of one")
    if (width < 2 )or (height < 2):
        raise Exception("'Width' and 'Height' must be greater or equal to 2")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

box_print('*', 15, 5)


box_print('O', 5, 16)
