import asyncio
import logging

import AwsAPI_pb2
import AwsAPI_pb2_grpc_aio as AwsAPI_pb2_grpc
import aioboto3
from grpc.experimental import aio as grpc


class S3(AwsAPI_pb2_grpc.S3Servicer):

    async def GetObjects(self, request, context):
        total_count = 0
        session = aioboto3.Session()
        print(request, context)
        request = await  context.read()
        async with session.resource('s3') as s3resource:
            bucket = await s3resource.Bucket(request.bucket)
            async for obj in bucket.objects.all():
                e_tag = await  obj.e_tag
                print(obj.key, e_tag)
                total_count += 1

        print(total_count)
        await context.write(AwsAPI_pb2.ObjectReply(count=total_count))


async def serve():
    server = grpc.server()
    AwsAPI_pb2_grpc.add_S3Servicer_to_server(S3(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print('run server port 50051')
    await  server.wait_for_termination()


# def get_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--workers', '-w', type=int, required=True, dest='workers')
#
#     return parser.parse_args()


if __name__ == '__main__':
    logging.basicConfig()
    # args = get_args()
    grpc.init_grpc_aio()
    asyncio.run(serve())
