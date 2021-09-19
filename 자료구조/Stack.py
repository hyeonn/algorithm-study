# Stack <= LIFO (후입선출)

class Stack():
    def __init__(self):
        self.stack = []
    # 데이터 삽입
    def push(self, data):
        self.stack.append(data)

    # 데이터 꺼내기
    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.stack.pop()
        return pop_object

    # 맨 위 원소 반환
    def top(self):
        top_object = None
        if self.isEmpty(): 
            print("Stack is Empty")
        else:
            top_object = self.stack[-1]
        return top_object

    # 스택이 비었는지 확인
    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty
