###
#programmer information
#Name: Keenan Faure
#Student Number: 3959394
#email Address: 3959394@myuwc.ac.za
#Course: CSC312 - Databases
#language: Python 3
####

#imports
import tkinter
from tkinter import messagebox as mb
from tkinter import simpledialog   

#used to hold the users prefered province and period - used for Q2()
userPeriod = []
userProvince = []

#lists that will contain the data
catagoryOne = []
num = ['23','35','43','13','13','13','13','13','13','13','13','13','13','13']
province = []
catagoryTwo = []
catagoryThree = []
catagoryFour = []
catagoryFive = []
catagorySix = []
catagorySeven = []
catagoryEight = []
catagoryNine = []
catagoryTen = []
catagoryEle = []
catagoryTwel = []
catagoryThirt = []
catagoryFourt = []

#main method
def main():
   read()
   UI() 
   #nothing will execute after this because tkinter.mainloop() is used at the end of
   #the UI() method
   
#method to read the information from .csv file
def read():
   #opens the file to be read
   file = open("SouthAfricaCrimeStats_v2.csv","r")
   
   #counter is created to skip the first line
   counter = 0
   
   #creates catagories
   for line in file:
      if(counter == 0): #skips the first line
         global catagories
         catagories = line.split(",")
         counter = counter + 1
      else:
         arrayCatagories = line.split(",")
         
         #creates the different catagories and stores them in the respective arrays
         catagoryOne.append(arrayCatagories[0])
         catagoryTwo.append(arrayCatagories[1])
         catagoryThree.append(arrayCatagories[2])
         catagoryFour.append(arrayCatagories[3])
         catagoryFive.append(arrayCatagories[4])
         catagorySix.append(arrayCatagories[5])
         catagorySeven.append(arrayCatagories[6])
         catagoryEight.append(arrayCatagories[7])
         catagoryNine.append(arrayCatagories[8])
         catagoryTen.append(arrayCatagories[9])
         catagoryEle.append(arrayCatagories[10])
         catagoryTwel.append(arrayCatagories[11])
         catagoryThirt.append(arrayCatagories[12])
         catagoryFourt.append(arrayCatagories[13])
         
         #stores the provinces into an array
         if(arrayCatagories[0] in province):
            continue
         else: 
            province.append(arrayCatagories[0])
         
         counter = counter + 1
   #closes the file
   file.close()

#1.)method for displaying the Data   
def displayData():
   out = ""
   #prints the catagories
   for i in range(len(catagories)-1,-1,-1):
      out = ("{: <"+str(num[i])+"}").format(catagories[i]) + out
   
   #adds a new line   
   out = out + "\n"
   #prints the catagory items
   for i in range(0,15):
      out = out + "{: <18} {: <30} {: <40} {: <13} {: <13} {: <13} {: <13} {: <13} {: <13} {: <13} {: <13} {: <13} {: <13} {: <13}".format(catagoryOne[i],catagoryTwo[i],catagoryThree[i],catagoryFour[i],catagoryFive[i],
      catagorySix[i],catagorySeven[i],catagoryEight[i],catagoryNine[i],catagoryTen[i],catagoryEle[i],catagoryTwel[i],catagoryThirt[i],catagoryFourt[i]) + "\n"
      
   mb.showinfo("Display CSV","{: <13000}".format(out))  
    
