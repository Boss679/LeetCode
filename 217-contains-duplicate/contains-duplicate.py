class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines if the given list of integers contains any duplicates.

        Args:
            nums (List[int]): The list of integers to be checked for duplicates.

        Returns:
            bool: True if there are any duplicates in the list, False otherwise.
        """

        # Create an empty set to store unique integers encountered so far.
        hashet = set()

        # Iterate through the list of integers.
        for n in nums:
            # If the integer is already in the set, it's a duplicate.
            if n in hashet:
                return True
            # Otherwise, add it to the set.
            hashet.add(n)
        # If no duplicates were found, return False.
        return False