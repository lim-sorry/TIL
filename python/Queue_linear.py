Q = [0] * 100
front = rear = -1

def enQueue(item):
    global rear
    if rear == len(Q)-1:
        print('Queue Full')
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print('Queue Empty')
    else:
        front += 1
        return Q[front]

def Qpeek():
    if front == rear:
        print('Queue Empty')
    else:
        return Q[front+1]