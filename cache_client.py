import sys
import socket
import random
from sample_data import USERS
from server_config import NODES
from pickle_hash import serialize_GET, serialize_PUT, serialize_DELETE
from node_ring import NodeRing
from lru_cache import Lru_Node,Lru_Cache


BUFFER_SIZE = 1024
hash_codes = set()
has_cache = False

class UDPClient():
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)       

    def send(self, request):
        print('Connecting to server at {}:{}'.format(self.host, self.port))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(request, (self.host, self.port))
            response, ip = s.recvfrom(BUFFER_SIZE)
            return response
        except socket.error:
            print("Error! {}".format(socket.error))
            exit()

def lru_cache(function):
    def wrapper(*args,**kwargs):
        if has_cache == False:
            lru_cache = Lru_Cache(*args,**kwargs)
            has_cache = True
        function(lru_cache)
        return wrapper

@lru_cache(5)
def post_users(lru_cache):
        myOb = NodeRing(NODES)
        # PUT all users.
        for u in USERS:
            data_bytes, key = serialize_PUT(u)
            # print(f'In put {data_bytes},{key}')
            # TODO: PART II - Instead of going to server 0, use Naive hashing to split data into multiple servers
            node = myOb.get_node(key)
            response = UDPClient(node['host'], node['port']).send(data_bytes)
            lru_cache.insert_into_cache(response,5)
            hash_codes.add(response)
            # print(hash_codes)
            # lru_cache.print_all_nodes()

        print(f"Number of Users={len(USERS)}\nNumber of Users in hash_codes={len(hash_codes)}")
        print(f"Number of Users={len(USERS)}\nNumber of Users Cached={lru_cache.getCount()}")
        
       
# TODO: PART I
# GET all users
@lru_cache(5)
def get_users(lru_cache):
        myOb = NodeRing(NODES)
        for hc in hash_codes:
            print(hc)
            data_bytes, key = serialize_GET(hc)
            print(f'In GET {data_bytes},{key}')
            data = lru_cache.get_from_cache(key,5)
            if data :
                print(f'{data} found in cache')
                return data
            node = myOb.get_node(key)
            response =  UDPClient(node['host'], node['port']).send(data_bytes)
            print(response)

#DELETE req
@lru_cache(5)
def delete_users(lru_cache):
        myOb = NodeRing(NODES)
        hc = random.sample(hash_codes, 1)[0]
        print(hc)
        data_bytes, key = serialize_DELETE(hc)
        node = myOb.get_node(key)
        response =  UDPClient(node['host'], node['port']).send(data_bytes)
        if(response.decode()=='Success'):
            print('Deleted Succesfully')
            lru_cache.delete_from_cache(key)
    
def process(udp_clients):
    # lru_cache = Lru_Cache(5)
    post_users(lru_cache)
    get_users(lru_cache)
    delete_users(lru_cache)
    

if __name__ == "__main__":
    clients = [
        UDPClient(server['host'], server['port'])
        for server in NODES
    ]
    process(clients)
