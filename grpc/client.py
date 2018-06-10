import server_pb2
import server_pb2_grpc
import grpc


class Object:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = server_pb2_grpc.ServerStub(channel)

    stringList = ['Alexandre', 'Farias', 'Santos']
    numbers = [1,2,3,4,5,6,7,8,9]
    float_numbers = [0.13, 0.72, 0.35, 0.43, 0.52]

    stub.voidFunction(server_pb2.void())  # void function
    stub.intArg(server_pb2.Integer(integer=10))  # int arg
    stub.longArg(server_pb2.Long(longValue=665656565656565))  # long arg
    stub.stringArg(server_pb2.String(text="This is Sparta!!!"))  # string arg
    stub.stringListArg(server_pb2.StringArray(texts=stringList))  # string array
    stub.intArray(server_pb2.IntArray(numbers=numbers))  # int array
    stub.floatArray(server_pb2.FloatArray(numbers=float_numbers))  # float array
    stub.objectArg(server_pb2.Object(name='alexandre', age=10, weight=72.5))  # passing object

    vector1 = server_pb2.FloatArray(numbers=[15.63,1.65,0.69])
    vector2 = server_pb2.FloatArray(numbers=[15.10,1.25,0.89])
    dist = stub.euclideanDistance(server_pb2.EuclidianVectors(vectors=[vector1,vector2]))  # euclidian distance
    print('euclidian distance calculated by the server: {}'.format(dist.num))
    print('client finished...')


if __name__ == '__main__':
    run()