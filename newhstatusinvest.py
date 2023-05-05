import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import time
from scipy.stats import norm
import numpy as np
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import warnings
warnings.filterwarnings('ignore') # Ignorar qualquer aviso...

sns.set_style("darkgrid")
plt.rcParams.update({"font.size":15})

start_time = time.time()

def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
 
    return random.choice(uastrings)

def get_result(ticker):
    executable_path = "C:/Users/Bem-vindo(a)/Downloads/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = executable_path

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'user-agent={GET_UA()}')
    

    driver = webdriver.Chrome(executable_path=executable_path,options=chrome_options)

    data = []

    driver.get("https://statusinvest.com.br/acoes/"+ticker)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    driver.find_element(By.ID,'contabil-section').click()
    
    try:
        popup_1 = driver.find_element(By.XPATH,"/html/body/div[23]/div/div/div[1]/button")
        time.sleep(4)
        action = ActionChains(driver)
        action.move_to_element(popup_1).perform()
        popup_1.click()
        time.sleep(1)
    except:
        pass
    
    time.sleep(5)
    
    try: 
        dropdown_1 = driver.find_element(By.XPATH,"//*[@id='contabil-section']/div[1]/div/div[2]/header/div[2]/div[4]/div[1]/input")
        actionis = ActionChains(driver)
        actionis.move_to_element(dropdown_1).perform()
        dropdown_1.click()
    except:
        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup).perform()
        popup.click()
        time.sleep(1)

    try:
        for opt in driver.find_elements(By.TAG_NAME,"Li"):
            if opt.text == "2011":
                time.sleep(1)
                actionis = ActionChains(driver)
                actionis.move_to_element(opt).perform()
                opt.click()
    except:
        try:
            for opt in driver.find_elements(By.TAG_NAME,"Li"):
                if opt.text == "2012":
                    time.sleep(1)
                    actionis = ActionChains(driver)
                    actionis.move_to_element(opt).perform()
                    opt.click()
        except:
            try:
                for opt in driver.find_elements(By.TAG_NAME,"Li"):
                    if opt.text == "2013":
                        time.sleep(1)
                        actionis = ActionChains(driver)
                        actionis.move_to_element(opt).perform()
                        opt.click()
            except:
                try:
                    for opt in driver.find_elements(By.TAG_NAME,"Li"):
                        if opt.text == "2014":
                            time.sleep(1)
                            actionis = ActionChains(driver)
                            actionis.move_to_element(opt).perform()
                            opt.click()
                except:
                    try:
                        for opt in driver.find_elements(By.TAG_NAME,"Li"):
                            if opt.text == "2015":
                                time.sleep(1)
                                actionis = ActionChains(driver)
                                actionis.move_to_element(opt).perform()
                                opt.click()
                    except:
                        pass
    
    folder = driver.find_element(By.XPATH,"//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button")
    actione = ActionChains(driver)
    actione.move_to_element(folder).perform()
    ver_tudor=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button")))
    driver.execute_script("arguments[0].click();", ver_tudor)

    movit = driver.find_element(By.XPATH,"//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[1]/span/div/div/a/span[1]")
    actions = ActionChains(driver)
    time.sleep(2)
    actions.move_to_element(movit).perform()

    time.sleep(0.5)
    rows = driver.find_elements(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr")
    try:
        popup_1 = driver.find_element(By.XPATH,"/html/body/div[23]/div/div/div[1]/button")
        time.sleep(4)
        action = ActionChains(driver)
        action.move_to_element(popup_1).perform()
        popup_1.click()
        time.sleep(1)
    except:
        pass
    time.sleep(5)

    for row in rows:
        try:
            popup_1 = driver.find_element(By.XPATH,"/html/body/div[23]/div/div/div[1]/button")
            time.sleep(4)
            action = ActionChains(driver)
            action.move_to_element(popup_1).perform()
            popup_1.click()
        except:
            pass
        cols = row.find_elements(By.XPATH, ".//td")
        cols = [x.text for x in cols]
        data.append(cols)

    try:
        popup_1 = driver.find_element(By.XPATH,"/html/body/div[23]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup_1).perform()
        popup_1.click()
        time.sleep(1)
    except:
        pass

    df = pd.DataFrame(data)

    df[0] = df[0].str.replace("[0-9]", "").str.replace("[^\w\s]", "").str.strip()
    df[0] = df[0].str.replace("show_chart", "").str.replace("- (R$)", "")

    df[0] = df[0].str.split('  ', 0).str[0]
    df[0] = df[0].str.split('\n', 0).str[0]

    row = df.iloc[1] 
    length = row.size
    for i in range(1,length):
        df[i] = df[i].str.replace("M", "").str.replace("%", "").str.strip()
        df[i] = df[i].str.replace(".", "").str.replace(",", ".").str.replace("-$", "")
        df[i] = pd.to_numeric(df[i], errors='coerce')
        
    df = df.drop(columns=[2,3,5,6,8,9,11,12,14,15,17,18,20,21,23,24,26,27,29,30,32,33],axis=1)
    df.set_index(0,inplace=True)

    columns = [34,31,28,25,22,19,16,13,10,7,4,1]
    df = df[columns]
    df = df.rename(columns={34:"2011",31:"2012",28:"2013",25:'2014',22:"2015",19:"2016",16:"2017", 13: "2018",10:"2019",7:"2020",4:"2021",1:"Ultimos 12m"})
    df_r = df.transpose()
    df_r["Custos"] = np.abs(df_r["Custos"])
    df_r.fillna(0,inplace=True)
    
    return df_r


def get_fluxo(ticker):
    executable_path = "C:/Users/Bem-vindo(a)/Downloads/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = executable_path

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'user-agent={GET_UA()}')
    

    driver = webdriver.Chrome(executable_path=executable_path,options=chrome_options)

    data = []
        
    driver.get("https://statusinvest.com.br/acoes/"+ticker)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    driver.find_element(By.ID,'contabil-section').click()
    
    time.sleep(5)
    
    dropdown_2 = driver.find_element(By.XPATH,"//*[@id='contabil-section']/div[1]/div/div[3]/header/div[2]/div[4]/div[1]/input")
    actionis = ActionChains(driver)
    actionis.move_to_element(dropdown_2).perform()
    dropdown_2.click()
    
    try:
        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup).perform()
        popup.click()
        time.sleep(1)
    except:
        pass
    
    try:
        for opt in driver.find_elements(By.TAG_NAME,"Li"):
            if opt.text == "2011":
                time.sleep(1)
                actionis = ActionChains(driver)
                actionis.move_to_element(opt).perform()
                opt.click()
    except:
        try:
            for opt in driver.find_elements(By.TAG_NAME,"Li"):
                if opt.text == "2012":
                    time.sleep(1)
                    actionis = ActionChains(driver)
                    actionis.move_to_element(opt).perform()
                    opt.click()
        except:
            try:
                for opt in driver.find_elements(By.TAG_NAME,"Li"):
                    if opt.text == "2013":
                        time.sleep(1)
                        actionis = ActionChains(driver)
                        actionis.move_to_element(opt).perform()
                        opt.click()
            except:
                try:
                    for opt in driver.find_elements(By.TAG_NAME,"Li"):
                        if opt.text == "2014":
                            time.sleep(1)
                            actionis = ActionChains(driver)
                            actionis.move_to_element(opt).perform()
                            opt.click()
                except:
                    try:
                        for opt in driver.find_elements(By.TAG_NAME,"Li"):
                            if opt.text == "2015":
                                time.sleep(1)
                                actionis = ActionChains(driver)
                                actionis.move_to_element(opt).perform()
                                opt.click()
                    except:
                        pass
    try:
        try:
            popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
            time.sleep(5)
            action = ActionChains(driver)
            action.move_to_element(popup).perform()
            popup.click()
            time.sleep(1)
        except:
            pass
        for opt in driver.find_elements(By.TAG_NAME,"Li"):
            if opt.text == "2013":
                time.sleep(1)
                actionis = ActionChains(driver)
                actionis.move_to_element(opt).perform()
                opt.click()
    except:
        try:
            try:
                popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                time.sleep(5)
                action = ActionChains(driver)
                action.move_to_element(popup).perform()
                popup.click()
                time.sleep(1)
            except:
                pass
            for opt in driver.find_elements(By.TAG_NAME,"Li"):
                if opt.text == "2014":
                    time.sleep(1)
                    actionis = ActionChains(driver)
                    actionis.move_to_element(opt).perform()
                    opt.click()
        except:
            try:
                try:
                    popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                    time.sleep(5)
                    action = ActionChains(driver)
                    action.move_to_element(popup).perform()
                    popup.click()
                    time.sleep(1)
                except:
                    pass
                for opt in driver.find_elements(By.TAG_NAME,"Li"):
                    if opt.text == "2015":
                        time.sleep(1)
                        actionis = ActionChains(driver)
                        actionis.move_to_element(opt).perform()
                        opt.click()
            except:
                pass
    
    try:
        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup).perform()
        popup.click()
        time.sleep(1)
    except:
        pass
    
    dropdown_2 = driver.find_element(By.XPATH,"//*[@id='contabil-section']/div[1]/div/div[3]/header/div[2]/div[4]/div[1]/input")
    actionis = ActionChains(driver)
    actionis.move_to_element(dropdown_2).perform()
    dropdown_2.click()
    
    try:
        for opt in driver.find_elements(By.TAG_NAME,"Li"):
            if opt.text == "2011":
                time.sleep(1)
                actionis = ActionChains(driver)
                actionis.move_to_element(opt).perform()
                opt.click()
    except:
        try:
            for opt in driver.find_elements(By.TAG_NAME,"Li"):
                if opt.text == "2012":
                    time.sleep(1)
                    actionis = ActionChains(driver)
                    actionis.move_to_element(opt).perform()
                    opt.click()
        except:
            try:
                for opt in driver.find_elements(By.TAG_NAME,"Li"):
                    if opt.text == "2013":
                        time.sleep(1)
                        actionis = ActionChains(driver)
                        actionis.move_to_element(opt).perform()
                        opt.click()
            except:
                try:
                    for opt in driver.find_elements(By.TAG_NAME,"Li"):
                        if opt.text == "2014":
                            time.sleep(1)
                            actionis = ActionChains(driver)
                            actionis.move_to_element(opt).perform()
                            opt.click()
                except:
                    try:
                        for opt in driver.find_elements(By.TAG_NAME,"Li"):
                            if opt.text == "2015":
                                time.sleep(1)
                                actionis = ActionChains(driver)
                                actionis.move_to_element(opt).perform()
                                opt.click()
                    except:
                        pass
    try:
        try:
            popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
            time.sleep(5)
            action = ActionChains(driver)
            action.move_to_element(popup).perform()
            popup.click()
            time.sleep(1)
        except:
            pass
        for opt in driver.find_elements(By.TAG_NAME,"Li"):
            if opt.text == "2013":
                time.sleep(1)
                actionis = ActionChains(driver)
                actionis.move_to_element(opt).perform()
                opt.click()
    except:
        try:
            try:
                popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                time.sleep(5)
                action = ActionChains(driver)
                action.move_to_element(popup).perform()
                popup.click()
                time.sleep(1)
            except:
                pass
            for opt in driver.find_elements(By.TAG_NAME,"Li"):
                if opt.text == "2014":
                    time.sleep(1)
                    actionis = ActionChains(driver)
                    actionis.move_to_element(opt).perform()
                    opt.click()
        except:
            try:
                try:
                    popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                    time.sleep(5)
                    action = ActionChains(driver)
                    action.move_to_element(popup).perform()
                    popup.click()
                    time.sleep(1)
                except:
                    pass
                for opt in driver.find_elements(By.TAG_NAME,"Li"):
                    if opt.text == "2015":
                        time.sleep(1)
                        actionis = ActionChains(driver)
                        actionis.move_to_element(opt).perform()
                        opt.click()
            except:
                pass
    
    folder2 = driver.find_element(By.XPATH,"//*[@id='contabil-section']/div[1]/div/div[3]/div[2]/div[1]/button")
    actiones = ActionChains(driver)
    actiones.move_to_element(folder2).perform()
    ver_tudof=WebDriverWait(driver,8).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='contabil-section']/div[1]/div/div[3]/div[2]/div[1]/button")))
    driver.execute_script("arguments[0].click();", ver_tudof)
    
    try:
        popup_1 = driver.find_element(By.XPATH,"/html/body/div[23]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup_1).perform()
        popup_1.click()
        time.sleep(1)
    except:
        pass

    rows2 = driver.find_elements(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[3]/div[1]/div[1]/table/tbody/tr")
    for row in rows2:
        cols2 = row.find_elements(By.XPATH, ".//td")
        cols2 = [x.text for x in cols2]
        data.append(cols2)
    
    
    try:
        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup).perform()
        popup.click()
        time.sleep(1)
    except:
        pass
    
    df = pd.DataFrame(data)

    df[0] = df[0].str.replace("[0-9]", "").str.replace("[^\w\s]", "").str.strip()
    df[0] = df[0].str.replace("show_chart", "").str.replace("- (R$)", "")

    df[0] = df[0].str.split('  ', 0).str[0]
    df[0] = df[0].str.split('\n', 0).str[0]

    row = df.iloc[1] 
    length = row.size
    for i in range(1,length):
        df[i] = df[i].str.replace("M", "").str.replace("%", "").str.strip()
        df[i] = df[i].str.replace(".", "").str.replace(",", ".").str.replace("-$", "")
        df[i] = pd.to_numeric(df[i], errors='coerce')
        
    df = df.drop(columns=[2,4,6,8,10,12,14,16,18,20],axis=1)
    df.set_index(0,inplace=True)

    columns = [21,19,17,15,13,11,9,7,5,3,1]
    df = df[columns]
    df = df.rename(columns={21:"2011",19:"2012",17:"2013",15:"2014",13:"2015",11:"2016",9: "2017", 7: "2018",5:"2019",3:"2020",1:"2021"})
    df_f = df.transpose()
    df_f.fillna(0,inplace=True)
    
    return df_f

def get_balance(ticker):
    executable_path = "C:/Users/Bem-vindo(a)/Downloads/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = executable_path

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'user-agent={GET_UA()}')
    

    driver = webdriver.Chrome(executable_path=executable_path,options=chrome_options)

    data = []
    
    driver.get("https://statusinvest.com.br/acoes/"+ticker)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    driver.find_element(By.ID,'contabil-section').click()
    
    time.sleep(2)

    balanc = driver.find_element(By.XPATH,"//*[@id='main-2']/div[8]/div/div/div[2]/div[1]/div[1]/table/tbody")
    balanc_act = ActionChains(driver)
    balanc_act.move_to_element(balanc).perform()
    
    try: 
        dropdown_3 = driver.find_element(By.XPATH,"//*[@id='main-2']/div[8]/div/div/div[2]/header/div[2]/div[4]/div[1]/input")
        actionis = ActionChains(driver)
        actionis.move_to_element(dropdown_3).perform()
        dropdown_3.click()
    except:
        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup).perform()
        popup.click()
        time.sleep(1)
        
    try:
        try:
            popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
            time.sleep(5)
            action = ActionChains(driver)
            action.move_to_element(popup).perform()
            popup.click()
            time.sleep(1)
        except:
            pass            
        for opt in driver.find_elements(By.TAG_NAME,"Li"):
            if opt.text == "2011":
                time.sleep(1)
                actionis = ActionChains(driver)
                actionis.move_to_element(opt).perform()
                opt.click()
    except:
        try:
            try:
                popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                time.sleep(5)
                action = ActionChains(driver)
                action.move_to_element(popup).perform()
                popup.click()
                time.sleep(1)
            except:
                pass
            for opt in driver.find_elements(By.TAG_NAME,"Li"):
                if opt.text == "2012":
                    time.sleep(1)
                    actionis = ActionChains(driver)
                    actionis.move_to_element(opt).perform()
                    opt.click()
        except:
            try:
                try:
                    popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                    time.sleep(5)
                    action = ActionChains(driver)
                    action.move_to_element(popup).perform()
                    popup.click()
                    time.sleep(1)
                except:
                    pass
                for opt in driver.find_elements(By.TAG_NAME,"Li"):
                    if opt.text == "2013":
                        time.sleep(1)
                        actionis = ActionChains(driver)
                        actionis.move_to_element(opt).perform()
                        opt.click()
            except:
                try:
                    try:
                        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                        time.sleep(5)
                        action = ActionChains(driver)
                        action.move_to_element(popup).perform()
                        popup.click()
                        time.sleep(1)
                    except:
                        pass
                    for opt in driver.find_elements(By.TAG_NAME,"Li"):
                        if opt.text == "2014":
                            time.sleep(1)
                            actionis = ActionChains(driver)
                            actionis.move_to_element(opt).perform()
                            opt.click()
                except:
                    try:
                        try:
                            popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                            time.sleep(5)
                            action = ActionChains(driver)
                            action.move_to_element(popup).perform()
                            popup.click()
                            time.sleep(1)
                        except:
                            pass
                        for opt in driver.find_elements(By.TAG_NAME,"Li"):
                            if opt.text == "2015":
                                time.sleep(1)
                                actionis = ActionChains(driver)
                                actionis.move_to_element(opt).perform()
                                opt.click()
                    except:
                        pass
    try:
        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup).perform()
        popup.click()
        time.sleep(1)
    except:
        pass
    folder3 = driver.find_element(By.XPATH,"/html/body/main/div[8]/div/div/div[2]/div[2]/button")
    actione = ActionChains(driver)
    actione.move_to_element(folder3).perform()
    ver_tudo=WebDriverWait(driver,8).until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div[8]/div/div/div[2]/div[2]/button")))
    driver.execute_script("arguments[0].click();", ver_tudo)
    
    try: 
        dropdown_3 = driver.find_element(By.XPATH,"//*[@id='main-2']/div[8]/div/div/div[2]/header/div[2]/div[4]/div[1]/input")
        actionis = ActionChains(driver)
        actionis.move_to_element(dropdown_3).perform()
        dropdown_3.click()
    except:
        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup).perform()
        popup.click()
        time.sleep(1)
        
    try:
        try:
            popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
            time.sleep(5)
            action = ActionChains(driver)
            action.move_to_element(popup).perform()
            popup.click()
            time.sleep(1)
        except:
            pass            
        for opt in driver.find_elements(By.TAG_NAME,"Li"):
            if opt.text == "2011":
                time.sleep(1)
                actionis = ActionChains(driver)
                actionis.move_to_element(opt).perform()
                opt.click()
    except:
        try:
            try:
                popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                time.sleep(5)
                action = ActionChains(driver)
                action.move_to_element(popup).perform()
                popup.click()
                time.sleep(1)
            except:
                pass
            for opt in driver.find_elements(By.TAG_NAME,"Li"):
                if opt.text == "2012":
                    time.sleep(1)
                    actionis = ActionChains(driver)
                    actionis.move_to_element(opt).perform()
                    opt.click()
        except:
            try:
                try:
                    popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                    time.sleep(5)
                    action = ActionChains(driver)
                    action.move_to_element(popup).perform()
                    popup.click()
                    time.sleep(1)
                except:
                    pass
                for opt in driver.find_elements(By.TAG_NAME,"Li"):
                    if opt.text == "2013":
                        time.sleep(1)
                        actionis = ActionChains(driver)
                        actionis.move_to_element(opt).perform()
                        opt.click()
            except:
                try:
                    try:
                        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                        time.sleep(5)
                        action = ActionChains(driver)
                        action.move_to_element(popup).perform()
                        popup.click()
                        time.sleep(1)
                    except:
                        pass
                    for opt in driver.find_elements(By.TAG_NAME,"Li"):
                        if opt.text == "2014":
                            time.sleep(1)
                            actionis = ActionChains(driver)
                            actionis.move_to_element(opt).perform()
                            opt.click()
                except:
                    try:
                        try:
                            popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
                            time.sleep(5)
                            action = ActionChains(driver)
                            action.move_to_element(popup).perform()
                            popup.click()
                            time.sleep(1)
                        except:
                            pass
                        for opt in driver.find_elements(By.TAG_NAME,"Li"):
                            if opt.text == "2015":
                                time.sleep(1)
                                actionis = ActionChains(driver)
                                actionis.move_to_element(opt).perform()
                                opt.click()
                    except:
                        pass
    try:
        popup = driver.find_element(By.XPATH,"/html/body/div[19]/div/div/div[1]/button")
        time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(popup).perform()
        popup.click()
        time.sleep(1)
    except:
        pass
    
    balanc = driver.find_element(By.XPATH,"//*[@id='main-2']/div[8]/div/div/div[2]/div[1]/div[1]/table/tbody")
    balanc_act = ActionChains(driver)
    balanc_act.move_to_element(balanc).perform()
    
    time.sleep(3)

    rows3 = driver.find_elements(By.XPATH, "//*[@id='main-2']/div[8]/div/div/div[2]/div[1]/div[1]/table/tbody/tr")
    for row in rows3:
        cols3 = row.find_elements(By.XPATH, ".//td")
        cols3 = [x.text for x in cols3]
        data.append(cols3)
        
    df = pd.DataFrame(data)

    df[0] = df[0].str.replace("[0-9]", "").str.replace("[^\w\s]", "").str.strip()
    df[0] = df[0].str.replace("show_chart", "").str.replace("- (R$)", "")

    df[0] = df[0].str.split('  ', 0).str[0]
    df[0] = df[0].str.split('\n', 0).str[0]

    row = df.iloc[1] 
    length = row.size
    for i in range(1,length):
        df[i] = df[i].str.replace("M", "").str.replace("%", "").str.strip()
        df[i] = df[i].str.replace(".", "").str.replace(",", ".").str.replace("-$", "")
        df[i] = pd.to_numeric(df[i], errors='coerce')
        
    df = df.drop(columns=[2,3,5,6,8,9,11,12,14,15,17,18,20,21,23,24,26,27,29,30],axis=1)
    df.set_index(0,inplace=True)

    columns = [31,28,25,22,19,16,13,10,7,4,1]
    df = df[columns]
    df = df.rename(columns={31:"2011",28:"2012",25:"2013",22:"2014",19:"2015",16:"2016",13: "2017",10:"2018",7:"2019",4:"2020",1:"2021"})
    df_b = df.transpose()
    df_b.fillna(0,inplace=True)
    
    return df_b
    
