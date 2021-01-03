class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet_num_list = []
        for char in s:
            if char.isalnum():
                alphabet_num_list.append(char.lower())
        for i in range(len(alphabet_num_list)//2):
            if alphabet_num_list[i] != alphabet_num_list[-i-1]:
                return False
        return True
