class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i =="+" or i=="*" or i=="/" or i=="-":
                operand2=stack.pop()
                operand1=stack.pop()
                if i=="+":
                    stack.append(int(operand1)+int(operand2))
                if i=="-":
                    stack.append(int(operand1)-int(operand2))
                if i=="*":
                    stack.append(int(operand1)*int(operand2))
                if i=="/":
                    stack.append(int((int(operand1)/int(operand2))))
            else:
                stack.append(int(i))
        return stack[0]



