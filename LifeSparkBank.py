#LifeSpark Bank
#Made by Ishan and Yash  


from tkinter import *
from tkinter.ttk import Combobox

import mysql.connector

c = 'C:\\Users\\acer\\Desktop\\InvestigatoryProject\\PythonProject\\Bank Management System_project\\images\\Background.gif'#image of background
d = 'C:\\Users\\acer\\Desktop\\InvestigatoryProject\\PythonProject\\Bank Management System_project\\images\\favicon.ico'#image of bulb icon
e = 'C:\\Users\\acer\\Desktop\\InvestigatoryProject\\PythonProject\\Bank Management System_project\\images\\lifespark.gif'#image of title :- LIFESPARK BANK
f = 'C:\\Users\\acer\\Desktop\\InvestigatoryProject\\PythonProject\\Bank Management System_project\\images\\dashboard.gif'#image of dashboard
g = 'C:\\Users\\acer\\Desktop\\InvestigatoryProject\\PythonProject\\Bank Management System_project\\images\\registration.gif'#image of registration
h = 'C:\\Users\\acer\\Desktop\\InvestigatoryProject\\PythonProject\\Bank Management System_project\\images\\update.gif' #image of update
i = 'C:\\Users\\acer\\Desktop\\InvestigatoryProject\\PythonProject\\Bank Management System_project\\images\\deposit.gif' #image of deposit
j = 'C:\\Users\\acer\\Desktop\\InvestigatoryProject\\PythonProject\\Bank Management System_project\\images\\withdraw.gif' #image of withdraw
k = 'C:\\Users\\acer\\Desktop\\InvestigatoryProject\\PythonProject\\Bank Management System_project\\images\\transfer.gif' #image of transfer




mydb = mysql.connector.connect(
  host="localhost",
  user="root",             #Enter your system's mysql username
  passwd="password",       #and password
  database="LifesparkBank" 
)

mycursor = mydb.cursor()
'''--------------------USE THESE TO CREATE NEW DATABASE OR TABLE IF NOT EXIST-----------------------'''
mycursor.execute('CREATE DATABASE IF NOT EXISTS LifeSparkBank')
mycursor.execute('''CREATE TABLE if not exists Accounts (Accno INT(5)ZEROFILL AUTO_INCREMENT PRIMARY KEY,
                                           fname varchar(20),
                                           lname varchar(20),
                                           DOB DATE,
                                           Mobile_number varchar(11) ,
                                           email varchar(25),
                                           City varchar(20),
                                           PINCODE int,
                                           Balance_amount int,
                                           password varchar(40))''')
#mycursor.execute('DROP table accounts')
'''-----------------------------------------WINDOWS--------------------------------------'''
def opwin1():
    global background_image1
    global background_image17

    
    HEIGHT = 600
    WIDTH = 650
    top = Toplevel()
    top.title('BANK MANAGEMENT')
    top.iconbitmap(d)
    
    canvas1 = Canvas(top, height = HEIGHT , width = WIDTH)
    canvas1.pack()
  
    background_image1 = PhotoImage(file=c)
    background_label1 = Label (top, image = background_image1)
    background_label1.place(relwidth =1 ,relheight =1)

    background_image17 = PhotoImage(file= f )
    background_label17 = Label (top, image = background_image17)
    background_label17.place(relwidth = 1 ,relheight = 0.15)


    

    frame3 = Frame (top, bg = "#80c1ff",bd =5)
    frame3.place(relx =0.1 , rely =0.18, relwidth = 0.35, relheight = 0.3 )

    frame3 = Frame (top, bg = "#80c1ff",bd =5)
    frame3.place(relx =0.1 , rely =0.58, relwidth = 0.35, relheight = 0.3 )


    frame4 = Frame (top, bg = "#80c1ff",bd =5)
    frame4.place(relx =0.57 , rely =0.18, relwidth = 0.35, relheight = 0.3 )

    frame4 = Frame (top, bg = "#80c1ff",bd =5)
    frame4.place(relx =0.57 , rely =0.58, relwidth = 0.35, relheight = 0.3 )

