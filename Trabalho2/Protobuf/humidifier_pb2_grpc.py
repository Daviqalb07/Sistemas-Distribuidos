# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import humidifier_pb2 as humidifier__pb2


class HumidifierStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OnHumid = channel.unary_unary(
                '/SmartOffice.Humidifier/OnHumid',
                request_serializer=humidifier__pb2.Request.SerializeToString,
                response_deserializer=humidifier__pb2.Response.FromString,
                )
        self.OffHumid = channel.unary_unary(
                '/SmartOffice.Humidifier/OffHumid',
                request_serializer=humidifier__pb2.Request.SerializeToString,
                response_deserializer=humidifier__pb2.Response.FromString,
                )
        self.ChangeVelocity = channel.unary_unary(
                '/SmartOffice.Humidifier/ChangeVelocity',
                request_serializer=humidifier__pb2.Request.SerializeToString,
                response_deserializer=humidifier__pb2.Response.FromString,
                )


class HumidifierServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OnHumid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OffHumid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeVelocity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HumidifierServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OnHumid': grpc.unary_unary_rpc_method_handler(
                    servicer.OnHumid,
                    request_deserializer=humidifier__pb2.Request.FromString,
                    response_serializer=humidifier__pb2.Response.SerializeToString,
            ),
            'OffHumid': grpc.unary_unary_rpc_method_handler(
                    servicer.OffHumid,
                    request_deserializer=humidifier__pb2.Request.FromString,
                    response_serializer=humidifier__pb2.Response.SerializeToString,
            ),
            'ChangeVelocity': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeVelocity,
                    request_deserializer=humidifier__pb2.Request.FromString,
                    response_serializer=humidifier__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SmartOffice.Humidifier', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Humidifier(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OnHumid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Humidifier/OnHumid',
            humidifier__pb2.Request.SerializeToString,
            humidifier__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OffHumid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Humidifier/OffHumid',
            humidifier__pb2.Request.SerializeToString,
            humidifier__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeVelocity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Humidifier/ChangeVelocity',
            humidifier__pb2.Request.SerializeToString,
            humidifier__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
