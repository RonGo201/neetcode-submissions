class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token not in "+-*/":
                st.append(token)
                continue
            
            b = int(st.pop())
            a = int(st.pop())
            if token == "+":
                st.append(a + b)
            elif token == "-":
                st.append(a - b)
            elif token == "*":
                st.append(a * b)
            elif token == "/":
                st.append(int(a / b))

        return int(st.pop())