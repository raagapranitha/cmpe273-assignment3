import sys
import socket
import os

from server_config import NODES
from pickle_hash import deserialize, hash_code_hex,serialize


BUFFER_SIZE = 1024

class MyDict(dict):
    def __init__(self): 
        self = dict() 
          
    def put(self, key, value):
        self[key] = value
        return key

class UDPServer():
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.db = MyDict()


    def extract_request(self, data_bytes):
        request = deserialize(data_bytes)
        operation = request['operation']
        key = request['id']
        payload = None
        if 'payload' in request: 
            payload = request['payload']
        print(f'operation={operation} in SERVER')
        # print(f'operation={operation} in SERVER \nid={key}\npayload={payload}')
        response = self.handle_operation(operation, key, payload)
        return response


    def handle_operation(self, operation, key, value):
        if operation == 'GET':
            # TODO: PART I - implement GET retrieval from self.db.xxxxx
            var =self.db[key.decode()]
            var = serialize(var)
            # print(f'Log in get 2 {var}')
            return (str(var)).encode()
            # return "FIX ME".encode()
        elif operation == 'PUT':
            return self.db.put(key, value)
        elif operation =='DELETE':
            # removed_value = self.db[key.decode()].pop(key) 
            # if removed_value == value:
            # print(key)
           
            print(f'{self.db} before delete')
            del self.db[key.decode()]
            print(f'{self.db} after deleting {key}')

            return "Success".encode()
        else:
            print(f'Error: Invalid operation={operation}')
            return 'Not supported operation={}'.format(operation)


    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.host, self.port))

        while True:
            data, ip = s.recvfrom(BUFFER_SIZE)
            print("ip={}:size={}".format(ip, len(data)))
            response = self.extract_request(data)
            # reply back to the client
            if isinstance(response, str):
                response = response.encode()

            s.sendto(response, ip)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Missing server index as argument. Usage: python3 cache_client.py [0-{}]'.format(len(NODES)-1))
        sys.exit(2)

    node_index = int(sys.argv[1])
    node = NODES[node_index]
    udpServer = UDPServer(node['host'], node['port'])
    print('Cache Server[{}] started at {}:{}:{}'.format(node_index, node['host'], node['port'],os.getpid()))
    # f= open("processes.txt","a+")
    #         f.write(str(ip[1]) + "\n")
    #         f.close() 
    udpServer.run()