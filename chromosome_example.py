#generate a list of 30 random chromosomes, with replacement
samples = random.choices(population, k =30)

print(samples)

def dedupe (things: list[int]) -> list[int]:
    """
    Deduplicate things
    This function takes O(N^2) time where N is the length of things.
    1 + N(N+1) + 1 = N^2 + N + 2 -> O(N^2)
    """
    new_things = [] #O(1)
    for element in things: # N times
        if element not in new_things: #O(N)
            new_things.append(element) #O(1)
    return new_things #O(1)
