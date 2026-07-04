class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        """
        We need to group anagrams together.
        Anagrams contain the same count of letters.
        if we sort anagrams, they will be same.
        we can also store the freq count of these in a dictonary
        """

        word_map=defaultdict(list)
        for string in strs:
            # lets sort and store as a key

            sorted_string="".join(sorted(string)) # sorted (string) turns it into a list and we basically join that list.

            # lets store this key

            word_map[sorted_string].append(string)

        return list(word_map.values())




        