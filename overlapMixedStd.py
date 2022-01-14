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


ABC  = np.random.rand(10000000)
muAB = np.mean(ABC)
stdAB = np.std(ABC)

AB = ABC[1:4000000]
muAB = np.mean(AB)
stdBC = np.std(BC)

B = [3, 4]
muB = np.mean(B)
stdB = np.std(B)

ABC = [1, 2, 3, 4, 5, 6, 7, 8, 9]

stdABC1 = np.std(ABC)
stdABC2 = overlapMixedStd(muAB, stdAB, 4, muB, stdB, 2, muBC, stdBC, 7)

print(stdABC1)
print(stdABC2[1])
