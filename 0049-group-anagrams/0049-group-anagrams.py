class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for i in strs:
            word = ''.join(sorted(i))
            print(word,i)
            anagrams[word].append(i)
        return anagrams.values()
        