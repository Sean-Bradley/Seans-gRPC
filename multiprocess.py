from multiprocessing import Process
import time
import client

if __name__ == '__main__':
    # freeze_support()   #only needed if creating a stand alone executable
    time1 = time.time()
    p1 = Process(target=client, args=([38]))
    p2 = Process(target=client, args=([38]))
    p3 = Process(target=client, args=([38]))
    p4 = Process(target=client, args=([38]))
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    print("p1 joined")
    p2.join()
    print("p2 joined")
    p3.join()
    print("p3 joined")
    p4.join()
    print("p4 joined")

    time2 = time.time()
    print("finished")
    print(f"{time2-time1} seconds")