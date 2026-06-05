from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad

@curry(2)
def add(x, y):
    return x + y

@curry(2)
def add10(functor):
    return functor.map(lambda x: add(10)(x))

print("Just(5) + 10:", add10(Just(5))) 

