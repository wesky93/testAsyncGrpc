import logging
from concurrent import futures

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print(f'Hello, {request.name}!')
        return helloworld_pb2.HelloReply(message=f'Hello, {request.name}!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('run server port 50051')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
