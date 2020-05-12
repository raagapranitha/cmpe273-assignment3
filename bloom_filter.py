import math
import hashlib
import pickle
# from bitarray import bitarray

class BloomFilter:
    def __init__(self,num_items,prob_score):
        self.num_items  =  num_items
        self.prob_score = prob_score
        self.mBit_count = self.get_m()
        # self.bit_array = bitarray(self.mBit_count)
        # self.bit_array.setall(0)
        self.hash_count = self.get_hash_count()
        self.bit_array = self.initialise_array(self.mBit_count)
    
    def initialise_array(self,mBit_count):
        bit_array=[]
        for i in range(mBit_count):
            bit_array.append(0)
        return bit_array

    
    def get_m(self): 
        mbits = -(self.num_items * math.log(self.prob_score))/(math.log(2)**2) 
        return int(mbits)

    def get_hash_count(self):
        count = (self.mBit_count/self.num_items)*math.log(2)
        return int(count)

    def print_all(self):
        print(f'{self.num_items}\n {self.prob_score} \n {self.mBit_count}\n {self.hash_count}')
    
    def add(self,key):
        hashes = []
        for i in range (self.hash_count):
            if isinstance(key,str):
                key = key.encode("utf-8")
            key = hashlib.md5(key).digest()
            val = int.from_bytes(key, byteorder='big')
            hash_gen = (val)%self.mBit_count
            key = str(hash_gen)
            hashes.append(hash_gen)
            self.bit_array[hash_gen]=1

    def delete(self,key):
        hashes = []
        # entry = key
        for i in range (self.hash_count):
            if isinstance(key,str):
                key = key.encode("utf-8")
            key = hashlib.md5(key).digest()
            val = int.from_bytes(key, byteorder='big')
            hash_gen = (val)%self.mBit_count
            key = str(hash_gen)
            hashes.append(hash_gen)
            self.bit_array[hash_gen]=0

    def is_member(self,key):
        for i in range(self.hash_count):
            if isinstance(key,str):
                key = key.encode("utf-8")
            key = hashlib.md5(key).digest()
            val = int.from_bytes(key, byteorder='big')
            hash_gen = (val)%self.mBit_count
            key = str(hash_gen)
            if self.bit_array[hash_gen] == 0:
                return False  
        return True


def test():
    bf = BloomFilter(1000000,0.05)
    print(bf.get_m())
    print(bf.get_hash_count())
test()
