class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_dict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
        res = []

        def backtrack(path, index):
            # Base Case -> reached max path length
            if len(path) == len(str(digits)):
                res.append(path[:])
                return
            
            # Get letters for that digit index
            letters = digit_dict[str(digits)[index]] 

            for letter in letters: # try each letter
                path.append(letter)
                backtrack(path, index + 1)
                path.pop()

        backtrack([], 0)

        return res