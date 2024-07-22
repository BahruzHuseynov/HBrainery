# range(start:stop:step) --> range(baslangic:son:addim) (son daxil deyil)
# range(stop) --> 0, 1, 2, ..., stop (stop daxil deyil)

print(list(range(5))) # 0,1,2,3,4 (5 daxil deyil)
print(list(range(2, 8))) # 2,3,4,5,6,7 (8 daxil deyil)
print(list(range(2, 8, 3))) # 2,5 (8 daxil deyil)
print(list(range(10, 5, -1))) # 10,9,8,7,6 (5 daxil deyil)
print(list(range(8, 2, -3))) # 8,5 (2 daxil deyil)
