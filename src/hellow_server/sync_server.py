import argparse
import logging
from concurrent import futures

import grpc

try:
    import helloworld_pb2
    import helloworld_pb2_grpc
except Exception as _:
    from . import helloworld_pb2
    from . import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print(f'Hello, {request.name}!')
        return helloworld_pb2.HelloReply(message=f'Hello, {request.name}!')


def serve(workers: int):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=workers))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('run server port 50051')
    server.wait_for_termination()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', '-w', type=int, required=True, dest='workers')

    return parser.parse_args()


if __name__ == '__main__':
    logging.basicConfig()
    args = get_args()
    serve(args.workers)
