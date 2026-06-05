class Solution:
    def addTwoNumbers(self, list1, list2):
        result = []
        carry = 0
        for i in range(len(list1)):
            total = list1[i] + list2[i] + carry
            result.append(total % 10)
            carry = total // 10
        if carry:
            result.append(carry)
        return result