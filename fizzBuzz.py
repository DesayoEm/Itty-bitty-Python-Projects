
def fizz_buzz(num:int)->str:
    """
    This is a simple fizz buzz game
    You plat by entering an integer `num` as an argument into the function. 
    
    :return:If`num`  is divisible by 3, the program returns `"fizz"`
    If `num` is divisible by `5`, it returns `"buzz"`.
    And if `num`  it's divisible by both 3 and 5, it returns `"fizz buzz"`.
    It'll return `num`  in string format if it's not divisible by either 3 or 5.

    """
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 != 0 and num % 5 != 0:
        return str(num)


for i in range(1, 101):
    print(i, fizz_buzz(i))

