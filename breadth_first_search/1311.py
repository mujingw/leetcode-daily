from collections import defaultdict, deque
from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], my_id: int,
                               level: int) -> List[str]:
        q = deque([(my_id, 0)])
        level_k_movies = defaultdict(int)
        seen = set([my_id])

        while q:
            curr, lvl = q.popleft()

            if lvl == level:
                for video in watchedVideos[curr]:
                    level_k_movies[video] += 1

            if lvl > level:
                break

            for friend in friends[curr]:
                if friend not in seen:
                    seen.add(friend)
                    q.append((friend, lvl + 1))

        return [x[0] for x in sorted(list(level_k_movies.items()), key=lambda x: (x[1], x[0]))]
