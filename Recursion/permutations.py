# Write a program to generate all permutations of a string using recursion.


def permutations(string):
    result = []
    if len(string) == 0:
        return [""]
    else:
        for index in range(len(string)):
            string[0], string[index] = string[index], string[0]
            subP = permutations(string[1:])
            for one in subP:
                result.append(string[0] + one)
            string[0], string[index] = string[index], string[0]
        return result


str1 = "ABC"
allP = permutations(list(str1))
print("all the permutations of ABC ", allP)
