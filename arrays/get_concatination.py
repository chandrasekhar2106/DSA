from typing import List
from copy import deepcopy

class GetConcatination:
    
    def getConcatinationWithExtend(self, nums: List[int]) -> List[int]:
        # Using deepcopy method so not to update orginal nums when result changes
        result = deepcopy(nums)

        result.extend(nums)
        return result
    
    def getConcatinationWithLoop(self, nums):
        nums_length = len(nums)
        result = [0] * (2*nums_length)
        for i, value in enumerate(nums):
            result[i] = result[i+nums_length] = value

        return result
