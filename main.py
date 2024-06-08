from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys





chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://192.168.1.1/")


def selected_manual_band():
    is_manual_band_clicked = True
    while is_manual_band_clicked:
        try:
            driver.find_element(By.XPATH, '//*[@id="_a_bandSel"]/div/ul/li[2]').click()
            is_manual_band_clicked = False
        except:
            pass

    is_manual_band = True
    while is_manual_band:
        try:
            driver.find_element(By.XPATH,'//*[@id="band-selection-container"]/div[1]/div[4]/div/div/div/div[2]/div/div[2]/button/span').click()
            is_manual_band = False
        except:
            pass
    return True

def change_auto_manual():
    is_band_clicked = True
    while is_band_clicked:
        try:
            selected_box = driver.find_element(By.XPATH, '//*[@id="_a_bandSel"]/div/div[1]').text
            if selected_box == 'Auto':
                driver.find_element(By.XPATH, '//*[@id="_a_bandSel"]/div/div[1]').click()
                driver.find_element(By.XPATH, '//*[@id="_a_bandSel"]/div/ul/li[3]').click()
                if selected_manual_band():
                    is_band_clicked = False
            elif selected_box == 'Manual':
                driver.find_element(By.XPATH, '//*[@id="_a_bandSel"]/div/div[1]').click()
                driver.find_element(By.XPATH, '//*[@id="_a_bandSel"]/div/ul/li[2]').click()
                is_band_clicked = False
        except:
            pass
    return True


def net_status():
    is_status = True
    while is_status:
        try:
            status = driver.find_element(By.XPATH, '//*[@id="a_internetStatus"]', )
            is_status = False
        except:
            pass

    is_appear = True
    while is_appear:
        net_status = status.get_attribute('value')
        if net_status == 'Connected' or net_status == "Disconnected":
            is_appear = False
    return net_status


def login():
    login = driver.find_element(By.CSS_SELECTOR, "#pc-login-password")
    login.send_keys("18082746", Keys.ENTER)
    try:
        confirm = driver.find_element(By.CSS_SELECTOR, "#confirm-yes")
        confirm.click()
    except:
        pass
    return True


def enter_advanced_menu():
    is_advanced = True
    while is_advanced:
        try:
            advanced = driver.find_element(By.CSS_SELECTOR, ".T_adv").click()
            is_advanced = False
        except:
            pass
    return True


def enter_network_menu():
    is_network = True
    while is_network:
        try:
            network = driver.find_element(By.CSS_SELECTOR, "#internet").click()
            is_network = False
        except:
            pass


def enter_internet_menu():
    is_internet = True
    while is_internet:
        try:
            internet = driver.find_element(By.XPATH, '//*[@id="menuTree"]/li[3]/ul/li[1]/a').click()
            is_internet = False
        except:
            pass
    return True

def menu_enter():
    enter_advanced_menu()
    enter_network_menu()
    enter_internet_menu()


def main():
    login()
    menu_enter()
    is_ok = True
    while is_ok:
        if net_status() == 'Disconnected':
            change_auto_manual()

        elif net_status() == 'Connected':
            is_ok = False


    print(net_status())







main()



















