def move(position:tuple[int,int], direction:str)->tuple[int,int]:
    x, y = position
    if direction == "north":
        return (0,1)
    if direction == "south":
        return (0,-1)
    if direction == "east":
        return (1,0)
    if direction == "west":
        return (-1,0)
    else:
        raise BadMoveError("Bad move!")
    
class BadMoveError(ValueError):
    pass