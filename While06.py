def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    sikl=0
    undoshlar=0
    undosh="aeiou"
    while len(s)>sikl:
        if undosh.find(s[sikl])!=-1:
            undoshlar+=1
        sikl+=1
    return undoshlar
print(main("codeschooluz"))
