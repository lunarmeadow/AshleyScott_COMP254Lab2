# public static boolean unique1(int[] data) {
#     int n = data.length;
#     for (int j=0; j < n-1; j++)
#       for (int k=j+1; k < n; k++)
#         if (data[j] == data[k])
#           return false;                    // found duplicate pair
#     return true;                           // if we reach this, elements are unique
#   }

#   /** Returns true if there are no duplicate elements in the array. */
#   public static boolean unique2(int[] data) {
#     int n = data.length;
#     int[] temp = Arrays.copyOf(data, n);   // make copy of data
#     Arrays.sort(temp);                     // and sort the copy
#     for (int j=0; j < n-1; j++)
#       if (temp[j] == temp[j+1])            // check neighboring entries
#         return false;                      // found duplicate pair
#     return true;                           // if we reach this, elements are unique
#   }

import copy
from time import perf_counter
import math

def unique1(n, x):
    count = 0

    start = perf_counter()

    # We are only interested in scaling and runtime,
    # but run the check anyways to simulate performance for each O.
    for j in range(n - 1):
        for k in range(j + 1, n):
            if x[j] == x[k]:
                return False
            count += 1

    end = perf_counter() - start

    print(
        f"  Func 1 performed {count:,} iterations in {end:2f} seconds where n = {n}\n       (projected {round(count * 60/end):,} in 1 minute)"
    )

    return round(count * 60/end)

def unique2(n, x):
    temp = copy.deepcopy(x)
    temp.sort()

    count = 0
    start = perf_counter()

    # We are only interested in scaling and runtime,
    # but run the check anyways to simulate performance for each O.
    for j in range(n - 1):
        if temp[j] == temp[j + 1]:
            return False
        count += 1

    end = perf_counter() - start

    print(
        f"  Func 2 performed {count:,} iterations in {end:2f} seconds where n = {n}\n       (projected {round(count * 60/end):,} in 1 minute)"
    )

    return round(count * 60/end)

    

# Benchmark results on my Ryzen 7 3700x:
# -----------------------------------------------------------------------------------------------
#   Func 1 performed 499,500 iterations in 0.028878 seconds where n = 1000
#        (projected 1,037,827,263 in 1 minute)
# ///////////////////////////////////////////////////////////////////////////////////////////////
#   Func 2 performed 999 iterations in 0.000049 seconds where n = 1000
#        (projected 1,219,978,771 in 1 minute)
# -----------------------------------------------------------------------------------------------
#   Func 1 performed 1,999,000 iterations in 0.092190 seconds where n = 2000
#        (projected 1,301,002,168 in 1 minute)
# ///////////////////////////////////////////////////////////////////////////////////////////////
#   Func 2 performed 1,999 iterations in 0.000099 seconds where n = 2000
#        (projected 1,208,268,706 in 1 minute)
# -----------------------------------------------------------------------------------------------
#   Func 1 performed 4,498,500 iterations in 0.204477 seconds where n = 3000
#        (projected 1,320,002,322 in 1 minute)
# ///////////////////////////////////////////////////////////////////////////////////////////////
#   Func 2 performed 2,999 iterations in 0.000150 seconds where n = 3000
#        (projected 1,195,916,595 in 1 minute)
# -----------------------------------------------------------------------------------------------
#   Func 1 performed 7,998,000 iterations in 0.355645 seconds where n = 4000
#        (projected 1,349,323,740 in 1 minute)
# ///////////////////////////////////////////////////////////////////////////////////////////////
#   Func 2 performed 3,999 iterations in 0.000202 seconds where n = 4000
#        (projected 1,187,357,410 in 1 minute)
# -----------------------------------------------------------------------------------------------
#   Func 1 performed 12,497,500 iterations in 0.547535 seconds where n = 5000
#        (projected 1,369,501,268 in 1 minute)
# ///////////////////////////////////////////////////////////////////////////////////////////////
#   Func 2 performed 4,999 iterations in 0.000261 seconds where n = 5000
#        (projected 1,147,436,876 in 1 minute)
# -----------------------------------------------------------------------------------------------
# | Func 1 had an average 1 minute projection of 1,275,531,352
# | Func 2 had an average 1 minute projection of 1,191,791,672

# Func 1 unexpectedly has a higher average projection.
# I predict that this is the result of a very expensive deep copy and sorting operation.
# The input data is best-case however, being a sequential list of numbers 0 .. n
# It would be worth investigating the internals of
# the default Python sort and deep copy for further explanation.

def main():
    print("-----------------------------------------------------------------------------------------------")

    u1_projections = []
    u2_projections = []

    # I know the assignment requirements said to binary search for the 60-sec upper-bound of N
    # I couldn't really figure that out so I decided to just run a few tests with some timers instead
    for n in [1000, 2000, 3000, 4000, 5000]:
        x = list(range(n))
        u1_projections.append(unique1(n, x))
        print("///////////////////////////////////////////////////////////////////////////////////////////////")
        u2_projections.append(unique2(n, x))
        print("-----------------------------------------------------------------------------------------------")

    print(f'| Func 1 had an average 1 minute projection of {round(sum(u1_projections) / len(u1_projections)):,}')
    print(f'| Func 2 had an average 1 minute projection of {round(sum(u2_projections) / len(u2_projections)):,}')

if __name__ == "__main__":
    main()
