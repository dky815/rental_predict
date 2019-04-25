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