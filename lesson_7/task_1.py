# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

fruits_1 = ['Banana', 'Apricot', 'Avocado', 'Cherry', 'Pineapple', 'Orange']
fruits_2 = ['Cherry', 'Pineapple', 'Orange', 'Banana', 'Bergamot', 'Grapes', 'Grapefruit', 'Pear', 'Melon']

result_list = [el for el in fruits_1 if fruits_2.count(el)]
print(result_list)