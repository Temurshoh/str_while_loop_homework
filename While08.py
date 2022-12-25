def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sikl=0
    juftson=0
    
    while len(s)>sikl:
        if int(s[sikl])%2!=0:

            juftson+=1
        sikl+=1
    return juftson
print(main("23456789as"))