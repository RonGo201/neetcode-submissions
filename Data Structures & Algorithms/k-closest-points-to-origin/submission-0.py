import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapLen = 0

        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            
            if heapLen < k:
                heapq.heappush(maxHeap, (-1 * dist, point))
                heapLen += 1

            elif heapLen == k and dist < -1 * maxHeap[0][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-1 * dist, point))

        return [item[1] for item in maxHeap]