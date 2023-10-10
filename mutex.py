import threading

lock = threading.Lock()
condition = [threading.Condition() for _ in range(3)]
count = 0

def print_thread_id(id, target):
    global count
    for _ in range(target):
        with condition[id - ord('A')]:
            while id - ord('A') != (count + 2) % 3:
                condition[id - ord('A')].wait()
            print(chr(id), end="")
            count += 1
            condition[(count + 2) % 3].notify_all()

def main():
    target = 1000
    threadA = threading.Thread(target=print_thread_id, args=('A', target))
    threadB = threading.Thread(target=print_thread_id, args=('B', target))
    threadC = threading.Thread(target=print_thread_id, args=('C', target))

    threadA.start()
    threadB.start()
    threadC.start()

    threadA.join()
    threadB.join()
    threadC.join()

    print()

if __name__ == "__main__":
    main()
