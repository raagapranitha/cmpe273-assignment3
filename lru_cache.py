from collections import OrderedDict

# class Lru_Node:
#     def __init__(self,data):
#         # self.head = None
#         self.data = data
#         # self.value = value
#         self.next = None
#         self.prev = None
#         # self.capacity = capacity

# class Lru_cache:
#     def __init__(self,capacity):
#         self.head = None
#         self.capacity = capacity
#         print(f'Lru cache initialised with size {self.capacity}')
    
#     def getSize(self):
#         return self.capacity

#     def getCount(self): 
#             temp = self.head  
#             count = 0 
#             while (temp): 
#                 count += 1
#                 temp = temp.next
#             return count 
        
#     def delete_lru(self):
#         temp = self.head
#         while(temp.next!=None):
#             temp = temp.next
#         last_node = temp.prev
#         last_node.next =None

#     def print_all_nodes(self):
#         temp = self.head
#         print("In lru cache print all")
#         while(temp):
#             print(temp.data)
#             temp = temp.next

#     def insert_into_cache(self,data):
#         new_node = Lru_Node(data)
#         # new_node.data = data
#         if self.head is None:
#             self.head = new_node
#             self.head.prev = None
#             # print("node inserted")
#             return
#         if((self.getCount()) > self.capacity):
#             self.delete_lru()
#         new_node.next = self.head
#         self.head.prev = new_node
#         self.head = new_node
#         print(f'{self.head.data} inserted into cache')
#         # self.print_all_nodes()

#     def get_from_cache(self,data):
#         temp = self.head
#         while(temp!= None):
#             if(temp.data == data):
#                 break
#             temp = temp.next
#         else:
#             # print("Data not in cache")
#             return
#         current = temp
#         if current.next != None:
#             if current.prev!=None:
#                 current.prev.next = current.next
#             else:
#                 current.next.prev=None
#                 self.head = current.next
#         else:
#             if current.prev!= None:
#                 current.prev.next = None
           
#         self.head.prev = current
#         current.next = self.head
#         self.head = current
#         # print("In lru_cache in get")
#         # print(self.head.data)
#         # self.print_all_nodes()
#         return self.head.data

#     def delete_from_cache(self,data):
#         temp =self.head
#         while(temp.next != None):
#             # print("In delete lru while loop")
#             # print(data)
#             # print(temp.data)
#             if temp.data == data:
#                 print(temp.data)
#                 break
#             temp = temp.next
#         else:
#             print("In delete Data not in lru_cache")
#             return 
#         remove = temp
#         if remove.next != None:
#             remove.prev.next = remove.next
#         if remove.prev != None:
#             remove.next.prev = remove.prev   
#         print(f'deleted node with data {remove.data} from lru_cache')
#         self.print_all_nodes()



# def getCount(obj): 
#             temp = obj.head  
#             count = 0 
#             while (temp.next is not None): 
#                 count += 1
#                 temp = temp.next
#             return count 

# def print_all_nodes(obj):
#         temp = obj.head
#         print("In lru cache print all")
#         while(temp is not None):
#             print(temp.data)
#             temp = temp.next


# func_name =""
# def lru_cache(size): 
#     def real_decorator(function):
#         print(function.__name__)
#         def wrapper(*args,**kwargs):
#             global func_name
#             global lru_hash_table
#             global lru_cache_obj

#             # if function.__name__ == 'post_users':
#             #     # print(lru_cache_obj.getSize())
#             #     print("In post_users lru_cache decorator")
#             #     if not lru_cache_initialized:
#             #         lru_cache_obj = Lru_cache(size)
#             #         lru_cache_initialized = True
                
