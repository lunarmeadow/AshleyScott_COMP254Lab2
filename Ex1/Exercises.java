/*
 * Copyright 2014, Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser
 *
 * Developed for use with the book:
 *
 *    Data Structures and Algorithms in Java, Sixth Edition
 *    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
 *    John Wiley & Sons, 2014
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */


/**
 * Code for end-of-chapter exercises on asymptotics.
 *
 * @author Michael T. Goodrich
 * @author Roberto Tamassia
 * @author Michael H. Goldwasser
 */
class Exercises {

  /** Returns the sum of the integers in given array. */
  // This algorithm has an O(n) run-time, where n = the array length.
  // It performs a single-pass iteration over the entirety of a dataset,
  // so scales directly linearly with input.
  public static int example1(int[] arr) {
    int n = arr.length, total = 0;
    for (int j=0; j < n; j++)       // loop from 0 to n-1
      total += arr[j];
    return total;
  }

  /** Returns the sum of the integers with even index in given array. */
  // This algorithm has an O(n) run-time, where n = the array length.
  // Despite the fact there are n/2 iterations, 
  // the algorithm still scales with respect to n.
  // Big-O notation discards any constant factors.
  public static int example2(int[] arr) {
    int n = arr.length, total = 0;
    for (int j=0; j < n; j += 2)    // note the increment of 2
      total += arr[j];
    return total;
  }

  /** Returns the sum of the prefix sums of given array. */
  // This algorithm has an O(n^2) run-time, where n = the array length.
  // The outer loop scales linearly with N, 
  // and the inner loop will iterate for however many iterations have been run
  // of the outer loop. For instance, on the 100th iteration of the outer loop,
  // J will be 100. Thus, the inner loop will run 100 times for that iteration.
  // You have n inner iterations for every nth outer iteration.
  public static int example3(int[] arr) {
    int n = arr.length, total = 0;
    for (int j=0; j < n; j++)       // loop from 0 to n-1
      for (int k=0; k <= j; k++)    // loop from 0 to j
        total += arr[j];
    return total;
  }

  /** Returns the sum of the prefix sums of given array. */
  // This algorithm has an O(n) run-time, where n = the array length.
  // We perform a single-pass iteration through the array.
  // The contents of each iteration are more expensive than a more trivial instance like
  // example 1, but big-O notation is in pure respect to scaling.
  public static int example4(int[] arr) {
    int n = arr.length, prefix = 0, total = 0;
    for (int j=0; j < n; j++) {     // loop from 0 to n-1
      prefix += arr[j];
      total += prefix;
    }
    return total;
  }

  /** Returns the number of times second array stores sum of prefix sums from first. */
  // This algorithm has an O(n^3) run-time. Both arrays are of equal length.
  // There is no early exit condition, it will process the entire array.
  // The first array is iterated through entirely for each iteration of the outer loop,
  // for each iteration of the second array.
  public static int example5(int[] first, int[] second) { // assume equal-length arrays
    int n = first.length, count = 0;
    for (int i=0; i < n; i++) {     // loop from 0 to n-1
      int total = 0;
      for (int j=0; j < n; j++)     // loop from 0 to n-1
        for (int k=0; k <= j; k++)  // loop from 0 to j
          total += first[k];
      if (second[i] == total) count++;
    }
    return count;
  }

}
