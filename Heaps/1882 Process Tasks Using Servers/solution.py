from typing import List

from heapq import heappop, heappush, nsmallest
from collections import deque, defaultdict


# class Solution:
#     def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
#         answer = []
#         available_servers = []
#         running_servers = []
#         for i, server in enumerate(servers):
#             heappush(available_servers, (server, i))
#         t = j = 0
#
#         while j < len(tasks):
#             if len(available_servers) == 0 or self.has_any_running_server_completed_execution(running_servers, t):
#                 task_execution_time, server_weight, server_index = heappop(running_servers)
#                 t = max(t, task_execution_time)
#                 heappush(available_servers, (server_weight, server_index))
#
#             server_weight, server_index = heappop(available_servers)
#             server_next_availability_time = t + tasks[j]
#             answer.append(server_index)
#             j += 1
#             heappush(running_servers, (server_next_availability_time, server_weight, server_index))
#             t += 1
#
#         return answer
#
#     def has_any_running_server_completed_execution(self, running_servers, t):
#         return len(running_servers) > 0 and nsmallest(1, running_servers)[0][0] <= t
#


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        answer = []
        available_servers = []
        running_servers = []
        for i, server in enumerate(servers):
            heappush(available_servers, (server, i))
        t = j = 0

        while j < len(tasks):
            while running_servers and running_servers[0][0] <= t:
                task_execution_time, server_weight, server_index = heappop(running_servers)
                heappush(available_servers, (server_weight, server_index))
            if len(available_servers) == 0:
                t = running_servers[0][0]
                continue
            server_weight, server_index = heappop(available_servers)
            server_next_availability_time = t + tasks[j]
            answer.append(server_index)
            j += 1
            heappush(running_servers, (server_next_availability_time, server_weight, server_index))
            t += 1

        return answer
