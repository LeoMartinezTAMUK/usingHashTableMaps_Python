""" Created by: Leo Martinez III, Spring 2022 """

from hash_table_map import HashTableMap

HM = HashTableMap(31)
# a) Create a hash table of length N (N = 31)

Students = [(417, 'Adebambo'), (616, 'Alfaro'), (443,'Alghanem'), (758, 'Alvarado'), (355, 'Alvarez'), (940,'Barragan'), (731, 'Beltran'), (599, 'Cantu'), (624,'Cao'), (850, 'Chapman'), (73, 'Devisetty'), (828, 'Flores'), (38,'Franco'), (834, 'Garcia'), (78, 'Gonzalez'), (30, 'Karki'), (979, 'Anthony'), (695, 'Martinez'), (205, 'Narvik'), (656,'Obi'), (98, 'Pena'),(862, 'Ramos'), (634, 'Rangel'), (156,'Rodriguez'), (141, 'Singer'), (149, 'Solis'), (826,'Hugo'), (639, 'Trevino'), (777, 'Diego'), (991,'Sebastian'), (990, 'William')]

for (k, v) in Students:
  HM.setitem(k, v)
print('Hash #1 (10 empty positions)')
print(HM._table)
# b) There are 10 empty buckets/positions

HM1 = HashTableMap(41)
# c) Create a hash table of length N1 (N1 = 41)

for (k, v) in Students:
  HM1.setitem(k, v)
print('\nHash #2 (18 empty positions)')
print(HM1._table)
# d) There are 18 empty buckets/positions

for (k, v) in Students:
  if k > 500:
   HM1.delitem(k)
print('\nHash #2 (without the items that were deleted)')
print(HM1._table)
# e) Remove all the items that has key greater than 500
