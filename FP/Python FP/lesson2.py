from pymonad.tools import curry

@curry(2)
def concatenate(str1, str2):
    return str1 + str2

concatenateHello = concatenate("Hello, ")

a = concatenateHello("Max")
print(a)

@curry(4)
def concatenateFour(str1, str2, str3, str4):
    return str1 + str2 + str4 + str3

final = concatenateFour("Hello")(", ")("!")
print(final("Vasya"))