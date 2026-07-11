from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            keys = ''.join(sorted(str))
            groups[keys].append(str)

        return list(groups.values())
   