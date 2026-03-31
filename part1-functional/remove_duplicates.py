"""
Part 1: Functional Programming - Remove Duplicates

A pure function that removes duplicates from a list while preserving
the original order of first occurrences.

Approach:
    Uses Python's functools.reduce to iterate through the list and
        accumulate unique elements. This is a functional programming approach
            that avoids mutation of the original input and has no side effects.
            """

from functools import reduce


def remove_duplicates(lst):
      """
          Remove duplicates from a list while preserving the order of first occurrences.

              This is a pure function:
                  - Same input always produces the same output
                      - No side effects
                          - Does not modify the original list

                              Uses functional programming via reduce to accumulate unique items.

                                  Args:
                                          lst (list): The input list potentially containing duplicates.

                                              Returns:
                                                      list: A new list with duplicates removed, preserving original order.
                                                          """
      if not lst:
                return []

      return reduce(
          lambda acc, item: acc if item in acc else acc + [item],
          lst,
          []
      )


# -------------------- Test Cases --------------------

if __name__ == "__main__":
      # Test Case 1: Mixed duplicates
      assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5], "Test 1 Failed"

    # Test Case 2: All identical elements
      assert remove_duplicates([1, 1, 1]) == [1], "Test 2 Failed"

    # Test Case 3: Empty list
      assert remove_duplicates([]) == [], "Test 3 Failed"

    # Additional edge cases
      # Test Case 4: Single element
      assert remove_duplicates([42]) == [42], "Test 4 Failed"

    # Test Case 5: No duplicates at all
      assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test 5 Failed"

    # Test Case 6: Strings (works with any hashable type)
      assert remove_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b", "c"], "Test 6 Failed"

    # Test Case 7: Verify original list is not modified (immutability check)
      original = [1, 2, 3, 2, 1]
      result = remove_duplicates(original)
      assert original == [1, 2, 3, 2, 1], "Original list was modified!"
      assert result == [1, 2, 3], "Test 7 Failed"

    print("All tests passed!")
