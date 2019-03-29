"""The Python implememntation of seans grpc client"""

import pingpong_pb2
import pingpong_pb2_grpc
import time
import grpc
import random
import threading

def run():
    counter = 0

    with grpc.insecure_channel("localhost:9999") as channel:
        stub = pingpong_pb2_grpc.PingPongServiceStub(channel)
        while True:
            try:
                start = time.time()
                response = stub.ping(pingpong_pb2.Ping(count=counter))
                counter = response.count
                if counter % 1000 == 0:
                    print("%.3f : resp: %s : %i" % (time.time() - start, response.count, threading.active_count()))
                    # counter = 0
                time.sleep(0.001)
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(close)                            
                exit()

def close(channel):
    channel.close()

# if __name__ == "__main__":
run()
