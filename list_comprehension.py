# my_lst = [1,2,3,4,5,6,7,8,9,10]
#
# my_lst_x2 = [i for i in my_lst if i % 2 == 0]
# my_lst_x2_else = [i if i % 2 == 0 else print(f'{i} failed with error') for i in my_lst]
#
#
# print(my_lst_x2)
# print(my_lst_x2_else)
#
# my_dict = {x: x for x in range(10)}
#
# print(my_dict)
#
# countries = ['ru','fr','ua','uk']
# codes = [74,43,12,811]
# dict_country_codes = dict(zip(countries, codes))
# print(dict_country_codes)




list_int = [1, 2, 3]
list_int_2 = [4, 5, 6]
list_int_fin = [(x, y) for x in list_int for y in list_int_2]
print(list_int_fin)



