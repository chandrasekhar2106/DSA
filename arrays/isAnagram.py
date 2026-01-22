class isAnagram:

    def isAnagramWithHashMap(self, str1, str2):
        count_str1 = {}
        count_str2 = {}

        if len(str1) != len(str2):
            return False
        
        for i in range(len(str1)):
            count_str1[str1[i]] = count_str1.get(str1[i], 0) + 1
            count_str2[str2[i]] = count_str2.get(str2[i], 0) + 1

        print(count_str1, count_str2)

        return count_str1 == count_str2
    
    def isAnagramWothASCI(self, str1, str2):
        if len(str1) != len(str2):
            return False
        
        count = [0] * 26
        for i in range(len(str1)):
            count[ord(str1[i]) - ord('a')] += 1
            count[ord(str2[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True