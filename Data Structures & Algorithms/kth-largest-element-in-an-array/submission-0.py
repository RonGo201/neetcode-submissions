import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapLen = 0

        for num in nums:
            if heapLen < k:
                heapq.heappush(heap, num)
                heapLen += 1
            
            elif heapLen == k and num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]