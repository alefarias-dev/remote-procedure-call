import server_pb2
import server_pb2_grpc
import grpc
import time
import numpy as np
import pandas as pd

class Object:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


def run():

    host = input("Host: ")
    channel = grpc.insecure_channel(host+':50051')
    stub = server_pb2_grpc.ServerStub(channel)

    # auxiliar data structures
    stringList = ['abcd' for i in range(200)]
    numbers = [32 for i in range(200)]
    float_numbers = [2.5 for i in range(200)]
    vector1 = server_pb2.FloatArray(numbers=[15.63,1.65,0.69])
    vector2 = server_pb2.FloatArray(numbers=[15.10,1.25,0.89])

    n_tests = 1024

    void_times = []
    for i in range(n_tests):
        s = time.time()
        stub.voidFunction(server_pb2.void())  # void function
        e = time.time()
        void_times.append(e-s)

    int_arg_times = []
    for i in range(n_tests):
        s = time.time()
        stub.intArg(server_pb2.Integer(integer=10))  # int arg
        e = time.time()
        int_arg_times.append(e-s)

    long_arg_times = []
    for i in range(n_tests):
        s = time.time()
        stub.longArg(server_pb2.Long(longValue=665656565656565))  # long arg
        e = time.time()
        long_arg_times.append(e-s)

    string_arg_times = []
    for i in range(n_tests):
        s = time.time()
        stub.stringArg(server_pb2.String(text="This is Sparta!!!"))  # string arg
        e = time.time()
        string_arg_times.append(e-s)

    string_array_times = []
    for i in range(n_tests):
        s = time.time()
        stub.stringListArg(server_pb2.StringArray(texts=stringList))  # string array
        e = time.time()
        string_array_times.append(e-s)

    int_array_times = []
    for i in range(n_tests):
        s = time.time()
        stub.intArray(server_pb2.IntArray(numbers=numbers))  # int array
        e = time.time()
        int_array_times.append(e-s)

    float_array_times = []
    for i in range(n_tests):
        s = time.time()
        stub.floatArray(server_pb2.FloatArray(numbers=float_numbers))  # float array
        e = time.time()
        float_array_times.append(e-s)

    object_arg_times = []
    for i in range(n_tests):
        s = time.time()
        stub.objectArg(server_pb2.Object(name='alexandre', age=10, weight=72.5))  # passing object
        e = time.time()
        object_arg_times.append(e-s)

    euclidian_times = []
    for i in range(n_tests):
        s = time.time()
        stub.euclideanDistance(server_pb2.EuclidianVectors(vectors=[vector1,vector2]))  # euclidian distance
        e = time.time()
        euclidian_times.append(e-s)

    void_times         = np.array(void_times)
    int_arg_times      = np.array(int_arg_times)
    long_arg_times     = np.array(long_arg_times)
    string_arg_times   = np.array(string_arg_times)
    int_array_times    = np.array(int_array_times)
    float_array_times  = np.array(float_array_times)
    string_array_times = np.array(string_array_times)
    object_arg_times   = np.array(object_arg_times)
    euclidian_times    = np.array(euclidian_times)

    print('void_times mean time: {}'.format(np.sum(void_times)/len(void_times)))
    print('int_arg_times mean time: {}'.format(np.sum(int_arg_times)/len(int_arg_times)))
    print('long_arg_times mean time: {}'.format(np.sum(long_arg_times)/len(long_arg_times)))
    print('string_arg_times mean time: {}'.format(np.sum(string_arg_times)/len(string_arg_times)))
    print('int_array_times mean time: {}'.format(np.sum(int_array_times)/len(int_array_times)))
    print('float_array_times mean time: {}'.format(np.sum(float_array_times)/len(float_array_times)))
    print('string_array_times mean time: {}'.format(np.sum(string_array_times)/len(string_array_times)))
    print('object_arg_times mean time: {}'.format(np.sum(object_arg_times)/len(object_arg_times)))
    print('euclidean_times mean time: {}'.format(np.sum(euclidian_times)/len(euclidian_times)))

    df = pd.DataFrame({'void':void_times,
                       'int_arg':int_arg_times,
                       'long_arg':long_arg_times,
                       'string_arg':string_arg_times,
                       'int_array':int_array_times,
                       'float_array':float_array_times,
                       'string_array':string_array_times,
                       'object_arg':object_arg_times,
                       'euclidean_arg':euclidian_times})
    df.to_csv('grpc_metrics_'+host+'.csv', index=False)
    print('client finished...')

if __name__ == '__main__':
    run()