from typing import List
from heapq import heappush, heappop


class Solution:
    # def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    #     trips.sort(key=lambda x: x[1])
    #
    #     num_passengers, start, end = 0, 1, 2
    #     min_heap = []
    #
    #     for trip in trips:
    #         while min_heap and min_heap[0][0] <= trip[start]:
    #             trip_end, trip_num_passengers = heappop(min_heap)
    #             capacity += trip_num_passengers
    #
    #         if capacity >= trip[num_passengers]:
    #             capacity -= trip[num_passengers]
    #         else:
    #             return False
    #         heappush(min_heap, (trip[end], trip[num_passengers]))
    #     return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0] * 1001
        for trip in trips:
            path[trip[1]] = path[trip[1]] + trip[0]
            path[trip[2]] = path[trip[2]] -trip[0]

        for passenger in path:
            capacity -= passenger
            if capacity < 0:
                return False
        return True
