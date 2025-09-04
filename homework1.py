from re import findall


def sort_1(str_1):
    output = []
    stack = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    ch = findall('[0-9]+|[-*/+)(]', str_1)
    for el in ch:
        if el.isdigit():
            output.append(el)
        elif el in priority:
            if not stack or '(' in stack:
                stack.append(el)
            else:
                while priority[stack[-1]] >= priority[el]:
                    output.append(stack.pop())
                    if not stack:
                        break
                stack.append(el)
        elif el == '(':
            stack.append(el)
        else:
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return output


def count(str_1):
    helper = []
    for el in str_1:
        if el.isdigit():
            helper.append(el)
        else:
            b = int(helper.pop())
            a = int(helper.pop())
            if el == '+':
                res = a + b
            elif el == '-':
                res = a - b
            elif el == '/':
                res = a // b
            else:
                res = a * b
            helper.append(res)
    return helper[0]



str1 = input()
p = sort_1(str1)
print(count(p))
