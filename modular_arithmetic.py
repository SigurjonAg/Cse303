def func(y,x,n):
    """Returns y**x mod n"""
    w = len(bin(x))-2
    s_k =1
    for k in range(w):
        if kth_bit(x,k):
            R_k = (s_k*y) % n
        else:
            R_k = s_k
        s_k = (R_k**2) % n
    return R_k

def kth_bit(num, k):
    return num&(1<<k)

def visualise(y,x,n):
    res = func(y,x,n)
    res0 = y**x
    res1 = res0 % n
    print("{} to the {} is: {}".format(x,y,res0))
    print("{} mod {} is : {}".format(res0, n,res1))
    print("your function gives: ", res)