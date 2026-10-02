# LeetCode

My LeetCode solutions in Python, grouped by pattern.

**Goal (Dec 31, 2026):** 300 problems · NeetCode 150 completed · 1700+ contest rating

**Solved:** 38 / 300

## Structure

One folder per pattern, one file per problem: `NNNN_problem_name.py` (e.g. `0217_contains_duplicate.py`).
Every file starts with a header (pattern, Big O, key idea) and ends with tests under `if __name__ == "__main__":`.
New problems start from [`_template.py`](_template.py).

## Log

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 217 | [Contains Duplicate](01-arrays-hashing/0217_contains_duplicate.py) | Easy | Hashing (set) | O(n) | O(n) |
| 268 | [Missing Number](01-arrays-hashing/0268_missing_number.py) | Easy | Hashing (set) | O(n) | O(n) |
| 448 | [Find All Numbers Disappeared in an Array](01-arrays-hashing/0448_find_all_numbers_dissappeared_in_the_array.py) | Easy | Hashing (set) | O(n) | O(n) |
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
