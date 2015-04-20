"""
Recursion according to the "Cat in the Hat"
"""
def wrapper(f):
    f.count=0
    
    def worker(*args):
        
        f.count+=1
        t =f( *args )
        print(f.count)
        return t
    return worker

@wrapper
def memoized_fib(num, memo_dict):
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

print(memoized_fib(25,{0:0,1:1}))        
def get_next_cat(current_cat):
    """
    Helper function to get next cat
    """
    if current_cat == "Cat in the Hat":
        return "Little Cat A"
    elif current_cat != "Little Cat Z":
        return "Little Cat " + chr(ord(current_cat[-1]) + 1)
    else:
        return "Voom"
def add_up(n):
    if n == 0:
        return 0
    else:
        return n + add_up(n - 1)

print(add_up(5))
print()


@wrapper
def clean_up(helper_cat):
    """
    Recursive function that prints out story
    """
    if helper_cat == "Voom":
        print(helper_cat + ": I got this. Mess is all cleaned up!")
    else:
        next_cat = get_next_cat(helper_cat)
        print(helper_cat + ": I'll have", next_cat, "clean up!")
        clean_up(next_cat)

clean_up("Cat in the Hat")
        