#2.)User period and province
def userPP():
   period = catagories[3:]
   #create window and sets sizes
   windowThree = tkinter.Tk()
   windowFour = tkinter.Tk()
   windowThree.title("Select a Province")
   windowFour.title("Select a Period")
   windowThree.geometry("250x300")
   windowFour.geometry("250x300")
   windowFour.withdraw()
   
   def iop():
      #saves which province the user chose
      def wc(): userProvince.append("Western Cape");windowThree.destroy();windowFour.deiconify()
      def ga(): userProvince.append("Gauteng");windowThree.destroy();windowFour.deiconify()
      def fs(): userProvince.append("Free State");windowThree.destroy();windowFour.deiconify()
      def nw(): userProvince.append("North West");windowThree.destroy();windowFour.deiconify()
      def kzn(): userProvince.append("Kwazulu/Natal");windowThree.destroy();windowFour.deiconify()
      def mp(): userProvince.append("Mpumalanga");windowThree.destroy();windowFour.deiconify()
      def ec(): userProvince.append("Eastern Cape");windowThree.destroy();windowFour.deiconify()
      def lp(): userProvince.append("Limpopo");windowThree.destroy();windowFour.deiconify()
      def nc(): userProvince.append("Northern Cape");windowThree.destroy();windowFour.deiconify()

      #saves which period the user chose and runs the method Q2() which then outputs the data
      def o(): userPeriod.append("2005-2006");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagoryFour)
      def t(): userPeriod.append("2006-2007");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagoryFive)
      def th(): userPeriod.append("2007-2008");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagorySix)
      def f(): userPeriod.append("2008-2009");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagorySeven)
      def fi(): userPeriod.append("2009-2010");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagoryEight)
      def s(): userPeriod.append("2010-2011");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagoryNine)
      def se(): userPeriod.append("2011-2012");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagoryTen)
      def e(): userPeriod.append("2012-2013");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagoryElev)
      def n(): userPeriod.append("2013-2014");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagoryTwel)
      def te(): userPeriod.append("2014-2015");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagoryThirt)
      def elev(): userPeriod.append("2015-2016");windowFour.destroy();Q2(userProvince[len(userProvince)-1],userPeriod[len(userPeriod)-1],catagoryFourt)
   
      #adds the buttons
      counter = 0
      wtbo = tkinter.Button(windowThree,text='{: ^30}'.format(province[counter]),command=wc).pack()
      counter = counter + 1
      wtbt = tkinter.Button(windowThree,text='{: ^30}'.format(province[counter]),command=ga).pack()
      counter = counter + 1
      wtbth = tkinter.Button(windowThree,text='{: ^30}'.format(province[counter]),command=fs).pack()
      counter = counter + 1
      wtbf = tkinter.Button(windowThree,text='{: ^30}'.format(province[counter]),command=nw).pack() 
      counter = counter + 1
      wtbfi = tkinter.Button(windowThree,text='{: ^30}'.format(province[counter]),command=kzn).pack()
      counter = counter + 1
      wtbs = tkinter.Button(windowThree,text='{: ^30}'.format(province[counter]),command=mp).pack()
      counter = counter + 1
      wtbse = tkinter.Button(windowThree,text='{: ^30}'.format(province[counter]),command=ec).pack()
      counter = counter + 1
      wtbe = tkinter.Button(windowThree,text='{: ^30}'.format(province[counter]),command=lp).pack()
      counter = counter + 1
      wtbn = tkinter.Button(windowThree,text='{: ^30}'.format(province[counter]),command=nc).pack()
      
      #adds the buttons 
      counter2 = 0
      wfbo = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=o).pack()
      counter2 = counter2 + 1
      wfbt = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=t).pack()
      counter2 = counter2 + 1
      wfbth = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=th).pack()
      counter2 = counter2 + 1
      wfbf = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=f).pack()
      counter2 = counter2 + 1
      wfbfi = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=fi).pack()
      counter2 = counter2 + 1
      wfbs = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=s).pack()
      counter2 = counter2 + 1
      wfbse = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=se).pack()
      counter2 = counter2 + 1
      wfbe = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=e).pack()
      counter2 = counter2 + 1
      wfbn = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=n).pack()
      counter2 = counter2 + 1
      wfbte = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=te).pack()
      counter2 = counter2 + 1
      wfbelev = tkinter.Button(windowFour,text='{: ^30}'.format(period[counter2]),command=elev).pack()   
   iop()
   
#Calculates how much Crimes occured in a period and province
def Q2(province, period, catagory):
   Answer = 0
   for i in range(0,len(catagoryOne)):
      if(province == catagoryOne[i]):
         Answer = int(catagory[i]) + Answer
   mb.showinfo("Q2", "The total amount of crimes for in the: " + str(province) + " \narea during the period: " + str(period) + " are: " + str(Answer)) 
   
#3.) Station, period 2004-2015  
def Q3():
   #creates the window UI and asks the user a question
   windowFive = tkinter.Tk()
   windowFive.withdraw()
   mb.showwarning("Careful","The following text is case sensitive!\nStart with a capital letter before and after each word")
   userStation = simpledialog.askstring(title="Q3 - ",prompt="What station would you like to look-up?:")
   
   #if the user entered nothing
   if((userStation) == None):
      mb.showwarning("Warning","No input")
      
   #else it continues
   else:
      Answer = 0
      #searces through the entire database and it adds up all the cases that occured in that period
      for i in range(0, len(catagoryTwo)):
         if(userStation == catagoryTwo[i]):
           Answer = int(catagoryFour[i]) + int(catagoryFive[i]) + int(catagorySix[i]) + int(catagorySeven[i]) + int(catagoryEight[i]) + int(catagoryNine[i]) + int(catagoryTen[i]) + int(catagoryEle[i]) + int(catagoryTwel[i]) + int(catagoryThirt[i]) + int(catagoryFourt[i]) + int(Answer)
      mb.showinfo("Q3", "The total amount of crimes for in the: " + str(userStation) + " \nduring the period 2005-2015 are: " + str(Answer))

