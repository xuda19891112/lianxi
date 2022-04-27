from os import error, write
from typing import get_args
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import requests
import warnings
import traceback
import pandas as pd
import logging
import datetime


# 获取xray的url列表
def getUrlList():
    global urlNum
    df1 = pd.read_excel('keytag.xlsx',sheet_name='KeyFramesTag')
    # urlList = df1['Xray link'].values.tolist()
    # 筛选planning prediction control
    urlList = df1[df1['Tag'].str.contains('Planning/') | df1['Tag'].str.contains('Prediction/') | df1['Tag'].str.contains('Control/')]['Xray link'].values.tolist()
    urlNum = len(urlList)
    print(urlNum)
    return urlList


# 登录谷歌账户
def googleLogIn(driver,account,password):
    url_google = 'https://accounts.google.com/signin'
    # url_google = 'https://accounts.google.com/signin/v2/identifier?hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    driver.get(url_google)
    sleep(1)
    wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath('//*[@id="identifierId"]'))
    input_name = driver.find_element_by_xpath('//*[@id="identifierId"]')
    input_name.clear()
    input_name.send_keys(account)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'))
    input_key = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    sleep(3)
    input_key.send_keys(password)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    print('--------------谷歌登录完毕！--------------')
    logger.info('--------------谷歌登录完毕！--------------')
    sleep(3)


# 登录xray
def xrayLogin(driver,url):
    driver.get(url)
    wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath('/html/body/div/div/div/div[@class="login-slack"]'))
    driver.find_element_by_xpath('/html/body/div/div/div/div').click()
    wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath('//*[@id="domain"]'))
    input_name = driver.find_element_by_xpath('//*[@id="domain"]')
    input_name.clear()
    input_name.send_keys("autox-ai")
    wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath('//*[@id="page_contents"]/div/div/div[1]/div[2]/form/button'))
    driver.find_element_by_xpath('//*[@id="page_contents"]/div/div/div[1]/div[2]/form/button').click()

    # sign in with google
    wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath('//*[@id="index_google_sign_in_with_google"]'))
    driver.find_element_by_xpath('//*[@id="index_google_sign_in_with_google"]').click()
    wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div/form/div/div[2]/button'))
    driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[2]/button').click()
    print('--------------XRAY登录完毕！--------------')
    logger.info('--------------XRAY登录完毕！--------------')
    sleep(10)

#自动打tag
def autoTag(driver,url):
    try:
        global skipNum
        global tagNum
        driver.get(url)
        tag_edit_xpath = '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[5]'
        tag_chrome_ok = '/html/body/div[5]/div[3]/div/div/div[3]/button'
        tag_input = '//*[@id="react-select-2-input"]'
        tag_edit_ok = '//div[@class="MuiDialogActions-root MuiDialogActions-spacing"]/button[2]'
    
        # tag_box = '/html/body/div[5]/div[3]/div/div/div[2]/li[3]/div/div/div/div/div/div[2]/div[2]'
        tag_box = '/html/body/div[3]/div[3]/div/div/div[2]/li[3]/div/div/div/div/div/div[2]/div[2]'
        # 非chrome浏览器需确认
        # try:
        #     wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath(tag_chrome_ok))
        #     driver.find_element_by_xpath(tag_chrome_ok).click()
        #     sleep(1)
        # except:
        #     pass
        # else:
        #     pass 
        wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath(tag_edit_xpath))
        try:
            driver.find_element_by_xpath(tag_edit_xpath).click()
        except:
            driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[3]/button').click()
            sleep(1)
            driver.find_element_by_xpath(tag_edit_xpath).click()
        else:
            pass
        sleep(1)
        wdwait = WebDriverWait(driver, 300, 0.5).until(lambda x: x.find_element_by_xpath(tag_box))
        driver.find_element_by_xpath(tag_box).click()
        tag_list = driver.find_elements_by_xpath("/html/body/div")[-1]
        # print(tag_list.tag_name)
        # print(tag_list.text)
        # print(type(tag_list.text))
        tagtext = str(tag_list.text)
        # with open('/home/daxu/Downloads/keytag.txt','w', encoding='utf-8') as fp:
        #     fp.write(tagtext)
        # logger.info(tagtext)

        #可能已经打过tag
        if "Simulation/xsim_logsim" not in tagtext:
            print('跳过')
            logger.info('跳过')
            skipNum += 1
            tagNum += 1
            return
        try:
            keytag = tag_list.find_element_by_xpath('./div/div/div[contains(text(), "Simulation/xsim_logsim")]')
            # print(keytag.text)
            # print(keytag.tag_name)
            keytag.click()
        except:
            errorList.append(url)
            logger.info(traceback.format_exc())
            return
        else:
            pass                                          

        sleep(1)
        driver.find_element_by_xpath(tag_edit_ok).click()
        tagNum += 1
        logger.info('----------yeah！----------')
        sleep(3)
    except:
        errorList.append(url)
        logger.info(traceback.format_exc())
        return
    else:
        pass 
    

def gettime():
    t = datetime.datetime.now()
    time = '_{0}_{1}_{2}_{3}_{4}'.format(t.year,t.month,t.day,t.hour,t.minute)
    return time    


if __name__ == '__main__':
    account = "daxu@autox.ai"  # 谷歌用户名
    password = "5211314XuDa"   # 谷歌密码
    time = gettime()
    warnings.filterwarnings("ignore")
    logging.basicConfig(level=logging.INFO,
                        filename="run_autotag"+time + ".log",
                        format="%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s")
    logger = logging.getLogger()
    logger.info("start run autotag!")
    try:
        # fileName = ''
        driver = webdriver.Chrome()
        driver.implicitly_wait(180)
        
        urlList = getUrlList()
        errorList = []
        tagNum = -1
        skipNum = 0
        for url in urlList:
            if tagNum == -1:
                googleLogIn(driver,account,password)
                xrayLogin(driver,url)
                tagNum += 1
            try:
                autoTag(driver,url)                            
            except:
                errorList.append(url)
                logger.info(traceback.format_exc())
                continue
            else:
                pass
            print('------已完成打tag{0}个------'.format(tagNum))
            logger.info('------已完成打tag{0}个------'.format(tagNum))
            # if tagNum == 3:
            #     break
        driver.close()
        print('------本次共有URL{0}个--------'.format(urlNum))
        print('------本次完成打tag{0}个------'.format(tagNum))  # 包含本次打标签的和跳过的
        print('------出问题的tag{0}个------'.format(len(errorList)))
        print('------本周{0}个case打上标签，其中本次成功完成{1}个，已被打过的tag{2}个------'.format(tagNum,tagNum-skipNum,skipNum))
        print(errorList)
        logger.info('------本次共有URL{0}个--------'.format(urlNum))
        logger.info('------本次完成打tag{0}个------'.format(tagNum))
        logger.info('------出问题的tag{0}个------'.format(len(errorList)))
        logger.info('------本周{0}个case打上标签，其中本次成功完成{1}个，已被打过的tag{2}个------'.format(tagNum,tagNum-skipNum,skipNum))
        logger.info(errorList)

    except:
        logger.info(traceback.format_exc())
        print('-------异常结束-------')
        logger.info('-------异常结束-------')
    else:
        pass

    # todo
    # 1-每周数据积累，并统计打tag数量，未成功数量及原因
    # 2-一个tag多个链接
    # 3-输出log