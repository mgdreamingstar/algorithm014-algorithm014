import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = collections.defaultdict(list)
        for s in strs:
            hash_map[''.join(sorted(s))].append(s)
        return list(hash_map.values())