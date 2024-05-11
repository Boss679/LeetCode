class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of all elements in the given list except for the element itself.

        Args:
            nums (List[int]): List of input integers.

        Returns:
            List[int]: List containing the product of all elements except for the element itself.
        """

        # Initialize a list to store the result.
        res = [1] * (len(nums))

        # Calculate the product of all elements to the left of each element.
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        # Initialize a variable to store the product of all elements to the right of each element.
        postfix = 1

        # Calculate the product of all elements to the right of each element and multiply it with the product
        # of all elements to the left of each element to get the final result.
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res