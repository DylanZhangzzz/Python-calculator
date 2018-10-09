import tkinter
import math
class calculate:
    

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.minsize(420,401)
        self.root.title('Calculate Pro')

        self.value = tkinter.StringVar()
        self.value = tkinter.StringVar()
        self.value.set(0)              
        self.process = tkinter.StringVar()      
        self.process.set('')
        
        self.radVar = tkinter.IntVar()

        self.lists=[]
        self.isPressSign = False        
        self.isPressNum = False
        self.islistsclear= False
        self.layout()
        self.root.mainloop()

    def layout(self):
        label = tkinter.Label(self.root,font = ('Times',20,"bold italic"),bg = 'gray',bd ='9',fg = 'white',anchor = 'se')
        label.place(width = 420,height = 80)
        label3 = tkinter.Label(self.root,font = ('Times',30),bg = 'dark gray',bd ='9',fg = 'black',anchor = 'se')
        label3.place(y = 80,width = 420,height = 70)

        #0 to 9 buttons
        btn7 = tkinter.Button(self.root,text = '7',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda :self.number('7')).place(x = 140,y = 200,width = 70,height = 50)
        btn8 = tkinter.Button(self.root,text = '8',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda :self.number('8')).place(x = 210,y = 200,width = 70,height = 50)
        btn9 = tkinter.Button(self.root,text = '9',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda :self.number('9')).place(x = 280,y = 200,width = 70,height = 50)
 
        btn4 = tkinter.Button(self.root,text = '4',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda :self.number('4')).place(x = 140,y = 250,width = 70,height = 50)
        btn5 = tkinter.Button(self.root,text = '5',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda :self.number('5')).place(x = 210,y = 250,width = 70,height = 50)
        btn6 = tkinter.Button(self.root,text = '6',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda :self.number('6')).place(x = 280,y = 250,width = 70,height = 50)
 
        btn1 = tkinter.Button(self.root,text = '1',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda :self.number('1')).place(x = 140,y = 300,width = 70,height = 50)
        btn2 = tkinter.Button(self.root,text = '2',font = ('Times',20,"bold"), fg = 'black',bd = 0.5,command = lambda :self.number('2')).place(x = 210,y = 300,width = 70,height = 50)
        btn3 = tkinter.Button(self.root,text = '3',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda :self.number('3')).place(x = 280,y = 300,width = 70,height = 50)

        btn0 = tkinter.Button(self.root,text = '0',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda :self.number('0')).place(x = 140,y = 350,width = 140,height = 50)
        point = tkinter.Button(self.root,text = '.',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda: self.number('.')).place(x = 280,y = 350,width = 70,height = 50)
 

        #radiobutton
        angle= tkinter.Radiobutton(self.root,indicatoron=0, text = 'Angle',bg = 'orange',variable= self.radVar,value=1,command = lambda:rad).place(x = 0,y = 150,width = 70,height = 50)
        
        radian= tkinter.Radiobutton(self.root,indicatoron=0, text = 'Rad',bg = 'orange',variable= self.radVar,value=2,command = lambda:rad).place(x = 0,y = 200,width = 70,height = 50)

        Sin = tkinter.Button(self.root,text = 'sin',bg = 'orange',font = ('Times',20),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda:self.rad('s'))
        Sin.place(x = 0,y = 250,width = 70,height = 50)

        Cos = tkinter.Button(self.root,text = 'cos',bg = 'orange',font = ('Times',20),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda:self.rad('c'))
        Cos.place(x = 0,y = 300,width = 70,height = 50)

        Tan = tkinter.Button(self.root,text = 'tan',bg = 'orange',font = ('Times',20),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda:self.rad('t'))
        Tan.place(x = 0,y = 350,width = 70,height = 50)

    
        #symbols
        Back = tkinter.Button(self.root,text = 'DEL',font = ('Times',20),fg = 'orange',bd = 0.5,activebackground= 'white',command = lambda:self.back())
        Back.place(x = 140,y =150,width = 70,height = 50)

        LOG = tkinter.Button(self.root,text = 'log10',bg = 'orange',font = ('Times',20),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda:self.log10())
        LOG.place(x = 70,y = 200,width = 70,height = 50)

        Root = tkinter.Button(self.root,text = '√',bg = 'orange',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda:self.sqrts())
        Root.place(x = 70,y = 250,width = 70,height = 50)

        Power = tkinter.Button(self.root,text = 'x^y',bg = 'orange',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda:self.number('**'))
        Power.place(x = 70,y = 150,width = 70,height = 50)

        btnac = tkinter.Button(self.root,text = 'AC',bd = 0.5,font = ('Times',20,"bold"),fg = 'orange',command = lambda :self.pressCompute('AC'))
        btnac.place(x = 70,y = 300,width = 70,height = 100)
        btnback = tkinter.Button(self.root,text = '+/-',font = ('Times',20,"bold"),fg ='black',bd = 0.5,command = lambda:self.pressCompute('inv'))
        btnback.place(x = 210,y = 150,width = 70,height = 50)

        divide = tkinter.Button(self.root,text = '÷',bg = 'orange',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda:self.pressCompute('/'))
        divide.place(x = 350,y = 150,width = 70,height = 50)
  
        multiply = tkinter.Button(self.root,text ='×',bg = 'orange',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda:self.pressCompute('*'))
        multiply.place(x = 350,y = 200,width = 70,height = 50)

        subtract = tkinter.Button(self.root,text = '-',bg = 'orange',font = ('Times',20,"bold"),fg ='black',bd = 0.5,activebackground= 'white',command = lambda:self.pressCompute('-'))
        subtract.place(x = 350,y = 250,width = 70,height = 50)

        add = tkinter.Button(self.root,text = '+',bg = 'orange',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,activebackground= 'white',command = lambda:self.pressCompute('+'))
        add.place(x = 350,y = 300,width = 70,height = 50)

        equal = tkinter.Button(self.root,text = '=',bg = 'orange',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,activebackground= 'white',command=lambda :self.pressEqual())
        equal.place(x = 350,y = 350,width = 70,height = 50)

        percent = tkinter.Button(self.root,text = '%',font = ('Times',20,"bold"),fg = 'black',bd = 0.5,command = lambda:self.pressCompute('%'))
        percent.place(x = 280,y = 150,width = 70,height = 50)


    def number(self,num):
      
        if self.isPressSign == False:
            pass
       
        else:
            self.value.set(0)
            self.isPressSign = False
       
        if self.islistsclear == False:
           
            oldNum = self.value.get()
            
            if oldNum == '0':
                
                self.value.set(num)
            else:
               
                newNum = oldNum + num
                self.value.set(newNum)
        
        else:
            
            self.result.set('0')
            self.islistsclear = False
            self.result.set(num)


    def pressCompute(self,symbol):

        self.num = self.value.get()       
        self.lists.append(self.num)        
 
        self.lists.append(symbol)
        self.symbol=symbol
        self.isPressSign = True
 
        if symbol =='AC':        
            self.lists.clear()
            self.value.set(0)
    
        if symbol =='inv':
            prenum=self.value.get()
            self.value.set(float(prenum)*(-1))
            self.lists.clear()

    def sqrts(self):
        a= value.get()
        self.value.set(math.sqrt(float(a)))
        self.lists.clear()
        self.islistsclear = True
     
    def log10():
        a=value.get()
        self.value.set(math.log10(float(a)))
        self.lists.clear()
        self.islistsclear = True         

    def pressEqual():
        a = selfvalue.get()     
        self.lists.append(a)
        computrStr = ''.join(self.lists)   
        endNum = eval(computrStr)    
        self.value.set(endNum)          
        self.process.set(computrStr)     
        self.lists.clear()          
        self.islistsclear = True

    def back():
        num=self.value.get()
        a=num[0:-1]
        self.value.set(a)

    def rad(self,obj):        
        a=self.value.get()
        event=self.radVar.get()
        if event ==1:
            radnum=math.radians(float(a))
            if obj=='s':
                self.value.set(math.sin(float(radnum)))
                self.islistsclear = True
            if obj=='c':
                self.value.set(math.cos(float(radnum)))        
                self.islistsclear = True        
            if obj=='t':
                self.value.set(math.tan(float(radnum)))      
                self.islistsclear = True
      
        else:     
            if obj=='s':
                self.value.set(math.sin(float(a)))        
                self.islistsclear = True
            if obj=='c':
               self.value.set(math.cos(float(a)))
               self.islistsclear = True
            if obj=='t':
               self.value.set(math.tan(float(a)))
               self.islistsclear = True





myjsq = calculate()
