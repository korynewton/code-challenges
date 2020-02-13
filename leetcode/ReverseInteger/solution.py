


def reverse(x):
    #if x = 0, return 0 immediately
    if x == 0:
        return 0
    
    # convert int to list
    int_list = list(str(x))
    
    #check if the first item is '-'
    if int_list[0] == '-':
        int_list.pop(0)
        int_list.reverse()
        int_list.insert(0,'-')
    else:
        int_list.reverse()
    
    reversed_int = int(''.join(int_list))
    
    if reversed_int > 2**31-1 or reversed_int < -2**31-1:
        return 0
    else:
        return reversed_int
            




print(reverse(321))
print(reverse(1534236469))
