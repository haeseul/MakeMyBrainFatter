from ArrayStack import ArrayStack

def checkBrackets(str):
    s = ArrayStack()

    for c in str:
        if c == '[' or c == '{' or c == '(':
            s.push(c)
        elif c == ']' or c == '}' or c == ')':
            if s.isEmpty():
                return False    # 조건 2 위배
            else:
                left = s.pop()
                if (c == ']' and left != '[') or \
                    (c == '}' and left != '{') or \
                    (c == ')' and left != '('):
                    return False    # 조건 3 위배
    return s.isEmpty()

s1 = "{ A[ (i+1) ] = 0; }"
s2 = "if( (i==0) && (j==0)"
s3 = "A[ (i+1] ) = 0;"

print(s1, "---> ", checkBrackets(s1))
print(s2, "---> ", checkBrackets(s2))
print(s3 , "---> ", checkBrackets(s3))
