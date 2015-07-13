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
import wx
from urllib.request import urlopen
class Test(wx.Frame):
	def __init__(self,parent,id):
	   wx.Frame.__init__(self,parent,id,'Frame Name',size=(300,300))
	   
	   panel = wx.Panel(self)
	   '''status = self.CreateStatusBar()
	   button = wx.Button(panel,label='exit',pos=(130,10),size=(60,60))
	   self.Bind(wx.EVT_BUTTON,self.closebutton,button)
	   self.Bind(wx.EVT_CLOSE,self.closewindow)
	   menubar = wx.MenuBar()
	   first = wx.Menu()
	   second = wx.Menu()
	   first.Append(wx.NewId(),"New Window","this is a new window")
	   first.Append(wx.NewId(),"Open....","This opens a  new window")
	   menubar.Append(first,'File')
	   menubar.Append(second,'Edit')
	   self.SetMenuBar(menubar)'''
	   '''box=wx.MessageDialog(None,'Are you good?','Goodness',wx.YES_NO)
	   answer = box.ShowModal()
	   box.Destroy()'''
	   '''box = wx.TextEntryDialog(None,"What's your name?",'YOUR Name',"please type your name")
	   if(box.ShowModal()==wx.ID_OK):
	    answer=box.GetValue()'''
	   wx.StaticText(panel,-1,"This is a static Text",(10,10))
	   custom = wx.StaticText(panel,-1,"This is a static Text",(10,30),(360,-1),wx.ALIGN_CENTER)
	   custom.SetForegroundColour('white')
	   custom.SetBackgroundColour('blue')
	   slider=wx.Slider(panel,-1,50,1,100,pos=(10,60),size=(250,-1),style=wx.SL_AUTOTICKS | wx.SL_LABELS)	  
	   spinner = wx.SpinCtrl(panel,-1,"",(10,120),(90,-1),style=wx.SP_WRAP)
	   spinner.SetRange(1,100)
	   spinner.SetValue(10)
	   wx.CheckBox(panel,-1,"Apples",(10,230),(160,-1))
	   mylist=['tuna','beef','cereals','cannon']
	   cunt=wx.ListBox(panel,-1,(10,150),(80,60),mylist,style=wx.LB_SINGLE)
	   cunt.SetSelection(2)
	   modal = wx.SingleChoiceDialog(None,"What's your favourite food","Food",mylist)
	   if(modal.ShowModal()==wx.ID_OK):
	    wx.StaticText(panel,-1,"My favourite food is "+(modal.GetStringSelection()),(10,250))
	   modal.Destroy()
	def closebutton(self,event)   :
		self.Close(True)
	def closewindow(self,event) :
		self.Destroy()
if(__name__=='__main__'):
	app=wx.App()
	frame = Test(parent=None,id=-1)
	frame.Show()
	app.MainLoop()