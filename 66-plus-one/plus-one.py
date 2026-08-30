class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = 0
        digits = digits[::-1]

        while i < len(digits) and carry:
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
            i += 1

        if carry:
            digits.append(carry)

        return digits[::-1]