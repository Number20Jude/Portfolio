# Types of problems
# 1 + 1 addition 
# 1 - 1 subtration 
# 1 / 1 division
# 1 * 1 multiplication 
# 1 ^ 1 powers
# 1 | 1 roots
# (1 + 1) parenthesis
# (1+3)/(3*2) fractions

import math
mathProblem = str(input('Enter a mathamatical equation: '))
strVersion = []
currentProblemSection = []
currentProblem = []
totalChar = -1
checkFP = 0


def mathOperation(list,totalChar):
    strVersion = list
    currentProblemSection = []
    currentProblem = []
    total = len(list)
    section = -1
    checkFP = 0
    continues = 0
    while total > 1:
        for x in list:
            totalChar += 1
    
   
            if x == '(':
                checkFP = 1
                currentProblemSection.append(totalChar) 
            if x == ')':
                currentProblemSection.append(totalChar) 
                break
    
        
        if checkFP == 1:
            currentProblem = strVersion[currentProblemSection[0] +1 :currentProblemSection[1] ]
        
            print(currentProblem)

            for x in currentProblem:
                section += 1
                if x == "^" or "|":
                    if x == "^":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x**y]
                    if x == "|":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [y**(1/x)]
                    print(currentProblem)
            section = -1
            for x in currentProblem:   
                section += 1        
                if x == "*" or "/":
                    if x == "*":
                        print(currentProblem)
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x*y]
                    if x == "/":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x/y]
                    print(currentProblem)
            section = -1
            for x in currentProblem: 
                section += 1
                if x == "-" or "+":
                    if x == "+":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x+y]
                    if x == "-":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x-y]
                    print(currentProblem)
            checkFP = 0   
            strVersion[currentProblemSection[0]:currentProblemSection[1] + 1] = [str(currentProblem).replace('[', '').replace(']', '')]
        for x in strVersion:
            
            if x == ")":
                continues = 0
                break
            else:
                continues = 1
        if continues == 1:
            currentProblem = strVersion
        
            print(currentProblem)

            for x in currentProblem:
                section += 1
                if x == "^" or "|":
                    if x == "^":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x**y]
                    if x == "|":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [y**(1/x)]
                    print(currentProblem)
            section = -1
            for x in currentProblem:   
                section += 1        
                if x == "*" or "/":
                    if x == "*":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x*y]
                    if x == "/":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x/y]
                    print(currentProblem)
            section = -1
            for x in currentProblem: 
                section += 1
                if x == "-" or "+":
                    if x == "+":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x+y]
                    if x == "-":
                        x = float(currentProblem[section - 1])
                        y = float(currentProblem[section + 1])
                        currentProblem[section-1:section+2] = [x-y]
                    print(currentProblem)
                
            strVersion = [currentProblem]
        print(currentProblem)
        
       


        total = len(list)

def combine_adjacent_numbers(lst):
    result = []
    buffer = ""

    for item in lst:
        if item.isdigit():
            buffer += item
        else:
            if buffer:
                result.append(buffer)
                buffer = ""
            result.append(item)

    # Append any remaining number in buffer
    if buffer:
        result.append(buffer)

    return result

strVersion += mathProblem
strVersion = combine_adjacent_numbers(strVersion)
print(strVersion)



mathOperation(strVersion,totalChar)

print(strVersion)