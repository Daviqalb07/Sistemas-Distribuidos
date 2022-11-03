# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import lamp_pb2 as lamp__pb2


class LampStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OnLamp = channel.unary_unary(
                '/SmartOffice.Lamp/OnLamp',
                request_serializer=lamp__pb2.Request.SerializeToString,
                response_deserializer=lamp__pb2.Response.FromString,
                )
        self.OffLamp = channel.unary_unary(
                '/SmartOffice.Lamp/OffLamp',
                request_serializer=lamp__pb2.Request.SerializeToString,
                response_deserializer=lamp__pb2.Response.FromString,
                )


class LampServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OnLamp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OffLamp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LampServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OnLamp': grpc.unary_unary_rpc_method_handler(
                    servicer.OnLamp,
                    request_deserializer=lamp__pb2.Request.FromString,
                    response_serializer=lamp__pb2.Response.SerializeToString,
            ),
            'OffLamp': grpc.unary_unary_rpc_method_handler(
                    servicer.OffLamp,
                    request_deserializer=lamp__pb2.Request.FromString,
                    response_serializer=lamp__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SmartOffice.Lamp', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Lamp(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OnLamp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Lamp/OnLamp',
            lamp__pb2.Request.SerializeToString,
            lamp__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OffLamp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Lamp/OffLamp',
            lamp__pb2.Request.SerializeToString,
            lamp__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
