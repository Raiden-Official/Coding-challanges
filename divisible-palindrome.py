import math

def generatePossibleList():
    """
        def generatePossibleList: Generates possible values for last 8 digits of the number
        return: a list of numbers from 0 to (10**8)-1
    """
    possible = []
    for i in range(int(math.pow(10,8))):
        possible.append(str(i))
    return possible
        
def getDivisiblePalindromesUnder1032(N):
    """
        def getDivisiblePalindromesUnder1032: Finds out all the palindromes under 10**32 divisible by N
        params: 
            N: Divisor for palindromes 
        return: a list of palindromic numbers under 10**32 divisible by N
    """
    right = generatePossibleList()
    divisiblePalindromes = []
    for R1 in right:
        L1 = int(R1[::-1])
        out = L1*math.pow(10,24) + int(R1)
        for R2 in right:
            L2 = int(str(R2)[::-1])
            inside = L2*math.pow(10,16) + R2*math.pow(10,8)
            if (inside + out)%N == 0:
                divPal = str(L1) + str(L2)
                divPal = divPal + str(R2)
                divPal = divPal + str(R1)
                divisiblePalindromes.append(divPal) 
                print(divPal)
    return divisiblePalindromes



getDivisiblePalindromesUnder1032(10000019)