from python_class import lesson_06
from text_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = test_data.url["url"]
user = test_data.login_data["username"]
pwd = test_data.login_data["password"]
s_key = test_data.s_key["s_key"]
print(url,user,pwd,s_key)
result = lesson_06.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)
if s_key in result:
    print("搜索结果是正确的！")
else:
    print("用例测试不通过！")