#-----------------------------------withdraw function-------------------------------------------------
    
    def opwin2 (): 

        
        global background_image2
        global background_image21
        HEIGHT = 600
        WIDTH = 650
        top1 = Toplevel()
        top1.title('BANK MANAGEMENT')
        top1.iconbitmap(d)
        canvas2 = Canvas(top1, height = HEIGHT , width = WIDTH)
        canvas2.pack()
  
        background_image2 = PhotoImage(file=c)
        background_label2 = Label (top1, image = background_image2)
        background_label2.place(relwidth =1 ,relheight =1)

        background_image21 = PhotoImage(file=j)
        background_label21 = Label (top1, image = background_image21)
        background_label21.place(relwidth =1 ,relheight =0.15)

        l4 = Label(top1, text = "Amount:", font = ' bold 36')
        l4.place(relx= 0.07, rely =0.47)

        frame5 = Frame (top1, bg = "#80c1ff",bd =5)
        frame5.place(relx =0.37 , rely =0.43, relwidth = 0.6, relheight = 0.2 )

        e3 = Entry(frame5 , font = 'bold 40')
        e3.place (relwidth = 0.6 , relheight = 1,anchor = 'nw')#withdraw

        def withdraw():
                withdraw_amount=e3.get()
                val=(withdraw_amount,fname,lname,passwd)
                sql='UPDATE accounts SET balance_amount=balance_amount-(%s)WHERE fname=%s AND lname=%s AND password=%s'

                mycursor.execute(sql,val)
                mydb.commit()
                opwin3()
      

        

        def opwin3 () :
            global background_image3
            HEIGHT = 600
            WIDTH = 650
            top2 = Toplevel()
            top2.title('BANK MANAGEMENT')
            top2.iconbitmap(d)
            canvas3 = Canvas(top2, height = HEIGHT , width = WIDTH)
            canvas3.pack()
  
            background_image3 = PhotoImage(file= c)
            background_label3 = Label (top2, image = background_image3)
            background_label3.place(relwidth =1 ,relheight =1)

            l5 = Label(top2, text = "Money had been withdrawn.", font = ' bold 36')
            l5.place(relx= 0.07, rely =0.42)

            
            l6 = Label(top2, text = "           Visit Again !!", font = ' bold 36')
            l6.place(relx= 0.07, rely =0.51)
            
        b4 = Button(top1,text = "ENTER",font = ' bold 30',bg = 'white', command = withdraw)
        b4.place(relx =0.74 , rely =0.44, relwidth = 0.22, relheight = 0.18 )
    b2 = Button(top,text = "WITHDRAW",font = ' bold 27',bg = 'white', command = opwin2)
    b2.place(relx =0.11,rely = 0.19,relwidth = 0.33, relheight = 0.28)

#----------------------------------------Deposit-----------------------------------------------
    def opwin6 ():
        
        global background_image2
        global background_image20
        HEIGHT = 600
        WIDTH = 650
        top6 = Toplevel()
        top6.title('BANK MANAGEMENT')
        top6.iconbitmap(d)
        canvas6 = Canvas(top6, height = HEIGHT , width = WIDTH)
        canvas6.pack()
  
        background_image2 = PhotoImage(file= c)
        background_label2 = Label (top6, image = background_image2)
        background_label2.place(relwidth =1 ,relheight =1)

        background_image20 = PhotoImage(file= i)
        background_label20 = Label (top6, image = background_image20)
        background_label20.place(relwidth =1 ,relheight =0.15)

        l6 = Label(top6, text = "Amount:", font = ' bold 36')
        l6.place(relx= 0.07, rely =0.47)

        frame6 = Frame (top6, bg = "#80c1ff",bd =5)
        frame6.place(relx =0.37 , rely =0.43, relwidth = 0.6, relheight = 0.2 )

        e6 = Entry(frame6 , font = 'bold 40')
        e6.place (relwidth = 0.6 , relheight = 1,anchor = 'nw')#deposit

        def deposit():
                add_amount=e6.get()
      
                val=(add_amount,fname,lname,passwd)
                sql='UPDATE accounts SET balance_amount=balance_amount+(%s)WHERE fname=%s AND lname=%s AND password=%s'
      
                mycursor.execute(sql,val)
                mydb.commit()
                opwin7()
      
      

        

        def opwin7 () :
            global background_image3
            HEIGHT = 600
            WIDTH = 650
            top7 = Toplevel()
            top7.title('BANK MANAGEMENT')
            top7.iconbitmap(d)
            canvas7 = Canvas(top7, height = HEIGHT , width = WIDTH)
            canvas7.pack()
  
            background_image3 = PhotoImage(file= c)
            background_label3 = Label (top7, image = background_image3)
            background_label3.place(relwidth =1 ,relheight =1)

            l7 = Label(top7, text = "Money had been Deposited.", font = ' bold 36')
            l7.place(relx= 0.07, rely =0.42)

            
            l8= Label(top7, text = "             Visit Again !!", font = ' bold 36')
            l8.place(relx= 0.07, rely =0.51)
            
        b11 = Button(top6,text = "ENTER",font = ' bold 30',bg = 'white', command = deposit)
        b11.place(relx =0.74 , rely =0.44, relwidth = 0.22, relheight = 0.18 )

    b10 = Button(top,text = "DEPOSIT",font = ' bold 27',bg = 'white', command = opwin6)
    b10.place(relx =0.11,rely = 0.59,relwidth = 0.33, relheight = 0.28)

