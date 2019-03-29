from multiprocessing import Process
import client as client

if __name__ == "__main__":
    count = 2
    processes = {}
    for x in range(count):
        processes[x] = Process(target=client.run)

    for x in range(count):
        processes[x].start()

