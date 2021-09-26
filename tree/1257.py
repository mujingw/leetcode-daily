from typing import List


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        region_to_parent = {}
        region1_ancestors = set()

        for region in regions:
            parent = region[0]

            for child in region[1:]:
                region_to_parent[child] = parent

        curr_region = region1

        while curr_region:
            region1_ancestors.add(curr_region)

            if curr_region not in region_to_parent:
                break
            else:
                curr_region = region_to_parent[curr_region]

        curr_region = region2

        while curr_region:
            if curr_region in region1_ancestors:
                return curr_region
            else:
                curr_region = region_to_parent[curr_region]
