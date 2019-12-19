# Faker的常用方法：https://mp.weixin.qq.com/s/cfnLW4HeXtNfFScv62BqWg 感谢参考
from faker import Faker
# 常见的语言代号
# 简体中文：zh_CN
# 繁体中文：zh_TW
# 美国英文：en_US
# 英国英文：en_GB
# 德文：de_DE
# 日文：ja_JP
# 韩文：ko_KR
# 法文：fr_FR

faker = Faker("zh_CN")
print('name:', faker.name())
print('address:', faker.address())
# print('text:', faker.text())

# 用于生成一些和地址相关的数据，如地址、城市、邮政编码、街道等内容， 用法如下：
faker.address()
# '新疆维吾尔自治区杰县南湖武汉街D座 253105'
print(faker.building_number())
# 'B座'
print(faker.city())
# '璐县'
print(faker.city_name())
# '贵阳'
print(faker.city_suffix())
# '县'
print(faker.country())
# '阿拉斯加'
print(faker.country_code(representation="alpha-2"))
# 'CR'
print(faker.district())
# '西峰'
print(faker.postcode())
# '726749'
print(faker.province())
# '福建省'
print(faker.street_address())
# '余路N座'
print(faker.street_name())
# '李路'
print(faker.street_suffix())
# '路'

# Color，用于生成和颜色相关的数据，如 HEX、RGB、RGBA 等格式的颜色，用法如下：
print(faker.color_name())
# 'DarkKhaki'
print(faker.hex_color())
# '#97d14e'
print(faker.rgb_color())
# '107,179,51'
print(faker.rgb_css_color())
# 'rgb(20,46,70)'
print(faker.safe_color_name())
# 'navy'
print(faker.safe_hex_color())
# '#dd2200'

# Company，用于生成公司相关数据，如公司名、公司前缀、公司后缀等内容，用法如下：
print(faker.bs())
# 'grow rich initiatives'
print(faker.catch_phrase())
# 'Self-enabling encompassing function'
print(faker.company())
# '恒聪百汇网络有限公司'
print(faker.company_prefix())
# '晖来计算机'
print(faker.company_suffix())
# '信息有限公司'