def log_values(source,ticker,index):
    df_l = source[ticker][index]
    
    print(f"Ativo: {ticker}")
    print(f"Indicador: {index}")
    
    plt.figure(figsize=(20,12))
    plt.plot(np.log(1+df_l.pct_change()))
    plt.title(f"Log {index} {ticker}")
    plt.show()
    
def historical_values(source,index):
    print(f"Dado Historico: {index}")
    
    plt.figure(figsize=(20,12))
    
    if index == "Margem Bruta":
        plt.title(f"Historico {index}%")
    
    elif index == "Margem Ebitda":
        plt.title(f"Historico {index}%")
    
    elif index == "Margem Líquida":
        plt.title(f"Historico {index}%")
    
    else:
        plt.title(f"Historico {index}")
    
    for t in source.keys():
        plt.plot(source[t][index],alpha=0.6)
    plt.legend([x for x in source.keys()],loc='upper left',framealpha=0.55)
    plt.show()
    
def CAGR(source,index):
    df = pd.DataFrame()
    
    for t in source.keys():
        df[t] = source[t][index]
    
    max_index = len(df)

    CAGR = np.power((df.iloc[max_index -1]/df.iloc[0]), (1/max_index)) - 1
    CAGR = CAGR.sort_values()
    print(f"CAGRs  em  % a.a:  \n{round(CAGR*100,2).values}\n")

    plt.figure(figsize=(20,12))
    plt.bar(CAGR.index,CAGR.values*100)
    plt.title(f"CAGR%  -  {index}")
    plt.ylabel("CAGR")
    plt.show()
    
