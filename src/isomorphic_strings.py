class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):

        if len(s) != len(t):
            return False

        charDict = {}
        for i, c in enumerate(s):
            if c not in charDict.keys() and t[i] not in charDict.values():
                charDict[c] = t[i]
            elif t[i] in charDict.values() or charDict[c] != t[i]:
                return False
        return True

if __name__ == '__main__':
    test_list = [["ab","aa"],["aa", "bb"]
    result_list = [False, True]
    success = True
    solution = Solution()
    for i, s in enumerate(test_list):
        result = solution.isIsomorphic(s[0], s[1])
        if result != result_list[i]:
            success = False
            print s
            print 'Expected value', result_list[i]
            print 'Actual value', result
    if success:
        print 'All the tests passed.'
    else:
        print 'Please fix the failed test'
