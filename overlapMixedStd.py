from time import time

import numpy as np

'''
由 [ 样本{A+B}的均值、标准差、样本个数,
    样本B的均值、标准差、样本个数， 
    样本{B+C}的均值、标准差、样本个数 ]
    计算新的{A+B+C}的均值、标准差
    
Input:  muAB:样本{A+B}的均值
        stdAB:样本{A+B}的标准差
        aPlusb:{A+B}的样本个数
        ==
        muB:样本B的均值
        stdB:样本B的标准差
        b:Y的样本个数
        ==
        muBC:样本{B+C}的均值
        stdBC:样本{B+C}的标准差
        bPlusc:{B+C}的样本个数

Output:
        muABC:样本{A+B+C}的均值
        stdABC:样本{A+B+C}的标准差

'''

def overlapMixedStd(muAB, stdAB, aPlusb, muB, stdB, b, muBC, stdBC, bPlusc):
    import math

    a = aPlusb - b
    c = bPlusc - b

    muA = (aPlusb * muAB - b * muB) / a

    t1 = (a * b * (muA - muB) ** 2) / aPlusb
    stdA = math.sqrt((aPlusb * stdAB ** 2 - b * stdB ** 2 - t1) / a)

    muABC = (a * muA + bPlusc * muBC) / (a + b + c)
    t2 = (a * bPlusc * (muA - muBC) ** 2) / (a + bPlusc)
    stdABC = math.sqrt((a * stdA ** 2 + bPlusc * stdBC ** 2 + t2) / (a + bPlusc))

    return muABC, stdABC

print(time())
ABC  = (4*np.random.rand(20000000)).tolist()
muABC = np.mean(ABC)
stdABC1 = np.std(ABC)

AB = ABC[0:12000000]
muAB = np.mean(AB)
stdAB = np.std(AB)
lenAB=len(AB)

BC = ABC[8000000:]
muBC = np.mean(BC)
stdBC = np.std(BC)
lenBC=len(BC)

B=ABC[800000:1200000]
muB = np.mean(B)
stdB = np.std(B)
lenB=len(B)

print(time())
stdABC2 = overlapMixedStd(muAB, stdAB, lenAB, muB, stdB, lenB, muBC, stdBC, lenBC)
print(time())

print(stdABC1)
print(stdABC2[1])
