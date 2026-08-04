class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_arr = sorted(zip(position, speed), reverse=True)
        st = []
        for car in sorted_arr:
            p1, s1 = car[0], car[1]
            time1 = (target - p1) / s1

            if not st:
                st.append(time1)
                continue

            time2 = st[-1]

            if time1 > time2:
                st.append(time1)
        
        return len(st)
            