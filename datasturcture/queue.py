# -*- coding: utf-8 -*-


class MyQueue:

    def __init__(self):
        self.MAX_SIZE = 10
        self.list = [0 * self.MAX_SIZE]
        self.head = 0
        self.tail = 0

    def enqueue(self, elem):
        if len(self.list) >= self.MAX_SIZE:
            return

        self.list.append(elem)
        self.tail += 1

    def dequeue(self) -> int:
        if self.head == self.tail:
            return -1

        popped = self.list[self.head]
        self.head += 1
        return popped

