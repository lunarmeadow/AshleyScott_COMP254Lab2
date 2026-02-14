#  public static double[] prefixAverage1(double[] x) {
#     int n = x.length;
#     double[] a = new double[n];    // filled with zeros by default
#     for (int j=0; j < n; j++) {
#       double total = 0;            // begin computing x[0] + ... + x[j]
#       for (int i=0; i <= j; i++)
#         total += x[i];
#       a[j] = total / (j+1);        // record the average
#     }
#     return a;
#   }

#   /** Returns an array a such that, for all j, a[j] equals the average of x[0], ..., x[j]. */
#   public static double[] prefixAverage2(double[] x) {
#     int n = x.length;
#     double[] a = new double[n];    // filled with zeros by default
#     double total = 0;              // compute prefix sum as x[0] + x[1] + ...
#     for (int j=0; j < n; j++) {
#       total += x[j];               // update prefix sum to include x[j]
#       a[j] = total / (j+1);        // compute average based on current sum
#     }
#     return a;
#   }

from time import perf_counter
import random

def prefixAverage1(n, x):
    start = perf_counter()
    a = [0.0] * n
    for j in range(n):
        total = 0
        for i in range(j):
            total += x[i]
            a[j] = total / (i + 1)
    elapsed = perf_counter() - start
    print(f"{elapsed:2f} seconds elapsed for {n:,} iterations of Func 1")

def prefixAverage2(n, x):
    start = perf_counter()
    a = [0.0] * n
    total = 0
    for j in range(n):
        total += x[j]
        a[j] = total / (j + 1)
    elapsed = perf_counter() - start
    print(f"{elapsed:2f} seconds elapsed for {n:,} iterations of Func 2")

# Benchmark from my Ryzen 7 3700x:
# -----------------------------------------------------------------------------------------------
# 0.009659 seconds elapsed for 500 iterations of Func 1
# ///////////////////////////////////////////////////////////////////////////////////////////////
# 0.000068 seconds elapsed for 500 iterations of Func 2
# -----------------------------------------------------------------------------------------------
# 0.823468 seconds elapsed for 5,000 iterations of Func 1
# ///////////////////////////////////////////////////////////////////////////////////////////////
# 0.000351 seconds elapsed for 5,000 iterations of Func 2
# -----------------------------------------------------------------------------------------------
# 3.339765 seconds elapsed for 10,000 iterations of Func 1
# ///////////////////////////////////////////////////////////////////////////////////////////////
# 0.000724 seconds elapsed for 10,000 iterations of Func 2
# -----------------------------------------------------------------------------------------------

# This shows that function 1 is O(n^2) and is much more expensive for each operation in n^2.
# This shows that function 2 is O(n) and is fairly cheap for each operation in n.

def main():
    print("-----------------------------------------------------------------------------------------------")
    for n in [500, 5000, 10000]:
        x = [random.random() for _ in range(n)]
        prefixAverage1(n, x)
        print("///////////////////////////////////////////////////////////////////////////////////////////////")
        prefixAverage2(n, x)
        print("-----------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()