#4.) truck hijacking, 2010-2011
def Q4():
   case = "Truck hijacking"
   period = "2010-2011"
   #catagoryThree is the period 2010-2011
   Answer = 0
   #searches through the entire database and then adds up the amount of cases
   #that occured in that period
   for i in range(0,len(catagoryThree)):
      if(catagoryThree[i] == case):
         Answer = int(catagoryNine[i]) + Answer
   mb.showinfo("Q4","The total amount of " + case + " during the period " + period + " are " + str(Answer))        

#5.) Arson in Boitekon, Ngodwana in 2009-2010      
def Q5():
   case = "Arson"
   Answer = 0
   #loops through the entire catagory
   for i in range(0, len(catagoryEight)):
      #if it finds a match its adds up all the cases in the respective period
      if(catagoryTwo[i] == "Boitekong" or catagoryTwo[i] == "Ngodwana"):
         Answer = int(catagoryEight[i]) + Answer
   mb.showinfo("Q5","The total amount of " + case + " during the 2009-2010 period\nIn Boitekong and Ngodwana is: " + str(Answer))
   
#6.)Highest crimes in 2014-2015
def Q6():

   arrayCasesCatagory = []
   arrayCasesNumber = []
   for i in range(0,len(catagoryThirt)): #loop through all the items (31k)
      #if it doesnt exist inside the array then add it
      if(catagoryThree[i] not in arrayCasesCatagory):
         arrayCasesCatagory.append(catagoryThree[i])
         arrayCasesNumber.append(int(catagoryThirt[i]))

         
      #else it exists inside the array
      else:
         if(catagoryThree[i] in arrayCasesCatagory):
            for num in range(0,len(arrayCasesCatagory)):
               if(catagoryThree[i] == arrayCasesCatagory[num]):
                  arrayCasesNumber[num] += int(catagoryThirt[i])
                  
   #checks which case had the higest amount of incidents               
   highest = -1  
   index = -2           
   for j in range(0,len(arrayCasesCatagory)):
      if(arrayCasesNumber[j] > highest):
         highest = arrayCasesNumber[j]
         index = j
   mb.showinfo("Q6","The '" + str(arrayCasesCatagory[index]) + "' catagory had the highest number of incidents with a value of " + str(highest) + " over the 2014-2015 period.")  

#7.)Nongoma in KZN, which period lowest cases
def Q7():
   case = "Murder"
   arrayCasesPeriods = catagories[3:]
   arrayCasesNumber = []
   #loops through all the items in that catagory
   counter = 0
   for i in range(0,len(catagoryThree)):
      #checks if it meets the requirements and adds the incident numbers to an empty array
      if(catagoryTwo[i] == "Nongoma" and catagoryOne[i] == "Kwazulu/Natal" and catagoryThree[i] == case):
         if(len(arrayCasesNumber) == 0): 
            arrayCasesNumber.append(catagoryFour[i]);arrayCasesNumber.append(catagoryFive[i]);arrayCasesNumber.append(catagorySix[i])
            arrayCasesNumber.append(catagorySeven[i]);arrayCasesNumber.append(catagoryEight[i]);arrayCasesNumber.append(catagoryNine[i])
            arrayCasesNumber.append(catagoryTen[i]);arrayCasesNumber.append(catagoryEle[i]);arrayCasesNumber.append(catagoryTwel[i])
            arrayCasesNumber.append(catagoryThirt[i]);arrayCasesNumber.append(catagoryFourt[i])
            
         #checks for the smaller value and saves it into the arrayCasesPeriods instead  
         else:
            counter = 0
            if(catagoryFour[i] < arrayCasesNumber[counter]): catagoryFour[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagoryFive[i] < arrayCasesNumber[counter]): catagoryFive[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagorySix[i] < arrayCasesNumber[counter]): catagorySix[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagorySeven[i] < arrayCasesNumber[counter]):catagorySeven[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagoryEight[i] < arrayCasesNumber[counter]): catagoryEight[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagoryNine[i] < arrayCasesNumber[counter]): catagoryNine[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagoryTen[i] < arrayCasesNumber[counter]): catagoryTen[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagoryEle[i] < arrayCasesNumber[counter]): catagoryEle[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagoryTwel[i] < arrayCasesNumber[counter]): catagoryTwel[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagoryThirt[i] < arrayCasesNumber[counter]): catagoryThirt[i] = arrayCasesNumber[counter]
            counter += 1
            if(catagoryFourt[i] < arrayCasesNumber[counter]): catagoryFourt[i] = arrayCasesNumber[counter]
         
   lowest = 50000000
   index = -1    
   #checks for the lowest value in the produced array and prints the corressponding period     
   for i in range(0,len(arrayCasesNumber)):
      if(int(arrayCasesNumber[i]) < int(lowest)):
         lowest = arrayCasesNumber[i]
         index = i
         
   mb.showinfo("Q7","The period that had the lowest amount of Murder cases in Nongoma in Kwazulu/Natal is: " + str(arrayCasesPeriods[index]) + " with a value of " + str(lowest))

