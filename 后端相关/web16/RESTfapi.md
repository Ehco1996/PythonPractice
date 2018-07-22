# RESTful api

提出者：Dr. Fielding

该api只和url形式相关
即定义了一个设计api url的套路

用url 来定位资源
使用HTTP动词 （GET/POS/DELETE/....）


举个例子
url

/GET /players 拿到当前所有玩家
/GET /player/id 访问对应id玩家的数据
/PUT /player 更新所有玩家的数据 全量更新
/PATCH /players 部分更新
/DELETE /player/id 删除一个玩家
/GET /player/id/level 获得某个数据


推荐资料 Facebook的open api 
编写规则十分REStful