#--------------------------------------Transfer

    def opwin8 ():
        
        global background_image2
        global background_image22
        HEIGHT = 600
        WIDTH = 650
        top1 = Toplevel()
        top1.title('BANK MANAGEMENT')
        top1.iconbitmap(d)
        canvas2 = Canvas(top1, height = HEIGHT , width = WIDTH)
        canvas2.pack()
  
        background_image2 = PhotoImage(file= c)
        background_label2 = Label (top1, image = background_image2)
        background_label2.place(relwidth =1 ,relheight =1)

        background_image22 = PhotoImage(file= k)
        background_label22 = Label (top1, image = background_image22)
        background_label22.place(relwidth =1 ,relheight =0.15)

        l4 = Label(top1, text = "Amount:", font = ' bold 36')
        l4.place(relx= 0.07, rely =0.53)

        frame5 = Frame (top1, bg = "#80c1ff",bd =5)
        frame5.place(relx =0.37 , rely =0.49, relwidth = 0.6, relheight = 0.2 )

        e345 = Entry(frame5 , font = 'bold 40')
        e345.place (relwidth = 0.6 , relheight = 1,anchor = 'nw')#transfer amount

        l12 = Label(top1, text = "Account no. of reciever :", font = ' bold 20')
        l12.place(relx= 0.07, rely =0.25)

        frame12 = Frame (top1, bg = "#80c1ff",bd =5)
        frame12.place(relx =0.07 , rely =0.32, relwidth = 0.6, relheight = 0.08 )

        e126 = Entry(frame12 , font = 'bold 20')
        e126.place (relwidth = 1 , relheight = 1,anchor = 'nw')#account no. of reciever

        frame112 = Frame (top1, bg = "#80c1ff",bd =5)
        frame112.place(relx =0.42 , rely =0.40, relwidth = 0.6, relheight = 0.08 )
        
        l12 = Label(top1, text = "Name of reciever :", font = ' bold 20')
        l12.place(relx= 0.07, rely =0.40)
        
        ename= Entry(frame112, font = 'bold 20')
        ename.place(relwidth=0.6 , relheight=1,anchor = 'nw')
                   

        def transfer():
            
                fname=ename.get()
                accno=e126.get()
                amount=e345.get()
                
                val=(amount,accno,fname)
                sql= 'UPDATE accounts SET balance_amount=balance_amount+(%s) WHERE accno=%s AND fname=%s'
                mycursor.execute(sql,val)

                ifname=e123.get()
                ilname=e223.get()
                iaccno=e1.get()
                
                val1=(amount,iaccno,ifname)
                sql1= 'UPDATE accounts SET balance_amount=balance_amount-(%s) WHERE accno=%s AND fname=%s'
                
                mycursor.execute(sql1,val1)
                mydb.commit()
                opwin5()



        def opwin5 () :
            global background_image3
            HEIGHT = 600
            WIDTH = 650
            top2 = Toplevel()
            top2.title('BANK MANAGEMENT')
            top2.iconbitmap(d)
            canvas3 = Canvas(top2, height = HEIGHT , width = WIDTH)
            canvas3.pack()
  
            background_image3 = PhotoImage(file= c)
            background_label3 = Label (top2, image = background_image3)
            background_label3.place(relwidth =1 ,relheight =1)

            l5 = Label(top2, text = "Money had been Transferred.", font = ' bold 36')
            l5.place(relx= 0.04, rely =0.42)

            
            l6 = Label(top2, text = "             Visit Again !!", font = ' bold 36')
            l6.place(relx= 0.07, rely =0.51)


            
        b4 = Button(top1,text = "ENTER",font = ' bold 30',bg = 'white', command = transfer)
        b4.place(relx =0.74 , rely =0.50, relwidth = 0.22, relheight = 0.18 )


    


    b8 = Button(top,text = "TRANSFER",font = ' bold 27',bg = 'white', command = opwin8 )
    b8.place(relx =0.58,rely = 0.19,relwidth = 0.33, relheight = 0.28)




    
