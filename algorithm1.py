#write a function to determine if a specific integer is included
#come up with the worst possible case of time complexity
def is_in(things: list[int], query:int) -> bool:
    for thing in things: #N times
        if thing == query: #O(1)
            return True #O(1)
        return False #O(1)
    
# N *(1+1) + 1 -> O(N)
