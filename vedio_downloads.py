import pandas as pd
import os
import subprocess
import time
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import requests
import warnings
import traceback
import logging
import datetime

def gettime():
    t = datetime.datetime.now()
    time = '_{0}_{1}_{2}_{3}_{4}'.format(t.year,t.month,t.day,t.hour,t.minute)
    return time

def DownloadVedio(url):
    commad = "lux "+url
    # cmd = 'lux https://www.iqiyi.com/v_2993z2f1klc.html'
    try:
        ret = subprocess.check_output(commad,shell=True)
        ret = ret.decode()
        logger.info('URL:  {0}'.format(url))
        logger.info('Name:  {0}'.format(ret))
        NameList.append(ret)
        UrlDoneList.append(url)
    except Exception as e:
        FailList.append(url)
        logger.info('Failed URL:  {0}'.format(url))
        logger.info(e)
    # print(type(ret))
    print('------finish:{0}'.format(url))

if __name__ == '__main__':

    time = gettime()
    warnings.filterwarnings("ignore")
    logging.basicConfig(level=logging.INFO,
                        filename="RunDownloads"+time + ".log",
                        format="%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s")
    logger = logging.getLogger()
    logger.info("start run!")

    # 读取文件中的视频链接
    data = pd.read_excel('Check TAADS Config.xlsx', sheet_name='Sheet29', usecols=[0, 1])
    print(data)
    URL_list = data['URL'].values.tolist()
    NameList = []
    UrlDoneList = []
    FailList = []
    print(len(URL_list))
    sum = 0

    # 遍历下载
    for url in URL_list:
        DownloadVedio(url)
        sum += 1
        logger.info('完成第{0}个'.format(sum))
        print('完成第{0}个'.format(sum))
        # if sum > 4:
        #     break
    
    # 保存
    df = pd.DataFrame({"URL":UrlDoneList,"Name":NameList})
    writer = pd.ExcelWriter('DownloadVedio.xlsx')
    df.to_excel(writer)
    writer.save()
    writer.book.close()
    print('写入done!')
        

