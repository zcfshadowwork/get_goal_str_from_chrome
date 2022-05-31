# -*- coding:utf-8 -*-

import datetime
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


def _get_goal_str(driver):
	# 从网页获取需要的元素
	# for example
	try:
		element = driver.find_element_by_class_name("xxxx")
	except NoSuchElementException as e:
		print(e)
		return None
	try:
		goal_str = element.get_property('xxx')
	except Exception as e:
		print(e)
		return None


def main():
	now = datetime.datetime.now()
	year = now.year
	month = now.month
	day = now.day
	text_name = "{0}_{1:02d}_{2:02d}.txt".format(year, month, day)
	chrome_options = Options()
	chrome_options.debugger_address="127.0.0.1:9222"
	chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
	driver = webdriver.Chrome(chrome_driver,options=chrome_options)
	for chrome_tag_name in driver.window_handles:
		driver.switch_to.window(chrome_tag_name)
		with open(text_name, 'a+') as f:
			goal_str = _get_goal_str(driver)
			if goal_str:
				f.write(goal_str + '\n')
			else
				print("{} get goal str failed".format(driver.current_url))
			driver.close()

if __name__ == "__main__":
	main()
