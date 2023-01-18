class HashTableMap:
  
  def __init__(self, cap):
    self._table = [[]for _ in range(cap)]

  def hash_func(self, key):
    return key % len(self._table)

  def setitem(self, key, value):
    hash_key = self.hash_func(key)
    self._table[hash_key].append((key, value))

  def getitem(self, key):
    hash_key = self.hash_func(key)
    bucket = self._table[hash_key]
    for k, v in bucket:
      if k == key:
        return v

  def delitem(self, key):
    hash_key = key % len(self._table)
    bucket = self._table[hash_key]
    for i, kv in enumerate(bucket):
      k, v = kv
      if k == key:
        del bucket[i]
