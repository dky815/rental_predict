# rental_predict
code for future_lab

预处理规则
rentType 拆成3列 未知方式，--作为一列unknown 整租一列whole_rent 合租一列share_rent(no_div分割方式下，未知0整租1合租2)
houseType 拆成3列，分别命名bedroom livingroom bathroom
houseFloor 低0 中1 高2
houseToward 拆成11列 暂无数据，东西南北。。。，只有某一列为1，剩下都是0
（
no_div方式下
[0,1,2,3,4,5,6,7,8,9,10]
[东,南,西,北,东南,西南,西北,东北,南北,东西,未知]
）
houseDecoration 拆成4列，其它other 精装hardbound 简装simple 毛坯rough，只有某一列为1，其他都是0
(
no_div方式下
[0,1,2,3]
[精装,简装,毛坯,其他]
)
communityName 去掉XQ，保留后5位
city 可去掉
region 去掉RG
plate 去BK
pv,uv的NaN用平均值填充
buildYear 加权平均，年*个数/年总和
tradeTime 分成3列


处理方式:
目前2种，LGBM和默认的空字符串（线性回归）

lightGBM:0.85212
目前添加了region plate communityName tradeMonth的平均tradeMoney和pv_div_uv作为新特征
region plate communityName 三个平均从0.808->0.846

pv_div_uv 0.846->0.848

tradeMonth的平均0.848->0.852

Linear_Regression:bias=1.65306122449 score=0.731681680179



特征test：
totalfloor*housefloor(0/3 1/3 2/3) finish

x室y厅z卫 找几个合适的权重 相乘相加得到一个数(卧室1/3 客厅1/3 卫生间1/14) finish

选几列，例如（height,totalheight,bedroom,livingroom,bathroom.....）做个dbscan然后把label当一列特征（低优先级）

tradeYear-buildYear算一个房龄 finish

所在region中有多少个plate finish

所在plate中有多少个小区 finish

（把region和实际上海行政区对应）(低优先级)

交通设施总数，教育机构总数，生活服务总数 

二手房成交总金额/二手房成交套数

新房成交总金额/新房成交总套数

本月成交套数+未成交套数=总套数

总套数*新房成交均价

当月板块土地供应面积/供应幅数

当月板块土地成交面积/成交幅数

totalWorkers/residentPopulation

newWorkers/totalWorkers

人均配套设施（低优先级）

lookNum/pv

lookNum/uv

