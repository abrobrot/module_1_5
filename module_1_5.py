immutable_var = 1, 2, 3, 4, 5, 'bottle', False
print (immutable_var)
#print (immutable_var[2]) #можно выводить обьекты кортежа выборочно
#immutable_var[0] = 3  #особенность данной переменной заключается в ее неизменности, выборочно поменять значение невозможно по самой сути переменной
#test_var=[1,2,3],True,'a' #но если в кортеже создать список, то обьекты самого списка изменять можно
#print (test_var)
#test_var[0][1] = 5
#print (test_var)
mutable_list = [1,2,3,'apple','boat','night']
mutable_list[1] = 8
mutable_list[-1] =True
print (mutable_list)