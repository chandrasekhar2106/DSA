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

            