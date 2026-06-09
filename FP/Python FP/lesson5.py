from pymonad.maybe import Maybe, Just, Nothing

def to_left(num):
    def inner(pole):
        l, r = pole
        if abs((l + num) - r) > 4:
            return Nothing
        else:
            return Just((l + num, r))
    return inner

def to_right(num):
    def inner(pole):
        l, r = pole
        if abs((r + num) - l) > 4:
            return Nothing
        else:
            return Just((l, r + num))
    return inner

def banana(x):
    return Nothing

def show(maybe):
    if maybe.is_nothing():
        print("Упал")
    else:
        print("Устоял", maybe.value)

begin = lambda: Just((0, 0))

show(
    begin()
    .bind(to_left(2))
    .bind(to_right(5))
    .bind(to_left(-2)) 
)