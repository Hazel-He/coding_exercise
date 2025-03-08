"""
LeetCode 332: https://leetcode.cn/problems/reconstruct-itinerary/description/
对每个机场的到达机场进行排序，保证我们按照字典序进行遍历
建立一个哈希表，map<出发机场, map<到达机场, 航班次数>>
如果“航班次数”大于零，说明目的地还可以飞，如果“航班次数”等于零说明目的地不能飞了，而不用对集合做删除元素或者增加元素的操作。
注意函数返回值我用的是bool！
我们之前讲解回溯算法的时候，一般函数返回值都是void，这次为什么是bool呢？
因为我们只需要找到一个行程，就是在树形结构中唯一的一条通向叶子节点的路线
所以找到了这个叶子节点了直接返回，不需要再继续遍历了
Return True when we find a valid itinerary (when we've used all tickets)
Return False when we can't find a valid path from the current state
"""


from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Sort the destinations to ensure we try them in lexicographical order
        tickets.sort(key=lambda x: x[1])
        depa_arri = {}
        for ticket in tickets:
            depa = ticket[0]
            arri = ticket[1]
            if depa not in depa_arri:
                depa_arri[depa] = {}

            if arri not in depa_arri[depa]:
                depa_arri[depa][arri] = 1
            else:
                depa_arri[depa][arri] = depa_arri[depa][arri] + 1

        res = ["JFK"]

        def backtrack(res):
            if len(res) == len(tickets) + 1:
                return True
            # Handle case where current airport has no outgoing flights
            if res[-1] not in depa_arri:
                return False

            for arri, value in depa_arri[res[-1]].items():
                if value <= 0:
                    continue
                depa_arri[res[-1]][arri] = depa_arri[res[-1]][arri] - 1
                res.append(arri)
                if backtrack(res):
                    return True
                res.pop()
                depa_arri[res[-1]][arri] = depa_arri[res[-1]][arri] + 1

        backtrack(res)
        return res