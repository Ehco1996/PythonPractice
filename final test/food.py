'''
考试题目1

题目内容：
输入一组不同食材的名字，用“,”分割，请输出它们可能组成的所有菜式名称。

输入格式:
食材1, 食材2, 食材3

输出格式：（注意：输出列表请按照用户输入食材顺序开始排列，例如：优先输出食材1开头的菜品）
食材1食材2
食材1食材3
食材2食材1
食材2食材3
食材3食材1
食材3食材2

输入样例：
西红柿, 花椰菜

输出样例：
西红柿花椰菜
花椰菜西红柿

'''


food = str(input())
food = food.replace(' ','')
foodlist = food.split(',')
for i in foodlist:
    new_food_list = foodlist.copy()
    new_food_list.remove(i)
    for j in new_food_list:
        print(i,end='')
        print(j)
        
      