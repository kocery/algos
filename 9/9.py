from typing import List
from random import randint
import unittest
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def sub_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def create_random_matr(n: int) -> List[List[int]]:
    return [[randint(1, 40) for _ in range(n)] for _ in range(n)]


def standard_matr_mult(f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
    if len(f[0]) != len(s):
        raise ValueError("Несовместимые размеры матриц для умножения")

    res = [[0] * len(s[0]) for _ in range(len(f))]
    for i in range(len(f)):
        for j in range(len(s[0])):
            for k in range(len(s)):
                res[i][j] += f[i][k] * s[k][j]

    return res


def fast_matr_mult(x: List[List[int]], y: List[List[int]]) -> List[List[int]]:
    if len(x) <= 3:
        return standard_matr_mult(x, y)

    n = len(x)

    a = [r[:n // 2] for r in x[:n // 2]]
    b = [r[n // 2:] for r in x[:n // 2]]
    c = [r[:n // 2] for r in x[n // 2:]]
    d = [r[n // 2:] for r in x[n // 2:]]

    e = [r[:n // 2] for r in y[:n // 2]]
    f = [r[n // 2:] for r in y[:n // 2]]
    g = [r[:n // 2] for r in y[n // 2:]]
    h = [r[n // 2:] for r in y[n // 2:]]

    i = add_matrix(fast_matr_mult(a, e), fast_matr_mult(b, g))
    j = add_matrix(fast_matr_mult(a, f), fast_matr_mult(b, h))
    k = add_matrix(fast_matr_mult(c, e), fast_matr_mult(d, g))
    l = add_matrix(fast_matr_mult(c, f), fast_matr_mult(d, h))

    return [i[r] + j[r] for r in range(len(i))] + [k[r] + l[r] for r in range(len(k))]


def strassen_matr_mult(x, y):
    n = len(x)

    if n <= 3:
        return standard_matr_mult(x, y)

    half_n = n // 2

    a = [r[:half_n] for r in x[:half_n]]
    b = [r[half_n:] for r in x[:half_n]]
    c = [r[:half_n] for r in x[half_n:]]
    d = [r[half_n:] for r in x[half_n:]]

    e = [r[:half_n] for r in y[:half_n]]
    f = [r[half_n:] for r in y[:half_n]]
    g = [r[:half_n] for r in y[half_n:]]
    h = [r[half_n:] for r in y[half_n:]]

    p1 = strassen_matr_mult(a, sub_matrix(f, h))
    p2 = strassen_matr_mult(add_matrix(a, b), h)
    p3 = strassen_matr_mult(add_matrix(c, d), e)
    p4 = strassen_matr_mult(d, sub_matrix(g, e))
    p5 = strassen_matr_mult(add_matrix(a, d), add_matrix(e, h))
    p6 = strassen_matr_mult(sub_matrix(b, d), add_matrix(g, h))
    p7 = strassen_matr_mult(sub_matrix(a, c), add_matrix(e, f))

    q1 = add_matrix(sub_matrix(add_matrix(p5, p4), p2), p6)
    q2 = add_matrix(p1, p2)
    q3 = add_matrix(p3, p4)
    q4 = sub_matrix(sub_matrix(add_matrix(p5, p1), p3), p7)

    return [q1[r] + q2[r] for r in range(len(q1))] + [q3[r] + q4[r] for r in range(len(q3))]


def calculate_statistics(execution_times):
    mean_time = np.mean(execution_times)
    std_deviation = np.std(execution_times)
    geometric_mean = np.exp(np.mean(np.log(execution_times)))
    return mean_time, std_deviation, geometric_mean


def run_algorithm(algorithm, A, B, num_runs=10):
    execution_times = []
    for _ in range(num_runs):
        start_time = time.perf_counter()
        result = algorithm(A, B)
        end_time = time.perf_counter()
        execution_times.append(end_time - start_time)
    return execution_times, result


class MatrixMultiplicationTest(unittest.TestCase):
    def test_matrix_multiply_algorithms(self):
        algorithms = [
            standard_matr_mult,
            fast_matr_mult,
            strassen_matr_mult
        ]

        matrix_sizes = [2 ** i for i in range(2, 10)]  # Adjust the range as needed

        results = {algorithm.__name__: {'mean_times': [], 'std_deviations': [], 'geometric_means': []}
                   for algorithm in algorithms}

        for size in matrix_sizes:
            matrix_A = np.random.rand(size, size)
            matrix_B = np.random.rand(size, size)

            for algorithm in algorithms:
                with self.subTest(algorithm=algorithm):
                    execution_times, result = run_algorithm(algorithm, matrix_A, matrix_B)
                    mean_time, std_deviation, geometric_mean = calculate_statistics(execution_times)
                    results[algorithm.__name__]['mean_times'].append(mean_time)
                    results[algorithm.__name__]['std_deviations'].append(std_deviation)
                    results[algorithm.__name__]['geometric_means'].append(geometric_mean)

        plt.figure(figsize=(18, 10))
        for algorithm, stats in results.items():
            plt.plot(matrix_sizes, stats['mean_times'], label=algorithm)
        plt.xscale('log', base=2)
        plt.yscale('log')
        plt.title('Average Execution Time of Matrix Multiplication Algorithms')
        plt.xlabel('Matrix Size (Power of 2)')
        plt.ylabel('Log(Average Execution Time)')
        plt.legend()
        plt.show()

        plt.figure(figsize=(18, 10))
        for algorithm, stats in results.items():
            plt.plot(matrix_sizes, stats['geometric_means'], label=f"{algorithm} - Geometric Mean")
        plt.xscale('log', base=2)
        plt.yscale('log')
        plt.title('Geometric Mean of Matrix Multiplication Algorithms')
        plt.xlabel('Matrix Size (Power of 2)')
        plt.ylabel('Log(Geometric Mean)')
        plt.legend()
        plt.show()

        plt.figure(figsize=(18, 10))
        for algorithm, stats in results.items():
            plt.plot(matrix_sizes, stats['std_deviations'], label=f"{algorithm} - Standard Deviation")
        plt.xscale('log', base=2)
        plt.title('Standard Deviation of Matrix Multiplication Algorithms')
        plt.xlabel('Matrix Size (Power of 2)')
        plt.ylabel('Standard Deviation')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    unittest.main()
