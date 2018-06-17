import rpyc
import numpy as np


class Server(rpyc.Service):

    def exposed_voidFunction(self):
        pass

    def exposed_intArg(self, int):
        # print('server received {} [{}]'.format(type(request), request.integer))
        return int

    def exposed_longArg(self, long):
        # print('server received {} [{}]'.format(type(request), request.longValue))
        return long

    def exposed_stringArg(self, string):
        # print('server received {} [{}]'.format(type(request), request.text))
        return string

    def exposed_objectArg(self, object):
        # print('server received {} [{}]'.format(type(request), request))
        return object

    def exposed_stringListArg(self, string_list):
        # print('server received {} {}'.format(type(request), request.texts))
        return string_list

    def exposed_intArray(self, int_list):
        # print('server received {} {}'.format(type(request), request.numbers))
        return int_list

    def exposed_floatArray(self, float_list):
        # print('server received {} {}'.format(type(request), request.numbers))
        return float_list

    def exposed_euclideanDistance(self, v, w):
        v = np.array(v);
        w = np.array(w);
        res = np.sqrt(np.sum((v-w))**2)
        return res


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(Server, port=18861)
    print('Server listening...')
    t.start()
