import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('chromedriver.exe')

driver = webdriver.Chrome(service=service)

driver.get("https://ya.ru")

driver.maximize_window()

# for cookie in cookies:
#     driver.add_cookie(cookie)
#
# driver.refresh()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "home-link2")))

services_link = driver.find_element(By.CSS_SELECTOR,
									"a.home-link2.headline__personal-item.headline__personal-item_services")

services_link.click()

try:
	popup_element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "services-more-popup"))
	)

	classes = popup_element.get_attribute("class").split()
	assert "services-more-popup_headline" in classes
	assert "services-more-popup_pinnable_yes" in classes

	print("Тест 1 пройден. Элемент div с нужным классом появился.")


except Exception as e:
	print("Тест 1 не пройден. Элемент не найден или произошла ошибка:", e)

driver.refresh()

try:
	alice_fab_button = driver.find_element(By.CSS_SELECTOR, "button.alice-fab")

	alice_fab_button.click()

	alice_element = WebDriverWait(driver, 40).until(
		EC.presence_of_element_located((By.CLASS_NAME, "scrollbar"))
	)

	alice_classes = alice_element.get_attribute("class").split()
	assert "scrollbar" in alice_classes
	assert "scrollbar_theme_light" in alice_classes
	assert "svelte-pwsra" in alice_classes

	print("Тест 2 пройден. Элемент div с классом scrollbar появился.")

except Exception as e:
	print("Тест 2 не пройден. Элемент не найден или произошла ошибка:", e)

driver.refresh()

try:
	camera_button = driver.find_element(By.CSS_SELECTOR, "button.mini-suggest__action.search3__action.search3__camera")

	camera_button.click()

	camera_popup = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "Popup2"))
	)

	camera_popup_classes = camera_popup.get_attribute("class").split()
	assert "Popup2_visible" in camera_popup_classes
	assert "CbirPanelPopup2" in camera_popup_classes

	print("Тест 3 пройден. Элемент div с классом Popup2_visible CbirPanelPopup2 появился.")

except Exception as e:
	print("Тест 3 не пройден. Ошибка:", e)

driver.refresh()

try:
	weather_link = driver.find_element(By.CSS_SELECTOR,
									   "a.home-link2.informers3__item.informers3__weather.home-link2_color_inherit.home-link2_hover_tertiary")

	weather_link.click()

	time.sleep(2)
	driver.switch_to.window(driver.window_handles[-1])

	assert "yandex.ru/pogoda/" in driver.current_url
	print("Тест 4 пройден. Открылась вкладка с адресом, содержащим 'yandex.ru/pogoda/'.")

	driver.close()
	driver.switch_to.window(driver.window_handles[0])

except Exception as e:
	print("Тест 4 не пройден. Ошибка:", e)

driver.refresh()

try:
	voice_button = driver.find_element(By.CSS_SELECTOR, "button.mini-suggest__action.search3__voice.search3__action")

	voice_button.click()

	voice_popup = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "simple-popup__content"))
	)

	print("Тест 5 пройден. Элемент div с классом simple-popup__content появился.")

except Exception as e:
	print("Тест 5 не пройден. Ошибка:", e)

driver.quit()
