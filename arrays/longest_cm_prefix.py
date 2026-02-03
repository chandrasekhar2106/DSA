class LongestCommonPrefix:

    def horizantal_scan(self, array):
        prefix = array[0]

        for i in range(1, len(array)):
            j = 0
            while j < min(len(prefix), len(array[i])):
                if prefix[j] != array[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
    
    def vertical_scan(self, array):
        for i in range(len(array[0])):
            for s in array:
                if i == len(s) or (i >= len(array[0]) and s[i] != s[0][i]):
                    return s[:i]
        return array[0]