def x1vsx2(ticker,source,source2,index,index2):
    df_a = source[ticker][index]
    df_h = source2[ticker][index2]
    
    print(f"Ativo: {ticker}")
    
    plt.figure(figsize=(20,12))
    plt.plot(df_a)
    plt.plot(df_h)
    plt.title(f"{index} vs {index2}  -  {ticker}")
    plt.legend([index,index2],loc='upper left',framealpha=0.55)
    plt.show()

def log_x1vsx2(ticker,source,source2,index,index2):
    df_a = source[ticker][index]
    df_h = source2[ticker][index2]
    
    print(f"Ativo: {ticker}")
    
    plt.figure(figsize=(20,12))
    plt.plot(100*(np.log(1+df_a.pct_change())))
    plt.plot(100*(np.log(1+df_h.pct_change())))
    plt.title(f"Log {index} vs {index2} (Em %) -  {ticker}")
    plt.legend([index,index2],loc='upper left',framealpha=0.55)
    plt.show()

def CCL():
    plt.figure(figsize=(20,12))
    
    for t in balanco_dict.keys():
        plt.plot(balanco_dict[t]["Ativo Circulante"] - balanco_dict[t]["Passivo Circulante"],alpha=0.45,lw=4)
    plt.legend([x for x in balanco_dict.keys()],loc='upper left',framealpha=0.55)
    plt.ylabel("CCL")
    plt.title("CCL Histórico == Ativo Circulante - Passivo Circulante")
    plt.show()

