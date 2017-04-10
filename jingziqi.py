# 井字棋游戏的判断
'''
井字棋 ：在九宫格里 如果有任何行 
或者列满足三子连城一线 
包括 斜着的线路，就能获得胜利
反之 则游戏失败
'''

'''
棋盘 

   |   |
— - - - - -
   |   |
- - - - - -
   |   |

'''


#定义一个二维数组 来接收棋盘 当位置上为零时 视为 没有罗子
board = [[0,0,0],[0,0,0],[0,0,0]]

#读取棋盘数组
for i in range(0,3):
    for j in range(0,3):
        board[i][j] = input("请输入第{}行，第{} 列的棋子  ".format(i+1,j+1))



#打印出棋盘
print("输入的棋盘如下 ：")
for i in range(0,3):
    print (board[i])
    print('- - - - -')


#判断是否获胜以及哪一方获胜： 一共只有八种胜利的组合 
is_win = False

while not is_win:
    #case 1
    if board[0][0]==board[1][0]==board[2][0]:
        print(board[0][0] ,'win')
        is_win = True
        break
    #case2 
    elif board[0][1]==board[1][1]==board[2][1]: 
        print(board[0][0] ,'win')
        is_win = True
        break
    #case3 
    elif board[0][2]==board[1][2]==board[2][2]:
        print(board[0][0] ,'win')
        is_win = True
        break
    #case4
    elif board[0][0]==board[0][1]==board[0][2]:
        print(board[0][0] ,'win')
        is_win = True
        break
    #case5
    elif board[1][0]==board[1][1]==board[1][2]:
        print(board[0][0] ,'win')
        is_win = True
        break
    #case6
    elif board[2][0]==board[2][1]==board[2][2]:
        print(board[0][0] ,'win')
        is_win = True
        break
    #case7
    elif board[0][0]==board[1][1]==board[2][2]:
        print(board[0][0] ,'win')
        is_win = True
        break
    #case8
    elif board[0][2]==board[1][1]==board[2][0]:
        print(board[0][0] ,'win')
        is_win = True
        break
    else:
         print("该棋盘没有胜利者")
