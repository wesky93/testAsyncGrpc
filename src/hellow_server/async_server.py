import argparse
import asyncio
# generated by protoc
import logging

import helloworld_grpc
import helloworld_pb2
from grpclib.server import Server
from grpclib.utils import graceful_exit


class Greeter(helloworld_grpc.GreeterBase):

    async def SayHello(self, stream):
        request = await stream.recv_message()
        message = f'Hello, {request.name}!'
        print(message)
        await stream.send_message(helloworld_pb2.HelloReply(message=message))


async def main(*, host='127.0.0.1', port=50051):
    server = Server([Greeter()])
    with graceful_exit([server]):
        await server.start(host, port)
        print(f'Serving on {host}:{port}')
        await server.wait_closed()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--loop', '-l', type=str,  dest='loop', default='asyncio')
    return parser.parse_args()


if __name__ == '__main__':
    logging.basicConfig()
    args = get_args()
    if args.loop == 'uvloop':
        import uvloop

        uvloop.install()
    asyncio.run(main())
