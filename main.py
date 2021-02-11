# from bs4 import BeautifulSoup
# import requests as r
# from requests.exceptions import HTTPError 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.chrome.options import Options
import time

# 1. Open FB Login Page

class Facebook:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		
		option = Options()

		option.add_argument("--disable-infobars")
		option.add_argument("start-maximized")
		option.add_argument("--disable-extensions")

		# Pass the argument 1 to allow and 2 to block
		option.add_experimental_option("prefs", { 
		    "profile.default_content_setting_values.notifications": 2 
		})

		self.driver = webdriver.Chrome(chrome_options=option, executable_path='./chromedriver.exe')
		self.driver.get('https://facebook.com')
		self.action = ActionChains(self.driver)

	def login(self):

		# Email Input
		emailInput = self.driver.find_element_by_xpath('//*[@id="email"]')
		emailInput.clear()
		emailInput.send_keys(self.email)

		# Password Input
		passwordInput = self.driver.find_element_by_xpath('//*[@id="pass"]')
		passwordInput.clear()
		passwordInput.send_keys(self.password)

		button = self.driver.find_element_by_xpath('//*[@id="u_0_d"]')
		button.send_keys(Keys.RETURN)

		# time.sleep(5)
		# self.driver.close()

	def findFriends(self):

		# fr = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[2]/div/div/div/div/label/input')
		# self.action.click(on_element=fr)

		friendSearch = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/label/input')
		friendSearch.clear()
		friendSearch.send_keys('India')
		friendSearch.send_keys(Keys.RETURN)

		time.sleep(10)
		people = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/a/div[1]/div[2]/div')
		people.click()

		time.sleep(5)

		friends = self.driver.find_elements_by_class_name('oajrlxb2')
		friend = 5
		for e in friends:
			if e.text.encode('utf-8') == b'India':
				friend = e
		friend.click()

		self.driver.execute_script('document.getElementsByClassName("hu5pjgll")[0].click()')

	def updateStatus(self):

		create = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[4]/div[1]/div[3]/span/div')
		create.click()

		time.sleep(2)

		post = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[1]')
		post.click()

		time.sleep(5)

		# inputPost = self.driver.find_element_by_xpath('//*[@id="facebook"]/body/div[3]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div')
		# inputPost.clear()
		# inputPost.send_keys("Hi! It is a nice day...")
		self.driver.execute_script('var element = document.querySelector("body > div.l9j0dhe7.tkr6xdv7 > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > form > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn > div > div > div.q5bimw55.rpm2j7zs.k7i0oixp.gvuykj2m.j83agx80.cbu4d94t.ni8dbmo4.eg9m0zos.l9j0dhe7.du4w35lb.ofs802cu.pohlnb88.dkue75c7.mb9wzai9.l56l04vs.r57mb794.kh7kg01d.c3g1iek1.buofh1pr > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 > div.o6r2urh6.buofh1pr.datstx6m.l9j0dhe7.oh7imozk > div.rq0escxv.buofh1pr.df2bnetk.hv4rvrfc.dati1w0a.l9j0dhe7.k4urcfbm.du4w35lb.gbhij3x4 > div > div > div > div > div._5rpb > div > div > div > div > span > br"); element.value = "It is a nice day"')

	def comment(self):

		profile = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]/img')
		profile.click()

		time.sleep(5)

		profileFinal = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[1]/a/div[1]/div[2]/div/div/div/div[1]/span')
		profileFinal.click()

		time.sleep(10)

		friendList = self.driver.find_elements_by_class_name('a8c37x1j')
		friends = 5
		for e in friendList:
			if e.text.encode('utf-8') == b'Friends\xef\xbb\xbf1':
				friends = e;
				print("Yellow, {0}".format(e.text.encode('utf-8')))
				break
		friends.click()

		time.sleep(10)

		friendProfiles = self.driver.find_elements_by_class_name('d3f4x2em')
		friendProfile = 5
		for e in friendProfiles:
			if e.text.encode('utf-8') == b'S\xc3\xa5ty\xc3\xa3m Kulk\xc3\xa4r\xc3\xb1\xc3\xaf':
				friendProfile = e
				print("Yellow, {0}".format(e.text.encode('utf-8')))
		friendProfile.click()

		time.sleep(10)

		comments = self.driver.find_element_by_class_name('_5rpu')
		comments.send_keys('It is Awesome')
		comments.send_keys(Keys.RETURN)

F = Facebook('eabois36@gmail.com', 'eabois')
F.login()
time.sleep(15)
# F.comment()
F.findFriends()