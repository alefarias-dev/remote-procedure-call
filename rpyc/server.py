import rpyc
import numpy as np


class Server(rpyc.Service):

    def exposed_voidFunction(self):
        pass

    def exposed_boolFunction(self, boolean):
        return boolean

    def exposed_intArg(self, int):
        return int

    def exposed_longArg(self, long):
        return long

    def exposed_stringArg(self, string):
        return string

    def exposed_objectArg(self, object):
        return object

    def exposed_stringListArg(self, string_list):
        return string_list

    def exposed_intArray(self, int_list):
        return int_list

    def exposed_floatArray(self, float_list):
        return float_list

    def exposed_euclideanDistance(self, v, w):
        v = np.array(v);
        w = np.array(w);
        res = np.sqrt(np.sum((v-w))**2)
        return res


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(Server, port=18861)
    print('RPyC listening...')
    t.start()
