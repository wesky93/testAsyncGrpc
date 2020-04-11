import asyncio

# generated by protoc
import helloworld_pb2
import helloworld_grpc
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


if __name__ == '__main__':
    asyncio.run(main())