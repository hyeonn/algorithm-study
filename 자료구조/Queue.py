# Queue <= FIFO (선입선출)

class Queue():
    def __init__(self):
        self.queue = []

    # 데이터 삽입
    def enqueue(self, data):
        self.queue.append(data)

    # 데이터 삭제
    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            dequeue_object = self.queue[0]
            self.queue = self.queue[1:]
        return dequeue_object

    # 가장 첫번째 값 출력
    def peek(self):
        peek_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            peek_object = self.queue[0]
        return peek_object

    # 비어있는지 확인
    def isEmpty(self):
        is_empty = False
        if len(self.queue) == 0:
            is_empty = True
        return is_empty