def ILC():
    plt.figure(figsize=(20,12))
    
    for t in balanco_dict.keys():
        plt.plot(balanco_dict[t]["Ativo Circulante"]/balanco_dict[t]["Passivo Circulante"],alpha=0.45,lw=4)
    plt.legend([x for x in balanco_dict.keys()],loc='upper left',framealpha=0.55)
    plt.ylabel("ILC")
    plt.title("Liquidez Corrente == Ativo Circulante / Passivo Circulante")
    plt.show()

def ILG():
    plt.figure(figsize=(20,12))
    
    for t in balanco_dict.keys():
        plt.plot((balanco_dict[t]["Ativo Circulante"] + balanco_dict[t]["Ativo Realizável a Longo Prazo"]) / (balanco_dict[t]["Passivo Circulante"] + balanco_dict[t]["Passivo Não Circulante"]) ,alpha=0.45,lw=4)
    plt.legend([x for x in balanco_dict.keys()],loc='upper left',framealpha=0.55)
    plt.ylabel("ILG")
    plt.title("Liquidez Geral == (AC + ARLP) / (PC + PNC)")
    plt.show()
    
def ILS():
    plt.figure(figsize=(20,12))
    
    for t in balanco_dict.keys():
        plt.plot((balanco_dict[t]["Ativo Circulante"] - balanco_dict[t]["Estoque"]) / (balanco_dict[t]["Passivo Circulante"]) ,alpha=0.45,lw=4)
    plt.legend([x for x in balanco_dict.keys()],loc='upper left',framealpha=0.55)
    plt.ylabel("ILS")
    plt.title("Liquidez Seca == (AC - Estoque) / Passivo Circulante")
    plt.show()

