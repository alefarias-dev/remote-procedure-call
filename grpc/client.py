# -*- coding: utf-8 -*-
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

    # estruturas de dados auxiliares
    n_tests        = 512
    stringList     = ['abcdef' for i in range(200)]
    numbers       = [32 for i in range(200)]
    float_numbers = [2.5 for i in range(200)]
    array_1       = server_pb2.FloatArray(numbers=[15.63,1.65,0.69])
    array_2       = server_pb2.FloatArray(numbers=[15.10,1.25,0.89])
    boolean = True
    string_32 = "a0APw0Di2UpuX8q4Z1ha8QHSvRu7U3UV"
    string_512 = "wGKH8e8QCparhy8coSOiypTFHFHcyqoBDhGcIHfNZU2Va3KFsOHXGDn28sprlXDLAmMl4AGeZGN3cDpTzylNCEHiSiUGUleje" \
                 "s3Gf2Z6HtBrWw8dx3LEaofGF8pPXjuMk7Cc3QcpteXIBVhPOSe0yn2Ha6RDUxqLlucSGjswZTWgb8caMSp28KVznIgKqe7A4P" \
                 "zqomk8hW1083DwRz9f9C9siw7ge53dgIOMtpkPlPBSh8wQMGTnkPHadvzHKGn9Y6gWUiFmiXo32ORxByPoxfZnTg89Jh7dcs9" \
                 "nyeLWCVPOvyHtnSfG3XCDGW4avw2GCMMJ39sZxJT9JQSzuqVKrSkicHMZHSx5Ci8QMu3jlH5KoYsGCbXu8LcsFxLv98eQr0Ur" \
                 "9AuDW8vtGaNNztSmJthCUIyGZzve81B2gOKquNN4mFgr2eTD9O3OWMCP1b28CUEhYIjjMFjxnCyOymxrPSPQttFJCr9fgQKgZ" \
                 "eNYINaesBNfDBIZ8dUPZTq3gHhC"
    string_1024 = "gVlTFdMnWdPIZm8xNLlorSCf7muQDXTn0YKx0cAp9Qc1bKjLyQ4aGXOkxCsGqjkLu8u5RxeFMOTwTGYc0e01KBCddp6SPM" \
                  "FsO3tOLDWRDv8D9bLXdI6tab1DI8nr6RrDThIGljrNnnWwtPqnFwPUdzUX2fPfCRh8L8eUIY1Xwk7Sikm2hRcy8WDFegDr" \
                  "50pptaJvXgpCp7JogNFbLTDLuDKPz4zakxk2Xxvd6QumzYC9mIMicaMjrX07DllSq9I7BXf843BOFZKN7IYaQzF3xoDX8H" \
                  "30nTVc139pYyuxThEedFUX9Kef0s5LagLAPNvil3zUOFpfx4rYEbMG3XzLItZI5yAws7DLHCy6mV4S99qrVfZabWAVlSnI" \
                  "Q6q4E25eXtf1UuGj3Kh9tlDZcEo5fD4M18MVgd2KLP7DYp7H2SLY0meVE7Rlr8TrpkJGvSJCCWEhYCyOLe85i43KsX6SGC" \
                  "lsTflmgwbxrtxxUoO8ty1FgLlPmaqqzvNYjs7Ay79pfps2kYK4CBOhC2vEarkxihnNYyJLD7b918QD6qduDr6ALpJwJ8zJ" \
                  "tgaifDabexcqsbVAiQpisJ72ROsI4JqlGyw6M17sNDFqUAmWH5YW6bjpRMVtyW28Z4xAkwEM1woReDZIMapSF5T8a3a1yG" \
                  "LBDDAzGTnBLE9U77TM3dk85YDoIUdxSVzPGTGe1knOTQD7ShgmFnvEuuhvTY3QhUzGhFmfiSWmUlpQ9Fnpuf4idtXQnTNu" \
                  "2M4nL6eMeCbO2Ggjn1bQWtrnp6f9ma3Z9WBHAbWx7GLAlb9NV79ZHUnVonCSSfddDlY4qmohttERA3AdBz4s9cOIfGUUci" \
                  "IX5dUuR2QkU7XNfTxKXKpbLSSzreH8m2WuMCSwiEb63UqKphzQvK2xBwnMTyMqxoTgPBKb8x7r051YTwKWWfAJldsrIGnM" \
                  "XGiS1jRTcT7aKcCB9fL0Id0Zh7k3foLbamAnjYNnMADo3r7XLUtsvKujRUT6QnMNGRdh5zvyW6sSE7O9ulnx"

    # testes
    void_times = []
    for i in range(n_tests):
        s = time.time()
        stub.voidFunction(server_pb2.void())  # void function
        e = time.time()
        void_times.append(e-s)

    bool_times = []
    for i in range(n_tests):
        s = time.time()
        stub.boolFunction(server_pb2.Bool(boolean=boolean))  # void function
        e = time.time()
        bool_times.append(e-s)

    string32_times = []
    for i in range(n_tests):
        s = time.time()
        stub.stringArg(server_pb2.String(text=string_32))
        e = time.time()
        string32_times.append(e-s)

    string512_times = []
    for i in range(n_tests):
        s = time.time()
        stub.stringArg(server_pb2.String(text=string_512))
        e = time.time()
        string512_times.append(e-s)

    string1024_times = []
    for i in range(n_tests):
        s = time.time()
        stub.stringArg(server_pb2.String(text=string_1024))
        e = time.time()
        string1024_times.append(e-s)

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

    euclidean_times = []
    for i in range(n_tests):
        s = time.time()
        stub.euclideanDistance(server_pb2.EuclidianVectors(vectors=[array_1, array_2]))  # euclidean distance
        e = time.time()
        euclidean_times.append(e-s)

    # dataset
    void_times         = np.array(void_times)
    bool_times         = np.array(bool_times)
    int_arg_times      = np.array(int_arg_times)
    long_arg_times     = np.array(long_arg_times)
    string32_times     = np.array(string32_times)
    string512_times    = np.array(string512_times)
    string1024_times   = np.array(string1024_times)
    int_array_times    = np.array(int_array_times)
    float_array_times  = np.array(float_array_times)
    string_array_times = np.array(string_array_times)
    object_arg_times   = np.array(object_arg_times)
    euclidean_times    = np.array(euclidean_times)

    df = pd.DataFrame({'void':void_times,
                       'boolean':bool_times,
                       'int_arg':int_arg_times,
                       'long_arg':long_arg_times,
                       'string32_arg':string32_times,
                       'string512_arg':string512_times,
                       'string1024_arg':string1024_times,
                       'int_array':int_array_times,
                       'float_array':float_array_times,
                       'string_array':string_array_times,
                       'object_arg':object_arg_times,
                       'euclidean_arg':euclidean_times})
    df.to_csv('grpc_metrics_'+host+'.csv', index=False)
    print('client finished...')


if __name__ == '__main__':
    run()