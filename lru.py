'''
//LRU

class LRUCache{
	private:
		map<int,int> k2v;
		map<int,int> k2f;
		int cnt;
		int capacity;

	public:
	LRUCache(int capacity) {
		cnt = 0;
		this.capacity = capacity;
		k2v.clear();
		v2f.clear()
	}

	int get(int key) {
		if(k2v.count(key) == 0) {
			return -1;
		}
		
		for(auto [k, f]:k2f) {
			f++;
		}
		k2f[key] = 0;
		return k2v[key];
	}

	void put(int key, int value) {
		if(cnt < capacity) {
			for(auto [k, f]:k2f) {
				f++;
			}
			k2f[key] = 0;
			k2v[key] = value;
			cnt++;
		} else{
			auto [k, f] = k2f.end();
			k2v.clear(k);
			k2f.clear(k);
			for(auto [k, f]:k2f) {
				f++;
			}
			k2f[key] = 0;
			k2v[key] = value;
		}
		
	}
}
'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param operations string字符串一维数组
# @param args int整型二维数组
# @return int整型一维数组
#

from typing import List

class DNode(object):
   
    def __init__(self, key, val, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class CowCache(object):

    def __init__(self, capacity):
        # 双向链表(插入O(1))+哈希表(访问O(1))
        self.size = 0
        self.capacity = capacity
        self.mp = {}
        self.head = DNode(-1, -1)
        self.tail = DNode(-1, -1)
        # 连接首尾, 首尾在mp中不出现
        self.head.prev = self.tail
        self.head.next = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head

    def getPriority(self, cow_id):
        if cow_id in self.mp:
            # 将访问的元素放入表头
            node = self.mp[cow_id]
            self.move_to_first(node)
            return node.val
        return -1

    def move_to_first(self, node):
        # 断开连接
        node.prev.next = node.next
        node.next.prev = node.prev
        # 在头部插入
        self.insert_first(node)
   
    def insert_first(self, node):
        # 将node移动到第一个
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        node.prev = self.head
        tmp.prev = node
        # 记录在mp中
        self.mp[node.key] = node
   
    def setPriority(self, cow_id, priority):
        if cow_id in self.mp:
            node = self.mp[cow_id]
            node.val = priority
            return -2
        # 如果没有就插入
        node = DNode(cow_id, priority)
        if self.size >= self.capacity:
            # 删除尾部元素
            tmp = self.tail.prev
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            del self.mp[tmp.key]
        self.insert_first(node)
        self.size += 1
        return -2

class Solution:
    def cowCacheOperations(self , operations: List[str], args: List[List[int]]) -> List[int]:
        # write code here
        cache = None
        ans = []
        for opt, arg in zip(operations, args):
            if opt == 'CowCache':
                cache = CowCache(*arg)
                ans.append(-2)
            else:
                func = getattr(cache, opt)
                ans.append(func(*arg))
        return ans