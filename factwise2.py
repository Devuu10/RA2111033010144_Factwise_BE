# -*- coding: utf-8 -*-


def maxScore(cardPoints, k):
    n = len(cardPoints)

    window_sum = sum(cardPoints[:k])
    max_sum = window_sum

    for i in range(k):
      window_sum+= cardPoints[n-1-i]- cardPoints[k-1-i]
      max_sum = max(max_sum, window_sum)
    return max_sum
print(maxScore([1,2,3,4,5,6,1],3))
print(maxScore([2,2,2],2))
print(maxScore([9,7,7,9,7,7,9],7))
