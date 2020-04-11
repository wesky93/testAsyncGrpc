import argparse
import logging
from concurrent import futures

import AwsAPI_pb2
import AwsAPI_pb2_grpc
import boto3
import grpc



class S3(AwsAPI_pb2_grpc.S3Servicer):

    def GetObjects(self, request, context):
        session = boto3.Session()
        s3resource = session.resource('s3')
        bucket = s3resource.Bucket(request.bucket)
        for obj in bucket.objects.all():
            yield AwsAPI_pb2.ObjectReply(name=obj.key,etag=obj.e_tag)


def serve(workers:int):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=workers))
    AwsAPI_pb2_grpc.add_S3Servicer_to_server(S3(), server)
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