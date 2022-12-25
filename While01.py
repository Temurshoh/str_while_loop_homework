def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    l=0
    while len(s)>l:
        if s[l].isdigit():
            i+=1
        l+=1 
    
        
    return i
print(main("python 2022")) 
