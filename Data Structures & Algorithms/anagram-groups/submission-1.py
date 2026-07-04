from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_map=defaultdict(list)
        for string in strs:

            sorted_string="".join(sorted(string))


            word_map[sorted_string].append(string)

        return list(word_map.values())

        