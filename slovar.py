a = {
	'Россия':'Москва',
	'США':'Вашингтон',
	'Египет':'Каир',
	'Замбия':'Луаска',
	'Иран':'Тегеран'
}
print('добавляем элемент')
a['Украина']='Киев'

for key,value in a.items():
	print('{}:{}'.format(key,value))

print('получаем данные')
print(a['Украина'])
print('сложение')
print(a['Украина'] + a['Египет'])
print('------------------------')
print ('метод get')
print (a.get('Замбия'))
print(a.get('Украина') + a.get('Египет'))
a.get('Франция',0)
print(a.get('Замбия'))
print("Франция" in a)
print('Украина' not in a)
print('Украина' in a)
for key in a:
	print(key)
print('-----------------')
del a['Замбия']
for key in a:
	print(key)
try:
	del a['Франция']
except KeyError:
	pass
print('111')