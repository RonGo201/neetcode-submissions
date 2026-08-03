class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while st:
                t = st[-1][1]
                if t >= temp:
                    break
                else:
                    i, t = st.pop()
                    res[i] = index - i
            st.append((index, temp))
                
        while st:
            i = st.pop()[0]
            res[i] = 0
        
        return res