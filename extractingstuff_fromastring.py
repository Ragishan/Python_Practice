class Solution:
    def repeatedchar(self, s: str) -> str:
        occurences = defaultdict(int)
        for char in s:
            occurences[char] += 1
            if occurences[char] == 2:
                return char
    
    repeatedchar("awccx")