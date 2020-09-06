N = 4
Q = [0] * N
front = rear = 0

def enQueue(item):
    global rear
    if (rear+1)%N == front:
        print('Queue Full')
    else:
        rear = (rear+1)%N
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print('Queue Empty')
    else:
        front = (front+1)%N
        return Q[front]

def Qpeek():
    if front == rear:
        print('Queue Empty')
    else:
        return Q[(front+1)%N]