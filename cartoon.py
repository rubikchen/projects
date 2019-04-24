from selenium import webdriver
import os
br = webdriver.Chrome()
br.get("https://www.zymk.cn/2/")
br.maximize_window()
def clear():
    global br
    try:
        br.execute_script('''var child = document.getElementById("layui-layer-shade1");if(child!=null)child.parentNode.removeChild(child);''')
        br.execute_script('''var child = document.getElementById("readguide");if(child!=null)child.parentNode.removeChild(child);''')
        br.execute_script('''var child = document.getElementById("layui-layer1");if(child!=null)child.parentNode.removeChild(child);''');
        br.execute_script('''var child = document.getElementById("footerTools");if(child!=null)child.parentNode.removeChild(child);''');
    except:
        pass
while True:
    input("next")
    br.implicitly_wait(5)
    times=len(br.find_element_by_class_name("selectpage").find_elements_by_tag_name("option"))
    clear()
    for i in range(times):
        input("next")
        br.find_element_by_css_selector('''body > div.container > div.footpage > span.btn.nextpage''')
        br.execute_script('''var child = document.getElementsByClassName("btn nextpage");if(child!=null)child[0].click()''')
        clear()
    else:
        br.execute_script('''var child = document.getElementsByClassName("looknext");child[0].click()''')
