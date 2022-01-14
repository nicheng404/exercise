import numpy as np

'''
由样本X的均值、标准差、样本个数，Y的均值、标准差、样本个数，计算新的Z={X}+{Y}的均值、标准差
Input:  muX:样本X的均值
        stdX:样本X的标准差
        m:X的样本个数
        ==
        muY:样本Y的均值
        stdY:样本Y的标准差
        n:Y的样本个数

Output:
        muZ:样本Z的均值
        stdZ:样本Z的标准差

'''
def mixedStd(muX, stdX, m, muY, stdY, n):
    import math
    muZ = (m * muX + n * muY) / (m + n)

    t = (m * n * (muX - muY) ** 2) / (m + n)
    stdZ = math.sqrt((m * stdX ** 2 + n * stdY ** 2 + t) / (m + n))

    return muZ, stdZ

