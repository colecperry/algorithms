class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1   # 2147483647
        INT_MIN = -(2**31)    # -2147483648

        sign = -1 if x < 0 else 1
        x = abs(x) # reverse the abs val, reapply sign at end
        result = 0

        while x != 0:
            digit = x % 10 # get last digit
            result = result * 10 + digit # update result
            x //= 10 # remove last digit with floor division

        result *= sign # reapply original sign
        return result if INT_MIN <= result <= INT_MAX else 0