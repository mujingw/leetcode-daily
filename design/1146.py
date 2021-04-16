from bisect import bisect_left
from collections import defaultdict


class SnapshotArray:

    def __init__(self, length: int):
        self.array = defaultdict(lambda: defaultdict(int))
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index][self.snap_id] = val

    def snap(self) -> int:
        snap_id = self.snap_id
        self.snap_id += 1

        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.array[index]:
            return self.array[index][snap_id]

        sorted_snap_ids = sorted(self.array[index].keys())
        idx = bisect_left(sorted_snap_ids, snap_id)
        most_recent_snap_id = sorted_snap_ids[idx - 1] if idx > 0 else 0

        return self.array[index][most_recent_snap_id]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
