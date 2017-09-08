#-*- coding: utf-8 -*-
numbers = [5, 6, 7, 8]
print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
#取部分的listletters = ['a', 'b', 'c', 'd', 'e']slice = letters[1:3]#是表示從頭取到中間的值,
# ie. 1, 2#或者不限制結束或開始my_list[:2]
#  Grabs the first two itemsmy_list[3:]
#  Grabs the fourth through last items

#增加list項目以及計算長度
letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)

# 尋找index
animals = ["ant", "bat", "cat"]
print animals.index("bat")

#插入
animals.insert(1, "dog")
print animals
#變成["ant", "dog", "bat", "cat"]
#插在index = 1之前一項

#印出所有list中的項目
my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    print 2*number

#sort
start_list = [5, 3, 1, 2, 4]
start_list.sort()

#remove item in list
beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles


## dictionary
#有一個Key對應儲存的值，透過查詢key得到值

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number: 104

#adding new entries
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']
menu['Spam'] = 2.50
print "There are " + str(len(menu)) + " items on the menu."
print menu

#deleting entries
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Unicorn']
#可以與list結合
my_dict = {
    "fish": ["c", "a", "r", "p"],
    "cash": -4483,
    "luck": "good"
}
print my_dict["fish"][0]

my_dict['pocket']=['seashell', 'strange berry', 'lint']
my_dict['fish'] = my_dict['fish'].remove('a')
my_dict['cash'] = 50

print my_dict.items()
#可以逐步print 出dict中的東西
print my_dict.keys()
print my_dict.values()

for key in my_dict:
    print key, my_dict[key]