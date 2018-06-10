from concurrent import futures
import server_pb2
import server_pb2_grpc
import grpc
import time


class ServerServicer(server_pb2_grpc.ServerServicer):

    def voidFunction(self, request, context):
        return server_pb2.void()

    def intArg(self, request, context):
        print('server received {} [{}]'.format(type(request), request.integer))
        return server_pb2.void()

    def longArg(self, request, context):
        print('server received {} [{}]'.format(type(request), request.longValue))
        return server_pb2.void()

    def stringArg(self, request, context):
        print('server received {} [{}]'.format(type(request), request.text))
        return server_pb2.void()

    def objectArg(self, request, context):
        print('server received {} [{}]'.format(type(request), request))
        return server_pb2.Object()

    def stringListArg(self, request, context):
        print('server received {} {}'.format(type(request), request.texts))
        return server_pb2.void()

    def intArray(self, request, context):
        print('server received {} {}'.format(type(request), request.numbers))
        return server_pb2.void()

    def floatArray(self, request, context):
        print('server received {} {}'.format(type(request), request.numbers))
        return server_pb2.void()

    def euclideanDistance(self, request, context):
        print(request)
        return server_pb2.Float(num=.1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_ServerServicer_to_server(ServerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('service listening')
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()