# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from Protobuf import message_pb2 as Protobuf_dot_message__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OnLamp = channel.unary_unary(
                '/SmartOffice.Greeter/OnLamp',
                request_serializer=Protobuf_dot_message__pb2.Request.SerializeToString,
                response_deserializer=Protobuf_dot_message__pb2.Response.FromString,
                )
        self.OffLamp = channel.unary_unary(
                '/SmartOffice.Greeter/OffLamp',
                request_serializer=Protobuf_dot_message__pb2.Request.SerializeToString,
                response_deserializer=Protobuf_dot_message__pb2.Response.FromString,
                )
        self.OnHumid = channel.unary_unary(
                '/SmartOffice.Greeter/OnHumid',
                request_serializer=Protobuf_dot_message__pb2.Request.SerializeToString,
                response_deserializer=Protobuf_dot_message__pb2.Response.FromString,
                )
        self.OffHumid = channel.unary_unary(
                '/SmartOffice.Greeter/OffHumid',
                request_serializer=Protobuf_dot_message__pb2.Request.SerializeToString,
                response_deserializer=Protobuf_dot_message__pb2.Response.FromString,
                )
        self.OnAirCond = channel.unary_unary(
                '/SmartOffice.Greeter/OnAirCond',
                request_serializer=Protobuf_dot_message__pb2.Request.SerializeToString,
                response_deserializer=Protobuf_dot_message__pb2.Response.FromString,
                )
        self.OffAirCond = channel.unary_unary(
                '/SmartOffice.Greeter/OffAirCond',
                request_serializer=Protobuf_dot_message__pb2.Request.SerializeToString,
                response_deserializer=Protobuf_dot_message__pb2.Response.FromString,
                )


class GreeterServicer(object):
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

    def OnAirCond(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OffAirCond(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OnLamp': grpc.unary_unary_rpc_method_handler(
                    servicer.OnLamp,
                    request_deserializer=Protobuf_dot_message__pb2.Request.FromString,
                    response_serializer=Protobuf_dot_message__pb2.Response.SerializeToString,
            ),
            'OffLamp': grpc.unary_unary_rpc_method_handler(
                    servicer.OffLamp,
                    request_deserializer=Protobuf_dot_message__pb2.Request.FromString,
                    response_serializer=Protobuf_dot_message__pb2.Response.SerializeToString,
            ),
            'OnHumid': grpc.unary_unary_rpc_method_handler(
                    servicer.OnHumid,
                    request_deserializer=Protobuf_dot_message__pb2.Request.FromString,
                    response_serializer=Protobuf_dot_message__pb2.Response.SerializeToString,
            ),
            'OffHumid': grpc.unary_unary_rpc_method_handler(
                    servicer.OffHumid,
                    request_deserializer=Protobuf_dot_message__pb2.Request.FromString,
                    response_serializer=Protobuf_dot_message__pb2.Response.SerializeToString,
            ),
            'OnAirCond': grpc.unary_unary_rpc_method_handler(
                    servicer.OnAirCond,
                    request_deserializer=Protobuf_dot_message__pb2.Request.FromString,
                    response_serializer=Protobuf_dot_message__pb2.Response.SerializeToString,
            ),
            'OffAirCond': grpc.unary_unary_rpc_method_handler(
                    servicer.OffAirCond,
                    request_deserializer=Protobuf_dot_message__pb2.Request.FromString,
                    response_serializer=Protobuf_dot_message__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SmartOffice.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
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
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Greeter/OnLamp',
            Protobuf_dot_message__pb2.Request.SerializeToString,
            Protobuf_dot_message__pb2.Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Greeter/OffLamp',
            Protobuf_dot_message__pb2.Request.SerializeToString,
            Protobuf_dot_message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Greeter/OnHumid',
            Protobuf_dot_message__pb2.Request.SerializeToString,
            Protobuf_dot_message__pb2.Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Greeter/OffHumid',
            Protobuf_dot_message__pb2.Request.SerializeToString,
            Protobuf_dot_message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnAirCond(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Greeter/OnAirCond',
            Protobuf_dot_message__pb2.Request.SerializeToString,
            Protobuf_dot_message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OffAirCond(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Greeter/OffAirCond',
            Protobuf_dot_message__pb2.Request.SerializeToString,
            Protobuf_dot_message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)