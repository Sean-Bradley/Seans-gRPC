"""The Python implementation of the GRPC Seans-gRPC server."""
from concurrent import futures
import threading
import time
import grpc
import pingpong_pb2
import pingpong_pb2_grpc

class Listener(pingpong_pb2_grpc.PingPongServiceServicer):
    """The listener function implemests the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()

    def __str__(self):
        return self.__class__.__name__

    def ping(self, request, context):
        self.counter += 1
        if self.counter > 10000:
            print("10000 calls in %3f seconds" % (time.time() - self.last_print_time))
            self.last_print_time = time.time()
            self.counter = 0
        return pingpong_pb2.Pong(count=request.count + 1)


def serve():
    """The main serve function of the server.
    This opens the socket, and listens for incoming grpc conformant packets"""

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pingpong_pb2_grpc.add_PingPongServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    serve()
