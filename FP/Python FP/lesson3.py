from pymonad.tools import curry
from pymonad.reader import Compose


@curry(2)
def tag(str1, str2, attr):
    def dictRes(dict): 
        res = ""
        for key, value in dict.items():
            res += key + "=" + '"' + value + '"' + ','
        return res
                        
    def mainRes(str1, str2):
        return "<" + str1 + " " + dictRes(attr) + ">" + str2 + "</" + str1 + ">"
    
    return mainRes(str1, str2)

def bold(str):
    return tag("b", str)

def italic(str):
    return tag("i", str)

print(tag("b", "string", {'class': 'list'}))

