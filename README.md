# LeetCode

My LeetCode solutions in Python, grouped by pattern.

**Goal (Dec 31, 2026):** 300 problems · NeetCode 150 completed · 1700+ contest rating

**Solved:** 62 / 300

## Structure

One folder per pattern, one file per problem: `NNNN_problem_name.py` (e.g. `0217_contains_duplicate.py`).
Every file starts with a header (pattern, Big O, key idea) and ends with tests under `if __name__ == "__main__":`.
New problems start from [`_template.py`](_template.py).

## Log

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 217 | [Contains Duplicate](01-arrays-hashing/0217_contains_duplicate.py) | Easy | Hashing (set) | O(n) | O(n) |
| 238 | [Product of Array Except Self](01-arrays-hashing/0238_product_of_array_except_self.py) | Medium | Prefix / suffix products | O(n) | O(1) |
| 268 | [Missing Number](01-arrays-hashing/0268_missing_number.py) | Easy | Hashing (set) | O(n) | O(n) |
| 448 | [Find All Numbers Disappeared in an Array](01-arrays-hashing/0448_find_all_numbers_dissappeared_in_the_array.py) | Easy | Hashing (set) | O(n) | O(n) |
| 724 | [Find Pivot Index](01-arrays-hashing/0724_find_pivot_index.py) | Easy | Prefix sum | O(n) | O(1) |
| 485 | [Max Consecutive Ones](01-arrays-hashing/0485_max_consecutive_ones.py) | Easy | Counter / stack | O(n) | O(1) |
| 1 | [Two Sum](01-arrays-hashing/0001_two_sum.py) | Easy | Hashing (dict) | O(n) | O(n) |
| 242 | [Valid Anagram](01-arrays-hashing/0242_valid_anagram.py) | Easy | Hashing (frequency dict) | O(n) | O(n) |
| 387 | [First Unique Character in a String](01-arrays-hashing/0387_first_unique_character_in_a_string.py) | Easy | Hashing (frequency dict) | O(n) | O(1) |
| 136 | [Single Number](01-arrays-hashing/0136_single_number.py) | Easy | Hashing (frequency dict) | O(n) | O(n) |
| 169 | [Majority Element](01-arrays-hashing/0169_majority_element.py) | Easy | Hashing (frequency dict) | O(n) | O(n) |
| 1929 | [Concatenation of Array](01-arrays-hashing/1929_concatenation_of_array.py) | Easy | — (list + list) | O(n) | O(n) |
| 704 | [Binary Search](05-binary-search/0704_binary_search.py) | Easy | Binary search | O(log n) | O(1) |
| 20 | [Valid Parentheses](04-stack/0020_valid_parentheses.py) | Easy | Stack | O(n) | O(n) |
| 682 | [Baseball Game](04-stack/0682_baseball_game.py) | Easy | Stack | O(n) | O(n) |
| 1047 | [Remove All Adjacent Duplicates In String](04-stack/1047_remove_all_adjacent_duplicates_in_string.py) | Easy | Stack | O(n) | O(n) |
| 844 | [Backspace String Compare](04-stack/0844_backspace_string_compare.py) | Easy | Stack | O(n + m) | O(n + m) |
| 155 | [Min Stack](04-stack/0155_min_stack.py) | Medium | Stack (two stacks) | O(1) | O(n) |
| 150 | [Evaluate Reverse Polish Notation](04-stack/0150_evaluate_reverse_polish_notation.py) | Medium | Stack | O(n) | O(n) |
| 739 | [Daily Temperatures](04-stack/0739_daily_temperatures.py) | Medium | Monotonic stack | O(n) | O(n) |
| 1480 | [Running Sum of 1d Array](01-arrays-hashing/1480_running_sum_of_1d_array.py) | Easy | Prefix sum | O(n) | O(n) |
| 1512 | [Number of Good Pairs](01-arrays-hashing/1512_number_of_good_pairs.py) | Easy | Hashing (frequency dict) | O(n) | O(n) |
| 1748 | [Sum of Unique Elements](01-arrays-hashing/1748_sum_of_unique_elements.py) | Easy | Hashing (frequency dict) | O(n) | O(n) |
| 1351 | [Count Negative Numbers in a Sorted Matrix](01-arrays-hashing/1351_count_negative_numbers_in_a_sorted_matrix.py) | Easy | Brute force (nested loops) | O(m·n) | O(1) |
| 1550 | [Three Consecutive Odds](01-arrays-hashing/1550_three_consecutive_odds.py) | Easy | Counter (run) | O(n) | O(1) |
| 1822 | [Sign of the Product of an Array](01-arrays-hashing/1822_sign_of_the_product_of_an_array.py) | Easy | Running product | O(n) | O(1) |
| 1394 | [Find Lucky Integer in an Array](01-arrays-hashing/1394_find_lucky_integer_in_an_array.py) | Easy | Hashing (frequency dict) | O(n) | O(n) |
| 344 | [Reverse String](02-two-pointers/0344_reverse_string.py) | Easy | Two pointers | O(n) | O(1) |
| 125 | [Valid Palindrome](02-two-pointers/0125_valid_palindrome.py) | Easy | Two pointers | O(n) | O(n) |
| 977 | [Squares of a Sorted Array](02-two-pointers/0977_squares_of_a_sorted_array.py) | Easy | Square + sort | O(n log n) | O(n) |
| 1672 | [Richest Customer Wealth](01-arrays-hashing/1672_richest_customer_wealth.py) | Easy | Array (running max) | O(m·n) | O(1) |
| 1470 | [Shuffle the Array](01-arrays-hashing/1470_shuffle_the_array.py) | Easy | Array (index math) | O(n) | O(n) |
| 1920 | [Build Array from Permutation](01-arrays-hashing/1920_build_array_from_permutation.py) | Easy | Array (index math) | O(n) | O(n) |
| 1431 | [Kids With the Greatest Number of Candies](01-arrays-hashing/1431_kids_with_the_greatest_number_of_candies.py) | Easy | Array (max + compare) | O(n) | O(n) |
| 1614 | [Maximum Nesting Depth of the Parentheses](04-stack/1614_maximum_nesting_depth_of_the_parentheses.py) | Easy | Stack (counter) | O(n) | O(1) |
| 167 | [Two Sum II - Input Array Is Sorted](02-two-pointers/0167_two_sum_ii_input_array_is_sorted.py) | Medium | Two pointers | O(n) | O(1) |
| 1544 | [Make The String Great](04-stack/1544_make_the_string_great.py) | Easy | Stack | O(n) | O(n) |
| 283 | [Move Zeroes](02-two-pointers/0283_move_zeroes.py) | Easy | Two pointers (same direction) | O(n) | O(1) |
| 2011 | [Final Value of Variable After Performing Operations](01-arrays-hashing/2011_final_value_of_variable_after_performing_operations.py) | Easy | Simulation | O(n) | O(1) |
| 1021 | [Remove Outermost Parentheses](04-stack/1021_remove_outermost_parentheses.py) | Easy | Stack | O(n) | O(n) |
| 11 | [Container With Most Water](02-two-pointers/0011_container_with_most_water.py) | Medium | Two pointers | O(n) | O(1) |
| 1768 | [Merge Strings Alternately](02-two-pointers/1768_merge_strings_alternately.py) | Easy | Index loop | O(n + m) | O(n + m) |
| 121 | [Best Time to Buy and Sell Stock](03-sliding-window/0121_best_time_to_buy_and_sell_stock.py) | Easy | Sliding window (running min) | O(n) | O(1) |
| 643 | [Maximum Average Subarray I](03-sliding-window/0643_maximum_average_subarray_i.py) | Easy | Sliding window (fixed k) | O(n) | O(1) |
| 1343 | [Number of Sub-arrays of Size K and Average >= Threshold](03-sliding-window/1343_number_of_sub_arrays_of_size_k_and_average_greater_than_or_equal_to_threshold.py) | Medium | Sliding window (fixed k) | O(n) | O(1) |
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](03-sliding-window/1456_maximum_number_of_vowels_in_a_substring_of_given_length.py) | Medium | Sliding window (fixed k) | O(n) | O(1) |
| 2390 | [Removing Stars From a String](04-stack/2390_removing_stars_from_a_string.py) | Medium | Stack | O(n) | O(n) |
| 2696 | [Minimum String Length After Removing Substrings](04-stack/2696_minimum_string_length_after_removing_substrings.py) | Easy | Stack | O(n) | O(n) |
| 496 | [Next Greater Element I](04-stack/0496_next_greater_element_i.py) | Easy | Brute force (nested loops + break) | O(n·m) | O(1) |
| 1295 | [Find Numbers with Even Number of Digits](01-arrays-hashing/1295_find_numbers_with_even_number_of_digits.py) | Easy | Array (counter) | O(n·d) | O(d) |
| 1365 | [How Many Numbers Are Smaller Than the Current Number](01-arrays-hashing/1365_how_many_numbers_are_smaller_than_the_current_number.py) | Easy | Brute force (nested loops) | O(n²) | O(n) |
| 232 | [Implement Queue using Stacks](04-stack/0232_implement_queue_using_stacks.py) | Easy | Stack (two stacks) | O(1) amortized | O(n) |
| 26 | [Remove Duplicates from Sorted Array](02-two-pointers/0026_remove_duplicates_from_sorted_array.py) | Easy | Two pointers (insert index) | O(n) | O(1) |
| 2215 | [Find the Difference of Two Arrays](01-arrays-hashing/2215_find_the_difference_of_two_arrays.py) | Easy | Hashing (set) | O(n·m) | O(n+m) |
| 2574 | [Left and Right Sum Differences](01-arrays-hashing/2574_left_and_right_sum_differences.py) | Easy | Prefix / suffix sums | O(n) | O(1) |
| 35 | [Search Insert Position](05-binary-search/0035_search_insert_position.py) | Easy | Binary search | O(log n) | O(1) |
| 74 | [Search a 2D Matrix](05-binary-search/0074_search_a_2d_matrix.py) | Medium | Binary search (flattened index) | O(log(m·n)) | O(1) |
| 875 | [Koko Eating Bananas](05-binary-search/0875_koko_eating_bananas.py) | Medium | Binary search on answer | O(n·log m) | O(1) |
| 509 | [Fibonacci Number](11-dynamic-programming/0509_fibonacci_number.py) | Easy | DP (bottom-up) | O(n) | O(n) |
| 1137 | [N-th Tribonacci Number](11-dynamic-programming/1137_n_th_tribonacci_number.py) | Easy | DP (bottom-up) | O(n) | O(n) |
| 118 | [Pascal's Triangle](11-dynamic-programming/0118_pascals_triangle.py) | Easy | DP (row from previous row) | O(n²) | O(n²) |
| 3174 | [Clear Digits](04-stack/3174_clear_digits.py) | Easy | Stack | O(n) | O(n) |
