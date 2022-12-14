# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Protobuf.lamp_pb2 as lamp__pb2


class LampStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OnOffLamp = channel.unary_unary(
                '/SmartOffice.Lamp/OnOffLamp',
                request_serializer=lamp__pb2.RequestLamp.SerializeToString,
                response_deserializer=lamp__pb2.ResponseLamp.FromString,
                )
        self.GetLampInfo = channel.unary_unary(
                '/SmartOffice.Lamp/GetLampInfo',
                request_serializer=lamp__pb2.RequestLamp.SerializeToString,
                response_deserializer=lamp__pb2.ResponseLamp.FromString,
                )
        self.OnOffLuminositySensor = channel.unary_unary(
                '/SmartOffice.Lamp/OnOffLuminositySensor',
                request_serializer=lamp__pb2.RequestLamp.SerializeToString,
                response_deserializer=lamp__pb2.ResponseOnOffLuminositySensor.FromString,
                )


class LampServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OnOffLamp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLampInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnOffLuminositySensor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LampServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OnOffLamp': grpc.unary_unary_rpc_method_handler(
                    servicer.OnOffLamp,
                    request_deserializer=lamp__pb2.RequestLamp.FromString,
                    response_serializer=lamp__pb2.ResponseLamp.SerializeToString,
            ),
            'GetLampInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLampInfo,
                    request_deserializer=lamp__pb2.RequestLamp.FromString,
                    response_serializer=lamp__pb2.ResponseLamp.SerializeToString,
            ),
            'OnOffLuminositySensor': grpc.unary_unary_rpc_method_handler(
                    servicer.OnOffLuminositySensor,
                    request_deserializer=lamp__pb2.RequestLamp.FromString,
                    response_serializer=lamp__pb2.ResponseOnOffLuminositySensor.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SmartOffice.Lamp', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Lamp(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OnOffLamp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Lamp/OnOffLamp',
            lamp__pb2.RequestLamp.SerializeToString,
            lamp__pb2.ResponseLamp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLampInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Lamp/GetLampInfo',
            lamp__pb2.RequestLamp.SerializeToString,
            lamp__pb2.ResponseLamp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnOffLuminositySensor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmartOffice.Lamp/OnOffLuminositySensor',
            lamp__pb2.RequestLamp.SerializeToString,
            lamp__pb2.ResponseOnOffLuminositySensor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
