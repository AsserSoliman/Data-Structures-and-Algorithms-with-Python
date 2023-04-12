# Binary search works only on sorted arrays 

#                 search  insert  delete
# array, unsorted   O(n)    O(1)    O(n)
# array, sorted    O(log n) O(n)    O(n)

# Binary search halves the array each step 


# Using Iteration 

def Binary_search_itr(list,number):
    min = 0
    max = len(list)-1
    
    while min <= max:
        
        mid = (min+max) // 2
        if list[mid] == number :
            return True
        elif list[mid] < number :
            min = mid + 1
        else:
            max = mid - 1
    
    return False

# Recursive

def Binary_search_rec(list,min,max,number):
    mid = (min+max) // 2 
    if min > max :
        return False
    
    if list[mid] == number :
        return True 
    elif list[mid] > number:
        Binary_search_rec(list,min,mid - 1,number)
    else:
        Binary_search_rec(list,mid + 1,max,number)


# Test

x = [1,2,5,7,8,9,12,15,20,25]
if Binary_search_rec(x ,0,len(x)-1, 5):
    print('Yes')
else:
    print('NO')
            
        
    
