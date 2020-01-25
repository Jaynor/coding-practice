class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max_now = 0
        temp_max = 0
        point_l = 0
        temp_dic = {}
        for i, chr in enumerate(s):
            if chr in temp_dic and temp_dic[chr] >= point_l:
                max_now = max(temp_max, max_now)
                temp_max = i - temp_dic[chr]
                point_l = temp_dic[chr] + 1
            else:
                temp_max += 1
            temp_dic[chr] = i

        return max(max_now, temp_max)

def main():
    str1 = Solution()
    print(str1.lengthOfLongestSubstring("pwwkew"))

main()