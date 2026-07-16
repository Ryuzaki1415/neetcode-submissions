class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freqmap = {}
        counts = {"b":1,"a":1,"l":2,"o":2,"n":1}

        for char in text:
            if char in counts:
                freqmap[char] = freqmap.get(char, 0) + 1

        count = float("inf")
        for key in counts:
            if key not in freqmap:
                return 0 #if any one is missing then we cannot make the word balloon
            count = min(count, freqmap[key] // counts[key])

        return count