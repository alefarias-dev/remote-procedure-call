from concurrent import futures
import server_pb2
import server_pb2_grpc
import grpc
import time
import numpy as np


class ServerServicer(server_pb2_grpc.ServerServicer):

    def voidFunction(self, request, context):
        # print('server received call for void')
        return server_pb2.void()

    def intArg(self, request, context):
        # print('server received {} [{}]'.format(type(request), request.integer))
        return server_pb2.Integer(integer=request.integer)

    def longArg(self, request, context):
        # print('server received {} [{}]'.format(type(request), request.longValue))
        return server_pb2.Long(longValue=request.longValue)

    def stringArg(self, request, context):
        # print('server received {} [{}]'.format(type(request), request.text))
        return server_pb2.String(text=request.text)

    def objectArg(self, request, context):
        # print('server received {} [{}]'.format(type(request), request))
        return server_pb2.Object(name=request.name, age=request.age, weight=request.weight)

    def stringListArg(self, request, context):
        # print('server received {} {}'.format(type(request), request.texts))
        return server_pb2.StringArray(texts=request.texts)

    def intArray(self, request, context):
        # print('server received {} {}'.format(type(request), request.numbers))
        return server_pb2.IntArray(numbers=request.numbers)

    def floatArray(self, request, context):
        # print('server received {} {}'.format(type(request), request.numbers))
        return server_pb2.FloatArray(numbers=request.numbers)

    def euclideanDistance(self, request, context):
        v = np.array(list(request.vectors[0].numbers));
        w = np.array(list(request.vectors[1].numbers));
        res = np.sqrt(np.sum((v-w))**2)
        return server_pb2.Float(num=float(res))


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