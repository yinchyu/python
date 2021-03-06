# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import receiver_pb2 as receiver__pb2


class ReceiverStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.receive = channel.unary_unary(
                '/Receiver/receive',
                request_serializer=receiver__pb2.Event.SerializeToString,
                response_deserializer=receiver__pb2.Reply.FromString,
                )
        self.receive2 = channel.unary_unary(
                '/Receiver/receive2',
                request_serializer=receiver__pb2.Event.SerializeToString,
                response_deserializer=receiver__pb2.Reply.FromString,
                )


class ReceiverServicer(object):
    """Missing associated documentation comment in .proto file."""

    def receive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def receive2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReceiverServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'receive': grpc.unary_unary_rpc_method_handler(
                    servicer.receive,
                    request_deserializer=receiver__pb2.Event.FromString,
                    response_serializer=receiver__pb2.Reply.SerializeToString,
            ),
            'receive2': grpc.unary_unary_rpc_method_handler(
                    servicer.receive2,
                    request_deserializer=receiver__pb2.Event.FromString,
                    response_serializer=receiver__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Receiver', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Receiver(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def receive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Receiver/receive',
            receiver__pb2.Event.SerializeToString,
            receiver__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def receive2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Receiver/receive2',
            receiver__pb2.Event.SerializeToString,
            receiver__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
