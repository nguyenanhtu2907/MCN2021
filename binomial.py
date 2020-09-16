import math

def prob(n, p, N):
    return (math.factorial(N)/(math.factorial(N-n)*math.factorial(n)))*float(p**n)


def infoMeasure(n, p, N):
    return -1*float(math.log2(prob(n, p, N)))


def sumProb(N, p):
    sum = 0.0
    for n in range(1, N+1):
        sum += prob(n, p, N)
    return sum


"""
hàm sumProb là tổng của cấp số nhân lùi hữu hạn( vô hạn phụ thuộc vào giá trị N)
theo công thức tính tổng cấp số nhân lùi vô hạn ta tính được giá trị của sum sẽ có lim=1.
"""


def approxEntropy(N, p):
    result = 0.0
    for n in range(1, N+1):
        key = prob(n, p, N)
        result += key*-1*infoMeasure(n, p, N)
    return result


print(approxEntropy(3, 0.5))
