import sys
import socket
import random
import os
from sample_data import USERS
from server_config import NODES
from pickle_hash import serialize_GET, serialize_PUT, serialize_DELETE
from node_ring import NodeRing
from lru_cache import lru_cache
from bloom_filter import BloomFilter


BUFFER_SIZE = 1024
hash_codes = set()
bf = BloomFilter(10,0.05)

class UDPClient():
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)       

    def send(self, request):
        print('Connecting to server at {}:{}:{}'.format(self.host, self.port, os.getpid()))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(request, (self.host, self.port))
            response, ip = s.recvfrom(BUFFER_SIZE)
            return response
        except socket.error:
            print("Error! {}".format(socket.error))
            exit()

def post_users():
        hash_codes = set()
        myOb = NodeRing(NODES)
        # PUT all users.
        for u in USERS:
            data_bytes, key = serialize_PUT(u)
            # TODO: PART II - Instead of going to server 0, use Naive hashing to split data into multiple servers
            node = myOb.get_node(key)
            response = UDPClient(node['host'], node['port']).send(data_bytes)
            hash_codes.add(response)
            bf.add(response)
        return hash_codes
        # print(f"Number of Users={len(USERS)}\nNumber of Users in hash_codes={len(hash_codes)}")
       
        
       
@lru_cache(6)
def get_users(hc):
        myOb = NodeRing(NODES)
        data_bytes, key = serialize_GET(hc)
        print(f'In GET {data_bytes},{key}')
        if bf.is_member(key):
            node = myOb.get_node(key)
            response =  UDPClient(node['host'], node['port']).send(data_bytes)
        else:
            print("Data not in bloom filter and probably not in server")
        return response

#DELETE req
def delete_users(hc):
        myOb = NodeRing(NODES)
        data_bytes, key = serialize_DELETE(hc)
        node = myOb.get_node(key)
        if bf.is_member(key):
            response =  UDPClient(node['host'], node['port']).send(data_bytes)
            if(response.decode()=='Success'):
                print('Deleted Succesfully')
                # bf.delete(key)
        else:
            print("Data not in bloom filter and probably not in server")
    
def process(udp_clients):
    hash_codes = set()
    hash_codes = (post_users())
    for hc in hash_codes:
        get_users(hc)
    for hc in hash_codes:
        get_users(hc)
    hc = random.sample(hash_codes, 1)[0]
    delete_users(hc)
    

if __name__ == "__main__":
    clients = [
        UDPClient(server['host'], server['port'])
        for server in NODES
    ]
    process(clients)
