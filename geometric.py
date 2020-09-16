import math
def prob(n, p):
    return float(p**n)

def infoMeasure(n, p):
    return -1*float(math.log2(prob(n,p)))

def sumProb(N, p):
    sum=0.0
    for n in range(1, N+1):
        sum+=prob(n, p)
    return sum
"""
hàm sumProb là tổng của cấp số nhân lùi hữu hạn( vô hạn phụ thuộc vào giá trị N)
theo công thức tính tổng cấp số nhân lùi vô hạn ta tính được giá trị của sum sẽ có lim=1.
"""
def  approxEntropy(N,p):
    result = 0.0
    for n in range(1, N+1):
        key = prob(n, p)
        result+= key*math.log2(key)*-1
    return result
"""
công thức được rút gọn về dạng k/2**k nên khi N chạy tới vô cugf, kết quả sẽ là xấp xỉ N với p=0.5;
"""

print(approxEntropy(3,0.5))