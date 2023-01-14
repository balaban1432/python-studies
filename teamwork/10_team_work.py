
def my_function(s):
    stack = []
    lookup = {")" : "(", "}" : "{", "]" : "["}

    for p in s:
        if p in lookup.values():
            stack.append(p)
        elif stack and lookup[p] == stack[-1]:
            stack.pop()
        else:
            return False

    return stack == [] 

s = "[]{}"
print(my_function(s))







combination = input('Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`: ')

#([])
def isValid(par):
    bracket_map = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    openP = {"(", "[", "{"}
    stack = [] #(
    for el in par: # )
        if el in openP:
            stack.append(el)
        elif el == bracket_map[stack[-1]]: #stakc son elaman ( -> )
            stack.pop()
        else:
            return False
    return stack == [] #boolean


print(isValid(combination))