#             #     # print(lru_cache_obj.getSize())
#             #     hash_codes = function()
#             #     return hash_codes
#             # elif function.__name__ == 'get_users':
#             #     print("In get lru_cache decorator")
#             #     if not lru_cache_initialized:
#             #         lru_cache_obj = Lru_cache(size)
#             #         lru_cache_initialized = True
#             #     data = lru_cache_obj.get_from_cache(*args,**kwargs)
#             #     if data :
#             #         print(f'{data} found in cache')
#             #     else:
#             #         lru_cache_obj.insert_into_cache(*args,**kwargs)
#             #         function(*args,**kwargs)
#             # elif function.__name__ == 'delete_users':
#             #     print("In delete lru_cache decorator")
#             #     function(*args,**kwargs)
#             #     lru_cache_obj.delete_from_cache(*args,**kwargs)
            
#                 # print("In test fucntion")
#             if func_name != (function.__name__):
#                 lru_cache_obj = Lru_cache(size)
#                 print_all_nodes(lru_cache_obj)
#                 lru_hash_table = dict()
#                 func_name = function.__name__
#             if  args in lru_hash_table:
#                 print(args)
#                 print('Inside hash_table')
#                 print("Data is in hash_table")  
#                 val = lru_hash_table.get(*args)
#                 temp = lru_cache_obj.head
#                 print(print_all_nodes(lru_cache_obj))
#                 while(temp is not None):
#                     print(f'In loop {temp.data}')
#                     if(temp.data == val):
#                         print(f'Before break {temp.data}')
#                         break
#                     temp = temp.next
#                 current = temp
#                 print(current.data)
#                 if current.next is not None:
#                     if current.prev is not None:
#                         current.prev.next = current.next
#                     else:
#                         current.next.prev=None
#                         lru_cache_obj.head = current.next
#                 else:
#                     if current.prev!= None:
#                         current.prev.next = None
            
#                 lru_cache_obj.head.prev = current
#                 current.next = lru_cache_obj.head
#                 lru_cache_obj.head = current
#                 print(f'Cache hit: {val}')
#                 return lru_cache_obj.head.data
#             else:
#                 val = function(*args,**kwargs)
#                 print('Function hit')
#                 new_node = Lru_Node(val)
#                 if lru_cache_obj.head is None:
#                     lru_cache_obj.head = new_node
#                     lru_cache_obj.head.prev = None
#                     print("node inserted with into cache value")
#                     print(print_all_nodes(lru_cache_obj))
#                 else:
#                     print('in else part node inserted with into cache value')
#                     # new_node.prev = None
#                     new_node.next = lru_cache_obj.head
#                     lru_cache_obj.head.prev = new_node
#                     lru_cache_obj.head = new_node
#                 lru_hash_table[args] =val
#                 print(f'Entry into hash table {lru_hash_table}')
#                 print(f'Entry into lru_cache')
#                 print(print_all_nodes(lru_cache_obj))
#                 if((getCount(lru_cache_obj)) > size):
#                     temp = lru_cache_obj.head
#                     while(temp.next is not None):
#                         temp = temp.next
#                     last_node = temp.prev
#                     last_node.prev.next = None
#                     print(f'Removed lru from cache with value {last_node.data}')
#                     print(print_all_nodes(lru_cache_obj))
#                     print(f'Before delete hash table {lru_hash_table}')
#                     del lru_hash_table[args]
#                     print(f'After delete hash table {lru_hash_table}')
#                 return val
#         return wrapper
#     return real_decorator


func_name =""
def lru_cache(size): 
    def real_decorator(function):
        print(function.__name__)
        def wrapper(*args,**kwargs):
            global func_name
            global lru_dict
            global capacity 
            if func_name != (function.__name__):
                lru_dict = OrderedDict()
                func_name = function.__name__
                capacity = size
                print('Cache initialised with size')
            if args in lru_dict:
                val = lru_dict[args]
                lru_dict.move_to_end(args, False)
                print(f'[Cache hit]  {val}')
                return val
            else:
                val = function(*args,**kwargs)
                if len(lru_dict) >= capacity:
                    lru_dict.popitem()
                lru_dict[args] = val
                lru_dict.move_to_end(args, False)
                return val
        return wrapper
    return real_decorator

            