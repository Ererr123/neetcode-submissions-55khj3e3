class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        hashmap = defaultdict(list)

        for s in strs:
            # Count frequency of each letter
            count = [0] * 26  # 'a' to 'z'
            for char in s:
                count[ord(char) - ord('a')] += 1

            # Convert list to tuple (immutable) to use as dict key
            key = tuple(count)
            hashmap[key].append(s)

        return list(hashmap.values())