def capital_terceiros():
    plt.figure(figsize=(20,12))
    
    for t in balanco_dict.keys():
        plt.plot((balanco_dict[t]["Passivo Circulante"] + balanco_dict[t]["Passivo Não Circulante"]) / (balanco_dict[t]["Passivo Circulante"] + balanco_dict[t]["Passivo Não Circulante"] + balanco_dict[t]["Patrimônio Líquido Consolidado"]),alpha=0.45,lw=4)
    plt.legend([x for x in balanco_dict.keys()],loc='upper left',framealpha=0.55)
    plt.ylabel("Capital de Terceiros")
    plt.title("Participação de Capitais de Terceiros == (PC + PNC) / (PC + PNC + PL)")
    plt.show()
    
def composicao_divida():
    plt.figure(figsize=(20,12))
    
    for t in balanco_dict.keys():
        plt.plot(balanco_dict[t]["Passivo Circulante"] / (balanco_dict[t]["Passivo Circulante"] + balanco_dict[t]["Passivo Não Circulante"]),alpha=0.45,lw=4)
    plt.legend([x for x in balanco_dict.keys()],loc='upper left',framealpha=0.55)
    plt.ylabel("Composição Dívidas")
    plt.title("Composição do Endividamento == PC / (PC + PNC)")
    plt.show()
    
