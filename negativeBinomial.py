import math

def prob(n, p, N, r):
    return (math.factorial(n)/(math.factorial(n-r+1)*math.factorial(r-1)))*float(p**n)


def infoMeasure(n, p, N, r):
    return -1*float(math.log2(prob(n, p, N, r)))


def sumProb(N, p, r): 
    sum = 0.0
    for n in range(r, N+1):
        sum += prob(n, p, N, r)
    return sum


"""
hàm sumProb là tổng của cấp số nhân lùi hữu hạn( vô hạn phụ thuộc vào giá trị N)
theo công thức tính tổng cấp số nhân lùi vô hạn ta tính được giá trị của sum sẽ có lim=1.
"""


def approxEntropy(N, p, r):
    result = 0.0
    for n in range(r, N+1):
        key = prob(n, p, N, r)
        result += key*-1*infoMeasure(n, p, N, r)
    return result


