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

0.85212447913360734


特征test：
totalfloor*housefloor(0/3 1/3 2/3) finish 否定

x室y厅z卫 找几个合适的权重 相乘相加得到一个数(卧室1/3 客厅1/3 卫生间1/14) finish 否定

选几列，例如（height,totalheight,bedroom,livingroom,bathroom.....）做个dbscan然后把label当一列特征（低优先级）

tradeYear-buildYear算一个房龄 finish 否定

所在region中有多少个plate finish 否定

所在plate中有多少个小区 finish 否定

（把region和实际上海行政区对应）(低优先级)

交通设施总数，教育机构总数，生活服务总数  否定

二手房成交总金额/二手房成交套数

新房成交总金额/新房成交总套数 add_totalNewTradeMoney_div_tradeNewNum  score=  0.84610655035

本月成交套数+未成交套数=总套数 add_totalNewNum  score=  0.847436450919

总套数*新房成交均价 add_totalNewNum_mul_tradeNewMeanPrice  score=  0.846148130849

当月板块土地供应面积/供应幅数 否定 add_totalTradeMoney_div_tradeSecNum  score=  0.847782797147

当月板块土地成交面积/成交幅数 add_tradeLandArea_div_tradeLandNum  score=  0.845296148871

totalWorkers/residentPopulation 否定

newWorkers/totalWorkers add_newWorkers_div_totalWorkers  score=  0.846846877336

人均配套设施（低优先级）

lookNum/pv 否定

lookNum/uv 否定

怀疑列：失败
totalfloor,region,salessechousenum,s学校，医院，药房，银行，健身中心，公园，二手房成交金额，二手房成交面积，二手房成交均价，二手房成交套数，新房成交均价，新房剩余未成交套数，土地所有，常住人口
tradingday 不删
drop  saleSecHouseNum
add_none  score=  0.844444095725
drop  interSchoolNum
add_none  score=  0.845475461968
drop  schoolNum
add_none  score=  0.843715842689
drop  privateSchoolNum
add_none  score=  0.846851230438
drop  hospitalNum
add_none  score=  0.846047115036
drop  drugStoreNum
add_none  score=  0.845985713395
drop  gymNum
add_none  score=  0.845306075257
drop  bankNum
add_none  score=  0.847629138691
drop  shopNum
add_none  score=  0.84440823683
drop  parkNum
add_none  score=  0.843220661638
drop  mallNum
add_none  score=  0.845459447015
drop  superMarketNum
add_none  score=  0.847610103709
drop  totalTradeMoney
add_none  score=  0.846414481299
drop  totalTradeArea
add_none  score=  0.847018848793
drop  tradeMeanPrice
add_none  score=  0.846909246973
drop  tradeSecNum
add_none  score=  0.84457056589
drop  totalNewTradeMoney
add_none  score=  0.844470877777
drop  totalNewTradeArea
add_none  score=  0.846816985933
drop  tradeNewMeanPrice
add_none  score=  0.84775182954
drop  tradeNewNum
add_none  score=  0.845706705067
drop  remainNewNum
add_none  score=  0.84603111953
drop  supplyNewNum
add_none  score=  0.847115725992
drop  supplyLandNum
add_none  score=  0.84795266712
drop  tradeLandNum
add_none  score=  0.847979736402
drop  tradeLandArea
add_none  score=  0.846737956749
drop  landTotalPrice
add_none  score=  0.846699150684
drop  landMeanPrice
add_none  score=  0.848286198539
drop  residentPopulation
add_none  score=  0.845848045568
drop  tradeMonth
add_none  score=  0.847023553599
drop  tradeDay
add_none  score=  0.844534947745
drop  bedroom
add_none  score=  0.844511628937
drop  livingroom
add_none  score=  0.847328446545
drop  bathroom
add_none  score=  0.849823481419

要做dbscan，需要将所有列归一化，使用sklearn的standardscaler
注意sklearn不识别dataframe的列名，应该调用的是asmatrix方法(as_matrix即将被丢弃，应使用dataframe.values)
numpy的标准差计算方式与dataframe自带的不同，dataframe自带的std()是对标准差的无偏估计


重新规定了预处理后
baseline
add_none  score=  0.853270015446
初始五步后：
add_none  score=  0.898763091417

add_tradeyear_minus_buildyear  score=  0.900337987251
add_plate_num_in_region  score=  0.897464105969
add_community_num_in_plate  score=  0.900070600605
add_transport_total_num  score=  0.89896188812
add_education_total_num  score=  0.900426925324
add_service_total_num  score=  0.898703746774
add_lookNum_div_pv  score=  0.8995455264
add_lookNum_div_uv  score=  0.90077141385
add_totalWorkers_div_residentPopulation  score=  0.901424302467
add_newWorkers_div_totalWorkers  score=  0.902997142283
add_tradeLandArea_div_tradeLandNum  score=  0.901296358998
add_supplyLandArea_div_supplyLandNum  score=  0.898730915913
add_totalNewNum  score=  0.899602149843
add_totalNewNum_mul_tradeNewMeanPrice  score=  0.901852362879
add_totalTradeMoney_div_tradeSecNum  score=  0.901788089618
add_totalNewTradeMoney_div_tradeNewNum  score=  0.899399879606

尝试每个板块月均的特征（trademoney或者trademoney_div_area）