ticker = ["EQTL3","TAEE11","PRIO3","UNIP6","MGLU3","WEGE3","RENT3","SAPR4"]
resultado_dict = {}
balanco_dict = {}
fluxoc_dict={}

for t in ticker:
    try:
        resultado_dict[t] = get_result(t).to_dict("series")
    except:
        try:
            resultado_dict[t] = get_result(t).to_dict("series")
        except:
            pass

for t in ticker:
    try:
        balanco_dict[t] = get_balance(t).to_dict("series")
    except:
        try:
            balanco_dict[t] = get_balance(t).to_dict("series")
        except:
            pass

for t in ticker:
    try:
        fluxoc_dict[t] = get_fluxo(t).to_dict("series")
    except:
        try:
            fluxoc_dict[t] = get_fluxo(t).to_dict("series")
        except:
            time.sleep(5.5)
            pass

end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nTempo de execução: {round(elapsed_time,2)/60} minutos.")

#with open("C:/Users/pedro/OneDrive/Área de Trabalho/assets.txt", 'w') as f: 
    #for key, value in resultado_dict.items(): 
        #f.write('%s:%s\n' % (key, value))
        
#with open("C:/Users/pedro/OneDrive/Área de Trabalho/assets.txt", 'a') as f: 
    #for key, value in balanco_dict.items(): 
        #f.write('%s:%s\n' % (key, value))