def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sikl=0
    sum=0
    while len(s)>sikl:
        sum+=int(s[sikl]) 
        sikl+=1
    return sum
print(main("123"))