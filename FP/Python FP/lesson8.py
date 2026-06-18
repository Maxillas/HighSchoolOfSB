from functools import reduce

def second_max(lst):
    def reducer(acc, x):
        first, second = acc
        if x > first:
            return (x, first)
        elif x > second:
            return (first, x)
        return acc
    
    result = reduce(reducer, lst, (float('-inf'), float('-inf')))
    return result[1]

