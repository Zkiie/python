# -*- coding:utf-8 -*-

# 列表
classMates = ['Yali','Anna','Amy']

print classMates
print len(classMates)
# 用索引来访问每一个位置的元素 当索引超出范围时，会报一个indexError的错误

print classMates[0]

# 追加元素到末尾可使用.append方法
# classMates.append('wa')

# 插入元素到指定的位置可使用.insert()方法
# classMates.insert(2,'Jack')

# 删除末尾的元素可使用.pop()方法
# classMates.pop()

# 删除指定位置的元素可使用.pop(i) i既是索引位置
# classMates.pop(2)

# 要把某个元素替换成别的元素，可直接赋值给对应的索引位置
# classMates[2] = 'Jhon'

# 需要说明的是 列表元素的数据类型可不同


# 条件判断 judge
age = 20
if age >= 18:
	print 'your age is',age
	print 'adult'

# if else 语句
age = 3
if age >= 18:
	print 'your age is',age
	print 'adult'
else:
	print 'your age is',age
	print 'teenager'

# if elif语句
age = 3
if age >= 18:
	print 'your age is',age
	print 'adult'
elif age >= 6:
	print 'your age is',age
	print 'teenager'
else:
	print 'kid'






