'-------------------------------------Login-------------------------------------------------'''

HEIGHT = 600
WIDTH =  650

window = Tk()
window.title(" BANK MANAGEMENT")
window.iconbitmap(d)
canvas = Canvas(window, height = HEIGHT , width = WIDTH)
canvas.pack()

background_image = PhotoImage(file= c)

background_label = Label (window, image = background_image)
background_label.place(relwidth =1 ,relheight =1)

background_image16 = PhotoImage(file= e )
background_label16 = Label (window, image = background_image16)
background_label16.place(relwidth = 1 ,relheight = 0.185)





l123 = Label(window, text = "First Name*", font = {'Helvetica',10})
l123.place(relx= 0.1, rely =0.27)

l223 = Label(window, text = "Last Name*",font = {'Helvetica',10})
l223.place(relx= 0.5, rely =0.27)

frame123 = Frame (window, bg = "#80c1ff",bd =5)
frame123.place(relx =0.1 , rely =0.32, relwidth = 0.35, relheight = 0.06 )

frame223 = Frame (window, bg = "#80c1ff",bd =5)
frame223.place(relx =0.5 , rely =0.32, relwidth = 0.35, relheight = 0.06 )

e123 = Entry(frame123 , font =40)
e123.place (relwidth = 1 , relheight = 1)#first name login

e223 = Entry(frame223 , font =40)
e223.place (relwidth = 1 , relheight = 1)#last name login



l1 = Label(window, text = "Account No.*", font = {'Helvetica',10})
l1.place(relx= 0.1, rely =0.4)

l2 = Label(window, text = "Pasword*",font = {'Helvetica',10})
l2.place(relx= 0.1, rely =0.53)

l3 = Label(window, text = "Don't have an account ? Try signing up.")
l3.place(relx= 0.1, rely =0.64)

frame1 = Frame (window, bg = "#80c1ff",bd =5)
frame1.place(relx =0.1 , rely =0.45, relwidth = 0.7, relheight = 0.06 )

frame2 = Frame (window, bg = "#80c1ff",bd =5)
frame2.place(relx =0.1 , rely =0.58, relwidth = 0.7, relheight = 0.06 )

e1 = Entry(frame1 , font =40)
e1.place (relwidth = 1 , relheight = 1)#account no. login

e2 = Entry(frame2 , font =40, show = '*')
e2.place (relwidth = 1 , relheight = 1)#password login



def login():
    
      global fname,lname, Accno, passwd
      fname = e123.get()
      lname = e223.get()
      Accno = e1.get()
      passwd= e2.get()
      
      mycursor = mydb.cursor(buffered=True)

      #Exception handling, i,e. calling out for wrong login credentials
      
      mycursor.execute("SELECT Accno,fname,password,lname FROM accounts")
      table_data = mycursor.fetchall()
      
      for i in range (0,len(table_data)):
            
            if table_data[i][1]==fname and table_data[i][2]==passwd and table_data[i][3]==lname:      
                  val=(fname,lname,passwd)
                  sql="SELECT * FROM accounts WHERE fname = %s AND lname= %s AND password=%s"
                  
                  
                  mycursor.execute(sql,val)
                  mydb.commit()
                  opwin1()
                  break
                  
            
            else:
                  print("The information entered is incorrect,please try again")
                  continue
                  login()
       

