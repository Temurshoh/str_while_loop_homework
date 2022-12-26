def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sikl=0
    sum=0
    while len(s)>sikl:
        if int(s[sikl])%2!=0:
            sum+=int(s[sikl]) 
        sikl+=1
    return sum
print(main("123445"))