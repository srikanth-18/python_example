'''
def helloworld(myString) :
	print (myString)
	myName = input("What is your name?")

	print(myName)

	myVar = input('What is your variable?')

	print(myVar)
	if(myName == 'spoorthy' and myVar == '100') :
	 print("True")
	elif(myName == 'srikanth') :
	 print("False")
	else :
	 print("Everything is false");

mystring = input("Please enter a string?")
helloworld(mystring)
'''
'''
 # record
def add(num1,num2):
  return num1+num2

def subtract(num1,num2):
  return num1-num2


def multiply(num1,num2):
  return num1*num2
  

def divide(num1,num2):
  return num1/num2

def main():
	operation = input("What do you want to do(+,-,*,/)")
	if(operation != '+' and operation != '-' and operation != '*' and operation != '/'  ):
	 print("You must enter a valid operation");
	else:
	  num1 = int(input("Enter num1 "))
	  num2 = int(input("Enter num2 "))
	  if(operation == '+'):
	    print(add(num1,num2))
	  elif(operation == '-'):
	    print(subtract(num1,num2))
	  elif(operation == '*'):
	    print(multiply(num1,num2))
	  else:
	    print(divide(num1,num2))

main()		'''
'''srik = "Hey there %s  how are you %s"
var = ("spoorthy","chitti")
print(srik % var)'''
'''print('%s and %s are friends' % ('bob','taber'))'''
'''import wx
app = wx.App()
win = wx.Frame(None)
win.Show()
app.MainLoop()'''
'''from urllib import request
goog_url ='https://wordpress.org/plugins/about/readme.txt'
def download_stock_data(csv_url):
		response = request.urlopen(csv_url)
		csv = response.read()
		csv_str = str(csv)
		lines = csv_str.split("\\n")
		dest_url=r'goog.txt'
		fx= open(dest_url,"w")
		for line in lines:
		  fx.write(line+"\n")
		fx.close()

download_stock_data(goog_url)
'''
'''from urllib import request
import requests
from bs4 import BeautifulSoup
def trade_spider(max_pages):
	page=1;
	while(page<=max_pages):
		pass
		''''''url="https://buckysroom.org/trade/search.php?page="+str(page)''''''
		url="http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=mobiles"
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text,"html.parser")
		for link in soup.findAll('a',{'class':'a-link-normal'}):
		   title=link.get('title')
		   print(title)
		page+=1
trade_spider(1)	  '''
from tkinter import *
root = Tk()

menu = Menu(root)

'''topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
button1 = Button(topframe,text="Button 1",fg="purple", bg="red")
button2 = Button(bottomframe,text="Button 2",fg="green")
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
'''
root.mainloop()