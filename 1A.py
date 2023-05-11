def final_verd(end_code, iterators_verd, checkers_verd):

    if iterators_verd == 0:
        return [checkers_verd, 3][end_code != 0]
    
    if iterators_verd == 1:
        return checkers_verd
    
    if iterators_verd == 4:
        return [4, 3][end_code != 0]
    
    if iterators_verd == 6:
        return 0
    
    if iterators_verd == 7:
        return 1
    
    return iterators_verd

r, i, c = int(input()), int(input()), int(input())
print(final_verd(r, i, c))