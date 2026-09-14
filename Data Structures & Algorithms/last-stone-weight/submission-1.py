import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -1 * stone)
        
        newLen = len(maxHeap)
        while newLen > 1:
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, -1 * (x - y))
                newLen -= 1
            else:
                newLen -= 2
        
        if newLen == 1:
            return -1 * maxHeap[0]
        else:
            return 0