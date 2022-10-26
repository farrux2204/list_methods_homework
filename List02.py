def main(fruits,x,i):
    """
    You will be given a list of fruits. Add the x fruit to the i index and return it.
    Args:
        fruits(list): parameter 
        x(str): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    a=fruits
    a.insert(i,x)
    return a
print(main(['olma','nok','behi'],'apple',0))