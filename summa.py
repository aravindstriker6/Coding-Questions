def romanToDecimal(S):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    a = roman[S[0]]+roman[S[-1]]
    i=1
    while i<len(S)-1:

        print(a)
        if (roman[S[i]] >= roman[S[i+1]]):
            a = a+roman[S[i]]
            i=i+1
        else:
            a = a -roman[S[i]]
            i=i+1
    return a

print(romanToDecimal('CMXVI'))
