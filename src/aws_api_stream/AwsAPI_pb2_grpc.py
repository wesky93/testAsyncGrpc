# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import AwsAPI_pb2 as AwsAPI__pb2


class S3Stub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetObjects = channel.unary_stream(
                '/AwsAPI.S3/GetObjects',
                request_serializer=AwsAPI__pb2.GetObjectsRequest.SerializeToString,
                response_deserializer=AwsAPI__pb2.ObjectReply.FromString,
                )


class S3Servicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetObjects(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_S3Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetObjects': grpc.unary_stream_rpc_method_handler(
                    servicer.GetObjects,
                    request_deserializer=AwsAPI__pb2.GetObjectsRequest.FromString,
                    response_serializer=AwsAPI__pb2.ObjectReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AwsAPI.S3', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class S3(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetObjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/AwsAPI.S3/GetObjects',
            AwsAPI__pb2.GetObjectsRequest.SerializeToString,
            AwsAPI__pb2.ObjectReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
