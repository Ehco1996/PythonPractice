'''
通过Python 分析囚徒困境每一轮 每一位角色的 获邢情况

关于囚徒困境（prisoner dilemma） 是一种博弈论中非常具有代表性的例子
具体情况如下：
有两名犯人 犯人a 和犯人b
每一轮中： 1 若 a 沉默 b也沉默 则 a ，b 各获刑0.5年
        2 若a沉默 b背叛， 则 a 获刑 10年 b不获刑
         3 若b沉默 a背叛 则b获刑10年 a不获刑
         4 若 a 与b 都背叛， 那么两人都获得5年刑法

在本例子中  一共有两种面对方式：
1 nice：不论对方是否背叛，都选择沉默
2 rat ：不论对方是否沉默，都选择背叛
3 tit_for_tat ：如果对方上一轮沉默 那就沉默 如果对方上一轮背叛，那就背叛

'''




#囚徒的三种决策方式
def nice(last_response):
    return False
def rat(last_response):
    return True

def tit_for_tat(last_response):
    if last_response == True:
        return True
    else:
        return False

def prisoner_delimma(turns,a_stragety,b_stragety):
    #函数内首先初始化 囚犯ab默认都不背叛，已经坐牢年限
    a_isbetray = False
    b_isbetray = False
    a_p_years = 0
    b_p_years = 0
    #循环每一轮的结果来累加年限
    for i in range(1, turn + 1):
        a_isbetray =a_stragety(b_isbetray)
        b_isbetray =b_stragety(a_isbetray)
        if a_isbetray and b_isbetray:
            a_p_years += 5
            b_p_years += 5
        elif a_isbetray == False and b_isbetray == False:
            a_p_years += 0.5
            b_p_years += 0.5
        elif a_isbetray == True and b_isbetray == False:
            a_p_years += 0
            a_p_years += 10
        elif a_isbetray == False and b_isbetray == True:
            a_p_years += 10
            a_p_years += 0
    print('囚徒a的年限是{} 囚徒b的年限是{}'.format(a_p_years,b_p_years))

#定义局数
turn = 2
prisoner_delimma(turn,tit_for_tat,tit_for_tat)
