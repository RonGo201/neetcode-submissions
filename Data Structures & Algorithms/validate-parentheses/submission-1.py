class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char in "({[":
                st.append(char)
            
            elif not st:
                return False
            
            elif (char == ")" and st.pop() != "(" or 
                    char == "}" and st.pop() != "{" or 
                    char == "]" and st.pop() != "["):
                        return False
        if st:
            return False

        return True        