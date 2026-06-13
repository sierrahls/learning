class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2]) #add sum of the last elements
            elif op == "D":
                stack.append(stack[-1] * 2) #double to allocate more space
            elif op == "C": #remove
                stack.pop()
            else:
                stack.append(int(op))
    
        return sum(stack) #sum function