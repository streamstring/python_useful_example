# encoding: utf-8

# 阶乘函数 返回正整数 n 的阶乘


def compute_factorial(n):
    if n == 0:
        return 1
    return n * compute_factorial(n-1)