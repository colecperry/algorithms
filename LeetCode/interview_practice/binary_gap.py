# You are given a string named digits made of digits '1' and/or '2'. It represents a positive integer. Remove zero or more digits from it, so that each remaining digits occours an even number of times, and the value of the resulting integer is as large as possible. You may not use sort, when you remove the character at said index, you must keep the list in tact.

# Ex. 1: Given digits = "121212", the function should return "2121"
# Ex. 2: Given digits = "2121122", the function should return "221122"
# Ex. 3: Given digits "1111", the function should return "1111"

def solution(string):
    # Implement your solution here
    digits_1_to_remove = (string.count("1")) % 2
    digits_2_to_remove = (string.count("2")) % 2


    for i in range(len(string) - 1):
        if (digits_1_to_remove == 1 and string[i] == '1'):
            string = string[:i] + string[i + 1:]
            digits_1_to_remove -= 1

    for i in range(len(string) - 1, -1, -1):
        if (digits_2_to_remove == 1 and string[i] == '2'):
            string = string[:i] + string[i+1:]
            digits_2_to_remove -= 1

    return string
            

print(solution("2121122"))
print(solution("221122"))
print(solution("1111"))