b1 = Button(window,text = "Login",font = 40,bg = '#80c1ff',command = login)
b1.place(relx =0.77,rely = 0.73)



'''-------------------------------------------Registration Function-------------------------------------------'''

def opwin4 ():
            global background_image4
            global background_image18
            global  combo
            HEIGHT = 600
            WIDTH = 650
            top3 = Toplevel()
            top3.title('BANK MANAGEMENT')
            top3.iconbitmap(d)
  

            
            canvas4 = Canvas(top3, height = HEIGHT , width = WIDTH)
            canvas4.pack()



                    


            


              
            background_image4 = PhotoImage(file= c)
            background_label4 = Label (top3, image = background_image4)
            background_label4.place(relwidth =1 ,relheight =1)

            background_image18 = PhotoImage(file= g  )
            background_label18 = Label (top3, image = background_image18)
            background_label18.place(relwidth = 1 ,relheight = 0.15)

            frame6 = Frame (top3, bg = "#80c1ff",bd =5)
            frame6.place(relx =0.1 , rely =0.28, relwidth = 0.43, relheight = 0.06 )

            l5 = Label(top3, text = "First Name", font = '40')
            l5.place(relx = 0.11, rely = 0.29,relwidth= 0.15, relheight = 0.04)

            e34 = Entry(top3 , font = ' 40')
            e34.place (relx= 0.27 , rely= 0.29  ,relwidth = 0.25 , relheight = 0.04 ) # first name register

            frame61 = Frame (top3, bg = "#80c1ff",bd =5)
            frame61.place(relx =0.5 , rely =0.28, relwidth = 0.43, relheight = 0.06 )

            l51 = Label(top3, text = "Last Name", font = '40')
            l51.place(relx = 0.51, rely = 0.29,relwidth= 0.15, relheight = 0.04)

            e31 = Entry(top3 , font = ' 40')
            e31.place (relx= 0.67 , rely= 0.29  ,relwidth = 0.25 , relheight = 0.04 ) #last name register

            
            frame7 = Frame (top3, bg = "#80c1ff",bd =5)
            frame7.place(relx =0.1 , rely =0.35, relwidth = 0.4, relheight = 0.06 )

            l6 = Label(frame7, text = "Gender", font = '40')
            l6.place(relwidth= 0.23, relheight = 1)

            v12 = [ 'Male','Female','Rather not say' ]
            combo = Combobox ( top3 ,values = v12 ,   font ={'Helvetica',10} )
            combo.place (relx= 0.21 , rely= 0.36  ,relwidth = 0.28 , relheight = 0.04 ) # gender register
            
            

            frame8 = Frame (top3, bg = "#80c1ff",bd =5)
            frame8.place(relx =0.1 , rely =0.42, relwidth = 0.59, relheight = 0.06 )

            l7 = Label(top3, text = "Date of birth", font = '40')
            l7.place(relx= 0.11 , rely= 0.43  ,relwidth = 0.14 , relheight = 0.04 )

            


            
            d1 = Entry( top3 ,   font ={'Helvetica',10} )
            d1.place (relx= 0.31 , rely= 0.43  ,relwidth = 0.07 , relheight = 0.04 ) #combobox day register

            l7 = Label(top3, text = "Date", font = '40')
            l7.place(relx= 0.26 , rely= 0.43  ,relwidth = 0.05 , relheight = 0.04)

            
            d2 = Entry( top3 , font ={'Helvetica',10} )
            d2.place (relx= 0.45 , rely= 0.43  ,relwidth = 0.07 , relheight = 0.04 ) #combobox month register

            l7 = Label(top3, text = "Month", font = '40')
            l7.place(relx= 0.38 , rely= 0.43  ,relwidth = 0.07 , relheight = 0.04)


            

            d3 = Entry( top3 ,font ={'Helvetica',10} )
            d3.place (relx= 0.58 , rely= 0.43  ,relwidth = 0.1 , relheight = 0.04 ) #combobox year register

            l7 = Label(top3, text = "Year", font = '40')
            l7.place(relx= 0.52 , rely= 0.43  ,relwidth = 0.06 , relheight = 0.04)

            
            frame9 = Frame (top3, bg = "#80c1ff",bd =5)
            frame9.place(relx =0.1 , rely =0.49, relwidth = 0.52, relheight = 0.06 )

            l7 = Label( top3, text = "Mobile No.", font = '40')
            l7.place(relx = 0.11  , rely= 0.50  ,relwidth= 0.14, relheight = 0.04)

            
            e6 = Entry(top3 , font = ' 40')
            e6.place (relx= 0.42 , rely= 0.50  ,relwidth = 0.19 , relheight = 0.04 ) # mobile no. register

            v = ['(AFG)''+93','(ALB)''+355','(DZA)''+213','(ASM)' '+1','(AND)' '+376', '(AGO)''+244','(ANG)' '+1','(ATG)' '+1', '(ARG)''+54','(ARM)' '+374',
                '(ABW)' '+297','(AUS)' '+61', '(AUT)''+43', '(AZE)''+994','(BHS)' '+1','(BHR)' '+973', '(BGD)''+880',
                 '(BRB)''+1','(BLR)' '+375','(BEL)' '+32','(BLZ)' '+501','(BEN)' '+229', '(BMU)''+1','(BTN)' '+975',
                '(BOL)' '+591','(BIH)' '+387','(BWA)' '+267','(BRA)' '+55','(BRN)' '+673', '(BGR)''+359','(BFA)' '+226',
                '(BDI)' '+257', '(KHM)''+855','(CMR)' '+237','(CAN )''+1','(CPV)' '+238','(CYM )''+1','(CAF)' '+236',
                '(TCD)''+235','(CHL)''+56','(CHN)' '+86','(CXR)' '+61', '(CCK)''+61', '(COL)''+57','(COM)' '+269',
                '(COD)' '+242','(COK)'  '+682','(CRI)' '+506','(CIV)' '+225','(HRV)' '+385','(CUB)''+53',
                '(CYP)' '+357','(CZE)' '+420','(DNK)''+45' ,'(DJI)''+253' ,'(DMA)''+1' ,'(DOM)''+1','(ECU)''+593','(EGY)''+20',
                '(SLV)' '+503', '(GNQ)' '+240', '(ERI)' '+291','(EST)' '+372',  '(ETH)''+251', '(FLK)' '+500',
                '(FRO)' '+298', '(FJI)' '+679', '(FIN)' '+358','(FRA)''+33','(GUF)'  '+594', '(PYF)' '+689',
                '(GAB)''+241', '(GMB)' '+220', '(GEO )' '+995', '(DEU)' '+49','(GHA)'  '+233','(GIB)'  '+350',
                '(GRC)' '+30', '(GRL)' '299', '(GRD)''+1', '(GLP)' '+590','(GUM)'  '+1','(GTM )' '+502','(GIN)'  '+224', '(GNB)' '+245',
                '(GUY)' '+592', '(HTI)' '+509', '(VAT)' '+379', '(HND)' '+504', '(HKG)' '+852','(HUN)' '+36', '(ISL)' '+354',  '(IND)''+91',
                '(IDN)' '+62', '(IRN)' '+98','(IRQ)'  '+964', '(IRL)' '+353','(ISR)'  '+972', '(ITA)' '+39',  '(JAM)' '+876' ,'(JPN)' '+81','(JOR)' '+962',
                 '(KAZ)''+7','(KEN)'  '+254', '(KIR)' '+686','(PRK)'  '+850', '(KOR)' '+82','(KWT)'  '+965', '(KGZ)' '+996','(LAO)'  '+856',
                 '(LVA)''+371', '(LBN)' '+961', '(LSO)''+266','(LBR)'  '+231', '(LBY)' '+218','(LIE)'  '+423',  '(LTU)' '+370','(LUX)'  '+352',
                '(MAC)' '+853','(MKD)'  '+389', '(MDG)' '+261','(MWI)'  '+265','(MYS)' '+60', '(MDV)' '+960', '(MLI)' '+223', '(MLT)' '+356',
                '(MHL)' '+692',  '(MTQ)''+596', '(MRT)' '+222','(MUS)'  '+230', '(MYT)' '+262', '(MEX)' '+52','(FSM)' '+691', '(MDA)' '+373',
                '(MCO)' '+377', '(MNG)' '+976', '(MNE)' '+382', '(MSR)' '+1', '(MAR)' '+212', '(MOZ)' '+258', '(MMR)' '+95','(NAM)' '+264',
                 '(NRU)' '+674','(NPL)' '+977','(NLD)'  '+31','(ANT)'  '+599', '(NCL)' '+687', '(NZL)' '+64', '(NIC)' '+505','(NER)'  '+227',
                '(NGA)' '+234',  '(NIU)' '+683', '(NFK)' '+672', '(MNP)' '+1' ,'(NOR)''+47', '(OMN)' '+968', '(PAK)' '+92','(PLW)'  '+680',
                 '(PSE)''+970', '(PAN)' '+507', '(PNG)' '+675', '(PRY)' '+595', '(PER)' '+51','(PHL)'  '+63', '(PCN)' '+870','(POL)' '+48',
                 '(PRT)''+351', '(PRI)' '+1', '(QAT)' '+974','(REU)'  '+262', '(ROU)' '+40', '(RUS)' '+7','(RWA)'  '+250','(SHN)'  '+290','(KNA)'  '+1',
                '(LCA)' '+1','(SPM)'  '+508', '(VCT)''+1', '(WSM)' '+685', '(SMR)' '+378', '(STP)' '+239', '(SAU)' '+966', '(SEN)' '+221',
                '(SRB)' '+381','(SYC)'  '+248', '(SLE)' '+232', '(SGP)' '+65','(SVK)'  '+421','(SVN)' '+386', '(SLB)' '+677', '(SOM)' '+252',
                 '(ZAF)' '+27', '(ESP)' '+34','(LKA)'  '+94', '(SDN)' '+249', '(SUR)' '+597','(SJM0' '+47','(SWZ)'  '+268','(SWE)'  '+46','(CHE)' '+41',
                '(SYR0' '+963', '(TWN)' '+886','(TJK)'  '+992','(TZA)'  '+255', '(THA)' '+66', '(TGO)'   '+228','(TKL)'  '+690',
               '(TON)'  '+676', '(TTO)' '+1', '(TUN)'  '+216','(TUR)' '+90','(TKM)'  '+993','(TCA)'  '+1', '(TUV)' '+688','(UGA)'  '+256','(UKR)'  '+380',
                 '(ARE)''+971', '(GBR)' '+44', '(USA)' '+1', '(URY)' '+598','(UZB)' '+998','(VUT)'  '+678','(VEN)'  '+58', '(VNM)' '+84', '(VIR)' '+1',
                 '(WLF)'  '+681','(YEM)'  '+967', '(ZMB)' '+260', '(ZWE)' '+263'  ]


            combo = Combobox ( top3 ,values = v ,   font ={'Helvetica',10},  )
            combo.place (relx= 0.26 , rely= 0.50 ,relwidth = 0.16 , relheight = 0.04 ) # combobox mobile no. country code register

            
            

            frame7 = Frame (top3, bg = "#80c1ff",bd =5)
            frame7.place(relx =0.1 , rely =0.56, relwidth = 0.4, relheight = 0.06 )


            

            l6 = Label(frame7, text = "Email", font = '40')
            l6.place(relwidth= 0.23, relheight = 1)

            
            e48 = Entry(top3 , font = ' 40')
            e48.place (relx= 0.21 , rely= 0.57  ,relwidth = 0.28 , relheight = 0.04 )#email register

            
            
            frame6 = Frame (top3, bg = "#80c1ff",bd =5)
            frame6.place(relx =0.1 , rely =0.63, relwidth = 0.36, relheight = 0.06 )

            l5 = Label(top3, text = "City", font = '40')
            l5.place(relx = 0.11    ,rely = 0.64    ,relwidth= 0.07, relheight = 0.04)

            e38 = Entry(top3 , font = ' 40')
            e38.place (relx= 0.19 , rely= 0.64  ,relwidth = 0.26 , relheight = 0.04 )#city register


            frame7 = Frame (top3, bg = "#80c1ff",bd =5)
            frame7.place(relx =0.1 , rely =0.7, relwidth = 0.29, relheight = 0.06 )


            

            l6 = Label(top3, text = "Pincode", font = '40')
            l6.place(relx = 0.11  ,rely = 0.71   ,relwidth= 0.1, relheight = 0.04)

            
            e47 = Entry(top3 , font = ' 40')
            e47.place (relx= 0.22 , rely= 0.71  ,relwidth = 0.16 , relheight = 0.04 )#pincode register

            frame10 = Frame (top3, bg = "#80c1ff",bd =5)
            frame10.place(relx =0.1 , rely =0.76, relwidth = 0.29, relheight = 0.06 )


            

            l10 = Label(top3, text = "Balance ", font = '40')
            l10.place(relx = 0.11  ,rely = 0.76   ,relwidth= 0.1, relheight = 0.04)

            
            bl1 = Entry(top3 , font = ' 40')
            bl1.place (relx= 0.22 , rely= 0.76  ,relwidth = 0.16 , relheight = 0.04 )#Balance
             
            
            frame7 = Frame (top3, bg = "#80c1ff",bd =5)
            frame7.place(relx =0.1 , rely =0.84, relwidth = 0.4, relheight = 0.06 )

            l6 = Label(frame7, text = "Password", font = '40')
            l6.place(relwidth= 0.29, relheight = 1)

            
            e43 = Entry(top3 , font = ' 40')
            e43.place (relx= 0.23, rely= 0.85  ,relwidth = 0.26 , relheight = 0.04 )#password register

            

            def opwin5 ():
                
                global background_image5
                
                HEIGHT = 600
                WIDTH = 650
                top4 = Toplevel()
                top4.title('BANK MANAGEMENT')
                top4.iconbitmap(d)
                canvas5 = Canvas(top4, height = HEIGHT , width = WIDTH)
                canvas5.pack()
  
                background_image5 = PhotoImage(file= c)
                background_label5 = Label (top4, image = background_image5)
                background_label5.place(relwidth =1 ,relheight =1)

                l5 = Label(top4, text = "Your account is created !!", font = ' bold 36')
                l5.place(relx= 0.07, rely =0.42)

                l11 = Label(top4, text='Your Account number is',font = ' bold 24 ')
                l11.place(relx=0.07, rely = 0.50)
               
                l12 = Label(top4, text = table_data[0], font = 'bold 24')
                l12.place(relx = 0.3,rely= 0.50)
                
                l6 = Label(top4, text ="    Try logging in. ", font = ' bold 36')
                l6.place(relx= 0.07, rely =0.54)



                
            def new_account():
                    
                        fname  = e34.get()
                        lname  = e31.get()
                        DOB    = int(str(d3.get())+str(d2.get())+str(d1.get())) 
                        passwd = e43.get()
                        email  = e48.get()
                        city   = e38.get()
                        pincode= e47.get()
                        mobile_number = e6.get()
                        balance_amount =bl1.get()

                        sql ='''INSERT INTO Accounts(fname,
                                                    lname,
                                                    DOB,
                                                    mobile_number,
                                                    email,
                                                    city,
                                                    pincode,
                                                    balance_amount,
                                                    password) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
      
                                   
                                    
                        values = (fname,lname,DOB ,mobile_number,email,city,pincode,balance_amount,passwd)
      

                        mycursor.execute(sql,values)
                        mydb.commit()
                        
                        opwin5() 
                        

            b5 = Button(top3,text = "Register",font = 40,bg = '#80c1ff',command = new_account )
            b5.place(relx =0.1,rely = 0.93 )


            
    




b4 = Button (window,text = "Sign Up",font = 40,bg = '#80c1ff', command = opwin4)
b4.place(relx =0.1,rely = 0.73)









window.mainloop()


                 
