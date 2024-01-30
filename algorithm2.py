#write a function to de-duplicate. don't use a set or dict
def is_in(things: list[int], query: int) -> bool:
    for thing in things: # N times
        if thing == query: # O(1)
            return True
    return True # O(1)


def dedup(things):
    unique_things = []
    for thing in things:
        if not is_in(unique_things, thing):
            unique_things.append(thing)
    return unique_things