#Write a program to check if a given string of parentheses is balanced.


def checkParenthesesBalanced(string):
    all = []
    for index in string:
        if index == "(" or index == "{" or index == "[":
            all.append(index)
        else:
            if not all:       #if there are a ),},] without (,{,[
                return False
            char = all.pop()  #the last element
            if char == "(":
                if index != ")":
                    return False
            if char == "{":
                if index != "}":
                    return False
            if char == "[":
                if index != "]":
                    return False
    return True


str0 = "()[{()}]"
print("\n", str0, "Is balanced" if checkParenthesesBalanced(str0) else "Is not balanced")

str1 = "()[{()}}]"
print("\n", str1, "Is balanced" if checkParenthesesBalanced(str1) else "Is not balanced")