#8.)Stations in North West had 0 cases for attepted murder during 2008-2009  
def Q8():
   case = "Attempted murder"
   stationsZeroCases = []
   for i in range(0,len(catagorySeven)):
      #checks if it has zero cases during 2008-2009
      #checks if the province is the North West
      #checks if it falls under the incident of Attempted murder
      #if true it adds that station to the array
      if(int(catagorySeven[i]) == 0 and catagoryOne[i] == "North West" and catagoryThree[i] == case):
         stationsZeroCases.append(catagoryTwo[i])
 
   mb.showinfo("Q8","The stations in the North West that had 0 cases for attempted murder during 2008-2009 are: " + str(stationsZeroCases))
   
#9.) Personal Query - What is the average amount of murders that occured in the Western Cape during 2005-2010
def Q9():
   Answer = 0
   #searches through the database and uses one loop to add up all the periods that are parallel to the 
   #found index, after which it adds up all the information and displays it to the user.
   for i in range(0, len(catagoryOne)):
      if(catagoryOne[i] == "Western Cape" and catagoryThree[i] == "Murder"):
         Answer = int(catagoryFour[i]) + int(catagoryFive[i]) + int(catagorySix[i]) + int(catagorySeven[i]) + int(catagoryEight[i]) + int(catagoryNine[i]) + Answer
         
         
   mb.showinfo("Q9 - Person Query", "The average number of murders that occured in the Western Cape during 2005-2010 are: " + str(Answer / 6))
def UI():
   def start():
      #create new window
      windowTwo = tkinter.Tk()
      windowTwo.title("Select a Query Number")
      windowTwo.geometry("250x300")
      
      #adds the different buttons to the Interface based on the Question number
      wtbo = tkinter.Button(windowTwo,text='{: ^35}'.format("One - 1"),command=displayData).pack()
      wtbt = tkinter.Button(windowTwo,text='{: ^35}'.format("Two - 2"),command=userPP).pack()
      wtbth = tkinter.Button(windowTwo,text='{: ^35}'.format("Three - 3"),command=Q3).pack()
      wtbf = tkinter.Button(windowTwo,text='{: ^35}'.format("Four - 4"),command=Q4).pack()
      wtbfi = tkinter.Button(windowTwo,text='{: ^35}'.format("Five - 5"),command=Q5).pack()
      wtbs = tkinter.Button(windowTwo,text='{: ^35}'.format("Six - 6"),command=Q6).pack()
      wtbse = tkinter.Button(windowTwo,text='{: ^35}'.format("Seven - 7"),command=Q7).pack()
      wtbe = tkinter.Button(windowTwo,text='{: ^35}'.format("Eight - 8"),command=Q8).pack()
      wtbn = tkinter.Button(windowTwo,text='{: ^35}'.format("Nine - 9"),command=Q9).pack()
      wtbexit = tkinter.Button(windowTwo,text='{: ^35}'.format("Exit"),command=quit).pack()
      tkinter.mainloop()
      
   #Closes the program   
   def quit():
      mb.showinfo("Closing", "Now closing program")
      exit()
   
   #creates the mainWindow
   window = tkinter.Tk()
   window.geometry("300x100")
   window.title("Database - 3959394")
   #adds the buttons to the window
   button = tkinter.Button(window,text="{: ^30}".format("Start"),command=start).pack()   
   button2 = tkinter.Button(window,text="{: ^30}".format("Quit"),command=quit).pack()
   window.mainloop()
      
main()

