import math
import random


class BloomFilter:
    def __init__(self, n, p):
        self.size = math.ceil(-n * math.log(p) / math.log(2) ** 2)
        self.bitset = 0
        self.num_hashes = self._calculate_num_hashes(n)
        self.hash_funcs = [self._create_hash_func() for _ in range(self.num_hashes)]

    def _calculate_num_hashes(self, n):
        return round(self.size * math.log(2) / n)

    def _create_hash_func(self):
        p = 2 ** 31 - 1
        a, b = random.randint(1, p - 7), random.randint(0, p - 9)
        return lambda x: ((a * x + b) % p) % self.size

    def add(self, ip):
        for hash_func in self.hash_funcs:
            index = hash_func(int(ip.replace('.', '')))
            newbit = 1 << index
            self.bitset |= newbit

    def __contains__(self, ip):
        for hash_func in self.hash_funcs:
            index = hash_func(int(ip.replace('.', '')))
            newbit = 1 << index

            if not self.bitset & newbit:
                return False
        return True


bloom_filter = BloomFilter(1000, 0.01)
bloom_filter.add("193.168.1.2")
print("193.168.1.2" in bloom_filter)
print("192.168.1.3" in bloom_filter)
