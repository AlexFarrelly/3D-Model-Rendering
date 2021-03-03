import tkinter as tk
import tkinter.font as font
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import csv



class windows(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = False )
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.farmes = {}

        for i in signinwindow, loginwindow, mainwindow:
            frame = i(container, self)
            
            self.farmes[i] = frame
            
            frame.grid(row = 15, column = 15, sticky = "nesw")
            
        self.show_frame(loginwindow)

        global maxScreen
        global key
        key = None
        maxScreen = True


    def show_frame(self,cont):
        frame = self.farmes[cont]
        frame.tkraise()


#Login Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class loginwindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#596387")
        self.checkVar = tk.IntVar()
        self.nextframe = lambda: controller.show_frame(mainwindow)
        ButtonFont = font.Font(size = 30, family="Helvetica")
        LabelFont = font.Font(size = 24, family = "Helvetica")
        EntryFont = font.Font(size = 35, family = "Helvetica")
        #Buttons------------------------------------
        self.minmaxbutton = tk.Button(self,
                                      command = minmax_frame, text = "Min", font = (font.Font(size = 12, family="Helvetica")))
        self.minmaxbutton.place(x = 1855, y = 0)
        
        self.exitbutton = tk.Button(self,
                                command = quitWindow, text = "X",  font = (font.Font(size = 12, family="Helvetica"))).place(x =1895 , y = 0)
        self.loginbutton = tk.Button(self,
                                      text = "Login", font = ButtonFont, width = 30, height = 2, command = self.login)
        self.loginbutton.place(x =1000 , y =700 )
        self.newuserbutton = tk.Button(self,
                                      text = """Dont Have an Account?
Sign Up""", font = ButtonFont , width = 30, command = lambda: controller.show_frame(signinwindow))
        self.newuserbutton.place(x =275 , y =700 )
        #Entry Boxs----------------------------------------------------
        self.usernamebox = tk.Entry(self,
                                    font = EntryFont)
        self.usernamebox.place(x = 700, y = 300)
        self.passwordbox = tk.Entry(self,
                                    show = "*", font = EntryFont)
        self.passwordbox.place(x = 700, y = 475)
        #Labels--------------------------------------------------------
        infomationLabel = tk.Label(self,
                                   text = """Please Enter Your Login Details Below""", font = font.Font(size = 35, family = "Helvetica")).place(x = 550, y = 100)
        usernameLabel = tk.Label(self,
                                 text = "Please enter your username:" , font = LabelFont).place(x = 765, y = 250)
        passwordLabel = tk.Label(self,
                                 text = "Please enter your password:" , font = LabelFont).place(x = 765, y = 425)
        #CheckBox---------------------------------------------------------
        self.showpassBox = tk.Checkbutton(self,
                                          text = "Show Password",variable = self.checkVar, command = self.showpassword,  font = LabelFont)                                                                  
        self.showpassBox.place(x = 850, y = 600)
            
    def showpassword(self):
        if self.checkVar.get() == 1:
            self.passwordbox.config(show = "")
        else:
            self.passwordbox.config(show = "*")

    def login(self):
        if len(self.passwordbox.get()) > 0 and len(self.usernamebox.get()) > 0 :
            match = False
            try:
                with open("UserData.csv", "r") as file:
                    fieldnames = ["Username", "Password", "UserKey"]
                    reader = csv.DictReader(file, fieldnames = fieldnames)
                    for row in reader:
                        if row["Username"] == self.usernamebox.get():
                            match = True
                            if row["Password"] == self.passwordbox.get():
                                global key
                                key = ("".join(str(ord(l)) for l in self.usernamebox.get()))
                                Popup = tk.Toplevel()

                                Message = tk.Label(master=Popup,
                                                    text= """Your logged in,
press ok to proceed""").grid(row=1, column=1, columnspan=2)
                                Button = tk.Button(master= Popup,
                                                    text="Ok",
                                                command =self.nextframe).grid(row=2, column=2)
                            else:
                                arg
                    if match == False:
                        arg
            except:
                Errorpopup("""Error: Ethier the username or
password is incorrect""")
        else:
            Errorpopup("""Error: Please enter a
username and or password""")

                            

#Regestration Window
class signinwindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#596387")
        self.checkVar = tk.IntVar()
        self.nextframe = lambda: controller.show_frame(mainwindow)
        ButtonFont = font.Font(size = 30, family="Helvetica")
        LabelFont = font.Font(size = 24, family = "Helvetica")
        EntryFont = font.Font(size = 35, family = "Helvetica")
        #Buttons------------------------------------
        self.minmaxbutton = tk.Button(self,
                                      command = minmax_frame, text = "Min", font = (font.Font(size = 12, family="Helvetica")))
        self.minmaxbutton.place(x = 1855, y = 0)
        
        self.exitbutton = tk.Button(self,
                                command = quitWindow, text = "X",  font = (font.Font(size = 12, family="Helvetica"))).place(x =1895 , y = 0)
        self.signupbutton = tk.Button(self,
                                      text = "Register", font = ButtonFont, width = 20, command = self.register)
        self.signupbutton.place(x =730 , y =700 )
        #Entry Boxs----------------------------------------------------
        self.usernameBox = tk.Entry(self,
                                    font = EntryFont)
        self.usernameBox.place(x = 700, y = 300)
        self.passwordBox = tk.Entry(self,
                                    show = "*", font = EntryFont)
        self.passwordBox.place(x = 965, y = 475)
        self.checkpasswordBox = tk.Entry(self,
                                    show = "*", font = EntryFont)
        self.checkpasswordBox.place(x = 435, y = 475)
        #Labels--------------------------------------------------------
        infomationLabel = tk.Label(self,
                                   text = """To Create An Account, Please
Enter Your Details Below""", font = LabelFont).place(x = 750, y = 100)
        usernameLabel = tk.Label(self,
                                 text = "Please enter your username:" , font = LabelFont).place(x = 765, y = 250)
        passwordLabel = tk.Label(self,
                                 text = "Please enter your password:" , font = LabelFont).place(x = 500, y = 425)
        repasswordLabel = tk.Label(self,
                                 text = "Please re-enter your password:" , font = LabelFont).place(x = 1000, y = 425)
        #CheckBox---------------------------------------------------------
        self.showpassBox = tk.Checkbutton(self,
                                          text = "Show Password",variable = self.checkVar, command = self.showpassword, font = LabelFont)                                                                  
        self.showpassBox.place(x = 840, y = 600)
        
    def showpassword(self):
        if self.checkVar.get() == 1:
            self.passwordBox.config(show = "")
            self.checkpasswordBox.config(show = "")
        else:
            self.passwordBox.config(show = "*")
            self.checkpasswordBox.config(show = "*")

    def register(self):
        if self.passwordBox.get() == self.checkpasswordBox.get() and len(self.passwordBox.get()) > 0 and len(self.usernameBox.get()) > 0 :
            try:
                with open("UserData.csv", "r") as file:
                    fieldnames = ["Username", "Password", "UserKey"]
                    reader = csv.DictReader(file, fieldnames = fieldnames)
                    for row in reader:
                        if row["Username"] == self.usernameBox.get():
                            arg
                    with open("UserData.csv", "a") as file:
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        writer.writerow({"Username": "%s" % self.usernameBox.get()
                                         ,"Password": "%s" % self.passwordBox.get()
                                         , "UserKey": "%s" % ("".join(str(ord(l)) for l in self.usernameBox.get())) })
                        global key
                        key = ("".join(str(ord(l)) for l in self.usernameBox.get()))
                Popup = tk.Toplevel()

                Message = tk.Label(master=Popup,
                                        text= """Your account has been created,
press ok to proceed""").grid(row=1, column=1, columnspan=2)
                Button = tk.Button(master= Popup,
                                        text="Ok",
                                    command =self.nextframe).grid(row=2, column=2)

    
            except:
                Errorpopup("""Error: That Username has
already been taken""")
        else:
            Errorpopup("""Error: Please check you have both a
username and matching passwords""")

        
#Main Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class mainwindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#596387")
        self.ImageFile = True
        self.nextframe = lambda: controller.show_frame(loginwindow)
        #Fonts-------------
        ButtonFont = font.Font(size = 24, family="Helvetica")
        MenuFont = font.Font(size = 12, family="Helvetica")
        LabelFont = font.Font(size = 10, family = "Helvetica")
        #Buttons-------
        self.minmaxbutton = tk.Button(self,
                                      command = minmax_frame, text = "[__]", font = MenuFont)
        self.minmaxbutton.grid(row = 0, column= 12)
        
        self.exitbutton = tk.Button(self,
                                command = quitWindow, text = "X",  font = MenuFont).grid(row = 0, column = 14)
        self.RenderImageBtn = tk.Button(self,
                                        text="Render Your Image", command = self.RenderImage, state = "disabled", font = ButtonFont, height = 3, width = 30 )
        self.RenderImageBtn.grid(row = 13, column = 6 )
        self.SelectImageBtn = tk.Button(self,
                                        command = self.imageSelector, text = "Select Your Images", font = ButtonFont, height = 3, width = 30 )
        self.SelectImageBtn.grid(row = 13, column = 5)
        #Dropdown selections-----------
        Fileoptions = ["Change File Type", "Save", "Open"]
        Useroptions = ["Log Out"]
        Presetsoptions = ["Save as Pre-set", "Open Pre-set"]
        
        self.Fileclicked = tk.StringVar()
        self.Userclicked = tk.StringVar()
        self.Presetsclicked = tk.StringVar()
        
        self.Fileclicked.set("File")
        self.Userclicked.set("User")
        self.Presetsclicked.set("Pre-sets")
        
        self.filedrop = tk.OptionMenu(self,
                                 self.Fileclicked, *Fileoptions, command = self.OptionChange)
        self.filedrop.config(font = MenuFont)
        userdrop = tk.OptionMenu(self,
                                 self.Userclicked, *Useroptions, command = self.OptionChange)
        userdrop.config(font = MenuFont)
        presetsdrop = tk.OptionMenu(self,
                                    self.Presetsclicked, *Presetsoptions, command = self.OptionChange)
        presetsdrop.config(font = MenuFont)
        
        self.filedrop.grid(row = 0, column= 0)
        userdrop.grid(row = 0, column= 2)
        presetsdrop.grid(row = 0, column= 4)
        #Canvas----------------
        self.LCanvas = tk.Canvas(self,
                                  bg = "#596387", height = 650, width = 650)
        self.LCanvas.grid(row = 1, column = 5 )
        self.RCanvas = tk.Canvas(self,
                                     bg = "#596387", height = 650, width = 650)
        self.RCanvas.grid(row = 1, column = 6)
        #Sliders------------------
        self.minDispSlider = tk.Scale(self,
                                      from_=1, to = 64, orient = "horizontal", length = 295, width = 20)
        self.minDispSlider.set(32)
        self.minDispSlider.grid(row = 10, column = 10)
        self.maxDispSlider = tk.Scale(self,
                                      from_=16, to = 320, orient = "horizontal", length = 295, width = 20)
        self.maxDispSlider.set(112)
        self.maxDispSlider.grid(row = 8, column = 10)
        self.focalSlider = tk.Scale(self,
                                      from_=18, to = 100, orient = "horizontal", length = 295, width = 20)
        self.focalSlider.set(28)
        self.focalSlider.grid(row = 12, column = 10)
        self.uniqueRatioSlider = tk.Scale(self,
                                          from_=1, to = 15, orient = "horizontal", length = 295, width = 20)
        self.uniqueRatioSlider.set(10)
        self.uniqueRatioSlider.grid(row = 6, column = 10)
        
        global uniqueRatioSlider, maxDispSlider, minDispSlider, focalSlider
        uniqueRatioSlider = self.uniqueRatioSlider
        maxDispSlider = self.maxDispSlider
        minDispSlider = self.minDispSlider
        focalSlider = self.focalSlider
        #Labels-------------------------
        self.minDispLabel = tk.Label(self,
                                     text = "Mininum Possible Disparity Value", font = LabelFont).grid(row = 9, column = 10)
        self.maxDispLabel = tk.Label(self,
                                     text = "Max Possible Disparity", font = LabelFont).grid(row = 7, column = 10)
        self.focalLabel = tk.Label(self,
                                   text = "Focal Length of Your Camera", font = LabelFont).grid(row = 11, column = 10)
        self.uniqueRatioLabel = tk.Label(self,
                                         text = "How Unique a Pixel Can Be To Be Matched in %", font = LabelFont).grid(row = 5, column = 10)

    def imageSelector(self):
        self.imagePathStr = []
        imagePath = filedialog.askopenfilename()
        while len(imagePath) > 0 or len(self.imagePathStr) < 2:
            self.imagePathStr.append(imagePath)
            imagePath = filedialog.askopenfilename()
        length = (len(self.imagePathStr) - 1)
        try:
            while length >= 0:
                imageCheck = Image.open((self.imagePathStr[length]))
                length -= 1
            pathL = Image.open((self.imagePathStr[0]))
            pathR = Image.open(self.imagePathStr[(len(self.imagePathStr)-1)])
            
            NewPathR = pathR.resize((650,650))
            NewPathL = pathL.resize((650,650))
            
            self.RCanvas.image = ImageTk.PhotoImage(NewPathR)
            self.RCanvas.create_image(0,0, image = self.RCanvas.image, anchor = "nw")
            
            self.LCanvas.image = ImageTk.PhotoImage(NewPathL)
            self.LCanvas.create_image(0,0, image = self.LCanvas.image, anchor = "nw")
            
            self.RenderImageBtn.configure(state = "active", bg = "light green")
        except:
            Errorpopup("""Error: One Of the file directorys given
was not an image please try again""")
            
                    
    def videoSelector(self):
        self.video = filedialog.askopenfilename()
        if len(self.video) > 0:
            try:
                self.imagePathStr = []
                self.createframes(self.video)
                
                pathL = Image.open((self.imagePathStr[0]))
                pathR = Image.open(self.imagePathStr[(len(self.imagePathStr)-1)])
                
                NewPathR = pathR.resize((650,650))
                NewPathL = pathL.resize((650,650))
                
                self.RCanvas.image = ImageTk.PhotoImage(NewPathR)
                self.RCanvas.create_image(0,0, image = self.RCanvas.image, anchor = "nw")
                
                self.LCanvas.image = ImageTk.PhotoImage(NewPathL)
                self.LCanvas.create_image(0,0, image = self.LCanvas.image, anchor = "nw")
                
                self.RenderImageBtn.configure(state = "active", bg = "light green")
                print (self.imagePathStr)
            except:
                Errorpopup("""Error: The file directory given
    was not a video please try again""")
        
    def createframes(self, video):
        Video = cv2.VideoCapture(self.video)
        maxFrames = int(Video.get(cv2.CAP_PROP_FRAME_COUNT))
        success, image = Video.read()
        count = 0
        
        while success:
            image = cv2.resize(image,(650,650))
            cv2.imwrite("images/frame%d.jpg" % count, image)
            self.imagePathStr.append("images/frame%d.jpg" % count)
            count += 1
            success, image = Video.read()


    def changeFileType(self):
        if self.ImageFile == True:
            self.ImageFile = False
            self.SelectImageBtn.config(command = self.videoSelector,
                                       text = "Select Your Video")
        else:
            self.ImageFile = True
            self.SelectImageBtn.config(command = self.imageSelector,
                                       text = "Select Your Images")
    
    
    def OptionChange(self, event):
        if self.Fileclicked.get() == "Change File Type":self.Fileclicked.set("File"), self.changeFileType()
        elif self.Fileclicked.get() == "Save":self.Fileclicked.set("File"), saveWindow([])
        elif self.Fileclicked.get() == "Open":self.Fileclicked.set("File"), openWindow("rendering")
        elif self.Presetsclicked.get()  == "Save as Pre-set":self.Presetsclicked.set("Pre-sets"), self.save()
        elif self.Presetsclicked.get()  == "Open Pre-set":self.Presetsclicked.set("Pre-sets"), openWindow("pre-set")
        elif self.Userclicked.get() == "Log Out": self.Userclicked.set("User"), self.logout()

    def logout(self):
        logoutWindow = tk.Toplevel()

        Message = tk.Label(master = logoutWindow,
                                text= """Are you sure that you want to log out,
all unsaved data will be lost?""").grid(row=1, column=1, columnspan=2)
        quitButton = tk.Button(master= logoutWindow ,
                                text="Yes",
                                command = self.nextframe).grid(row=2, column=1)
        cancelButton = tk.Button(master= logoutWindow,
                                text="No",
                                 command = lambda: logoutWindow.destroy()).grid(row=2, column=2)


    def save(self):
        x = [self.minDispSlider.get(), self.maxDispSlider.get(), self.focalSlider.get(), self.uniqueRatioSlider.get()]
        saveWindow(x)

    def RenderImage(self):
        images = self.imagePathStr
        mindisp = self.minDispSlider.get()
        maxValue = self.maxDispSlider.get()
        focal_length = self.focalSlider.get()
        uniquenessRatio = self.uniqueRatioSlider.get()
        RenderedimageData(images, focal_length, maxValue, mindisp, uniquenessRatio)

#Rendering method---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class RenderedimageData():
    def __init__(self, images, f, maxValue, mindisp, uniquenessRatio):
        homogenized = np.array([[1,0,0],
                    [0,1,0],
                    [0,0,-f]])
            
        distortion = np.array([[0.],
                       [0.],
                       [0.],
                       [0.]])
        if len(images) > 2:
            totalImages = (len(images) - 1)
            currentLeftImage = 0
            while totalImages > currentLeftImage:
                pathL = images[currentLeftImage]
                pathR = images[(currentLeftImage + 1)]
                left_image = cv2.imread(pathL)
                right_image = cv2.imread(pathR)
        #Image~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                height, width, _ = left_image.shape
                RGB = right_image.reshape(-1,3)
        #Matrices~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                camreaMatrix = np.array([[f,0,width/2],
                                         [0,f,height/2],
                                         [0,0,1]])
                transformation = np.float32([[1,0,0,-width/2],
                                             [0,1,0,-height/2],
                                             [0,0,0,-f],
                                             [0,0,-1/100,0]])

                camreaMatrix = self.OptimalMatrix(camreaMatrix, distortion, right_image)
                
                rVector, tVector = self.rt_Vectors(homogenized, camreaMatrix)

                stereo = self.depthMap(left_image, right_image)

                points = self.pointsTo3D(stereo, transformation)

                deleteNoise = ((stereo.reshape(-1)) > (stereo.reshape(-1)).min())
                points = points[deleteNoise]
                RGB = RGB[deleteNoise]
                
                c = [ [i] for i in points]
                d = [ [i] for i in RGB]
                a = 0
                largeArray = []
                for i in points:
                    pointsArray = np.array(c[a])

                    coloursArray = np.array(d[a])

                    mainArray = np.hstack((pointsArray, coloursArray))
                    if a == 0:
                        largeArray = mainArray
                    else:
                        largeArray = np.vstack((largeArray, mainArray))
                    a +=1
            print (largeArray)
            
            points = largeArray[abs(largeArray[:,2]-(np.mean(largeArray,axis=0)[2]))<2]
            
            axis, RGB = points[:,:3], points[:,3:]
            project = plt.axes(projection='3d')
            
            project.scatter(axis[:,0], axis[:,1], axis[:,2], c = RGB/255, s = 0.01)
            plt.show()

        else:
            pathL = images[0]
            pathR = images[1]
            left_image = cv2.imread(pathL)
            right_image = cv2.imread(pathR)
            height, width, _ = left_image.shape
            RGB = right_image.reshape(-1,3)

            camreaMatrix = np.array([[f,0,width/2],
                                     [0,f,height/2],
                                     [0,0,1]])
            transformation = np.float32([[1,0,0,-width/2],
                             [0,1,0,-height/2],
                             [0,0,0,-f],
                             [0,0,-1/100,0]])
            
            camreaMatrix = self.OptimalMatrix(camreaMatrix, distortion, right_image)
                
            rVector, tVector = self.rt_Vectors(homogenized, camreaMatrix)

            stereo = self.depthMap(left_image, right_image, maxValue, mindisp, uniquenessRatio)

            points = self.pointsTo3D(stereo, transformation)

            deleteNoise = ((stereo.reshape(-1)) > (stereo.reshape(-1)).min())
            points = points[deleteNoise]
            RGB = RGB[deleteNoise]

            projected = self.projectPoints(points, rVector, tVector, camreaMatrix, distortion)

            xPoints, yPoints = projected[:, 0], projected[:, 1]

            projected, RGB = self.filterNoise(projected, RGB, xPoints, yPoints, right_image)

            self.createModel(height, width, projected, RGB)

    def OptimalMatrix(self, camreaMatrix, distortion, right_image):
        camreaMatrix, _ = cv2.getOptimalNewCameraMatrix(camreaMatrix, distortion, (right_image.shape[:2]), 1, (right_image.shape[:2]))
        return camreaMatrix

    def rt_Vectors(self, homogenized, camreaMatrix):
        _, RotationMatrix1, _, transitionVectors = cv2.decomposeHomographyMat(homogenized, camreaMatrix)
        return RotationMatrix1[3], transitionVectors[1]

    def depthMap(self, left_image, right_image, maxValue, mindisp, uniquenessRatio):        
        stereo = cv2.StereoSGBM_create(minDisparity = mindisp,
                                       numDisparities = maxValue - mindisp,
                                       blockSize = 7  , 
                                       uniquenessRatio = uniquenessRatio,
                                       speckleWindowSize = 200,
                                       speckleRange = 2,
                                       disp12MaxDiff = 10,
                                       P1 = 8*3*1**2,
                                       P2 =32*3*1**2)
        return stereo.compute(left_image, right_image)

    def pointsTo3D(self, stereo, transformation):
        points = cv2.reprojectImageTo3D(stereo, transformation)
        points = points.reshape(-1,3)
        return points

    def projectPoints(self, points, rVector, tVector, camreaMatrix, distortion):
        projected, _ = cv2.projectPoints(points, rVector, tVector, camreaMatrix, distortion)
        projected = projected.reshape(-1, 2)
        return projected.astype(int)

    def filterNoise(self, projected, RGB, xPoints, yPoints, right_image):
        height, width = right_image.shape[:2]
        deleteNoise = ((0 <= xPoints & yPoints)&(xPoints < width)&(yPoints < height))
        return projected[deleteNoise], RGB[deleteNoise]

    def createModel(self, height, width, projected, RGB):
        model = np.zeros((height, width, 3), np.uint8)
        model[projected[:, 1],projected[:, 0]] = RGB
        global renderedimage
        renderedimage = model
        cv2.imshow("Rendered Data", model)


#Quiting the windows~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       
class quitWindow():

    def __init__(self):

        exitWindow = tk.Toplevel()

        master = exitWindow

        master.title("Exit")

        Message = tk.Label(exitWindow,
                                text= """Are you sure that you want to quit,
all unsaved data will be lost?""").grid(row=1, column=1, columnspan=2)
        quitButton = tk.Button(master= exitWindow ,
                                text="Yes",
                                command = self.quitALL).grid(row=2, column=1)
        cancelButton = tk.Button(master= exitWindow,
                                text="No",
                                 command = lambda: exitWindow.destroy()).grid(row=2, column=2)

    def quitALL(self):
        app.destroy()

        
#Minimizing/Maximizing the windows~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class minmax_frame():
        def __init__(self):
            global maxScreen
            if maxScreen == True:
                app.attributes("-fullscreen", False)
                maxScreen = False
            elif maxScreen == False:
                maxScreen = True
                app.attributes("-fullscreen", True)
#Error popup window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Errorpopup():
    def __init__(self, error):
        ErrorPopup = tk.Toplevel()

        master = ErrorPopup
        
        master.title("Error")

        Message = tk.Label(ErrorPopup,
                                text= error).grid(row = 1, column = 1,)
        Button = tk.Button(master = ErrorPopup,
                                text = "Ok", command = lambda: ErrorPopup.destroy()).grid(row=2, column = 1)
#Save Files/Presets~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class saveWindow():
    def __init__(self, x):
        Popup = tk.Toplevel()
        Popup.title("Save")
        font = tk.font.Font(size = 15, family="Helvetica")
        self.x = x
        #Labels-------------------------------------------------------------------
        saveLabel = tk.Label(master = Popup,
                                text= """Please enter details to
be saved below""", font = font).grid(row=1, column=2, columnspan=3)
        nameLabel = tk.Label(master = Popup,
                                text= "Name:", font = font).grid(row=4, column=2)
        valueLabel = tk.Label(master = Popup,
                                text= "Values:", font = font).grid(row=5, column=2)
        if len(self.x) == 4:
            tableLabel = tk.Label(master = Popup,
                                  font = font, text= ("""Minimum Disparity: %s"""% x[0] + """
Maximum Disparity: %s"""% x[1] + """
Focal Length: %s"""% x[2] + """
Uniqueness Ratio: %s"""% x[3])).grid(row=5, column=1, columnspan=3)
        else:
            tableLabel = tk.Label(master = Popup,
                                  font = font, text= ("""This will save your
last rendering of two images""")).grid(row=5, column=1, columnspan=3)
        #Button---------------------------------------------------------------------
        saveButton = tk.Button(master= Popup,
                                text="Save as", width = 30, font = font, command = self.save).grid(row=6, column=3)
        #EntryBox-------------------------------------------------------------------
        self.entryBox = tk.Entry(master = Popup, font = font)
        self.entryBox.grid(row=4, column=3)

    def save(self):
        if len(self.entryBox.get()) > 0:
            try:
                if len(self.x) == 4:
                    with open("PresetData.csv", "r") as file:
                        fieldnames = ["UserKey", "Name", "Data"]
                        reader = csv.DictReader(file, fieldnames = fieldnames)
                        for row in reader:
                            if row["UserKey"] == key:
                                if row["Name"] == self.entryBox.get():
                                    arg
                    with open("PresetData.csv", "a") as file:
                        fieldnames = ["UserKey","Name","Data"]
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        writer.writerow({"UserKey": "%s" % key,
                                         "Name": "%s" % self.entryBox.get(),
                                         "Data": self.x})
                else:
                    try:
                        if len(renderedimage) != 0:
                            try:
                                with open("RenderedData.csv", "r") as file:
                                    fieldnames = ["UserKey", "Name", "Data"]
                                    reader = csv.DictReader(file, fieldnames = fieldnames)
                                    for row in reader:
                                        if row["UserKey"] == key:
                                            if row["Name"] == self.entryBox.get():
                                                arg
                                with open("RenderedData.csv", "a") as file:
                                    fieldnames = ["UserKey","Name","Data"]
                                    writer = csv.DictWriter(file, fieldnames = fieldnames)
                                    cv2.ppf_match_3d.writePLY(renderedimage, self.entryBox.get())
                                    writer.writerow({"UserKey": "%s" % key,
                                                     "Name": "%s" % self.entryBox.get()})
                            except:
                                Errorpopup( """Youve already used that name
please choose another""")
                    except:
                        Errorpopup("     Please render a image first     ") 
            except:
                Errorpopup("""Youve already used that name
please choose another""")
        else:
            Errorpopup("Please enter a name")

            
#Open files/Prests~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class openWindow():
    def __init__(self, _type):
        self.type = _type
        Popup = tk.Toplevel()
        Popup.title("Open")
        font = tk.font.Font(size = 20, family="Helvetica")
        #Label--------------------------------------------------
        openLabel = tk.Label(master = Popup,
                         text =  """Select what you want
to open""", font = font).grid(row = 1, column = 1)
        #Listbox ----------------------------------------------
        self.selectionBox = tk.Listbox(master = Popup,
                                  font = font)
        self.selectionBox.grid(row = 2, column = 1)
        self.ListOptions()
        #Button------------------------------------------------
        openButton = tk.Button(master = Popup,
                               text = "Open", font = font, command = self.open)
        openButton.grid(row = 3, column = 1)
        
    def ListOptions(self):
        if self.type == "pre-set":
            with open("PresetData.csv", "r") as file:
                fieldnames = ["UserKey", "Name", "Data"]
                reader = csv.DictReader(file, fieldnames = fieldnames)
                for row in reader:
                    if row["UserKey"] == key:
                        self.selectionBox.insert("end", row["Name"])
        else:
            with open("RenderedData.csv", "r") as file:
                fieldnames = ["UserKey", "Name", "Data"]
                reader = csv.DictReader(file, fieldnames = fieldnames)
                for row in reader:
                    if row["UserKey"] == key:
                        self.selectionBox.insert("end", row["Name"])

    def open(self):
        if len(self.selectionBox.get("anchor")) > 0:
            if self.type == "pre-set":
                with open("PresetData.csv", "r") as file:
                        fieldnames = ["UserKey", "Name", "Data"]
                        reader = csv.DictReader(file, fieldnames = fieldnames)
                        for row in reader:
                            if row["UserKey"] == key:
                                if row["Name"] == self.selectionBox.get("anchor"):
                                    data = row["Data"]
                                    data = data.replace("[", "")
                                    data = data.replace("]", "")
                                    data = data.replace(",", "")
                                    data = data.split(" ")
                                    dataList = list(map(int, data))
                                    minDispSlider.set(data[0])
                                    maxDispSlider.set(data[1])
                                    focalSlider.set(data[2])
                                    uniqueRatioSlider.set(data[3])
            else:
                with open("RenderedData.csv", "r") as file:
                        fieldnames = ["UserKey", "Name", "Data"]
                        reader = csv.DictReader(file, fieldnames = fieldnames)
                        for row in reader:
                            if row["UserKey"] == key:
                                if row["Name"] == self.selectionBox.get("anchor"):
                                    data = row["Name"]
                                    file = cv2.ppf_match_3d.loadPLYSimple(data)
                                    cv2.imshow("Your Rendered Image", file)
                                
        else:
            Errorpopup("Please select a file")

                          
             


app = windows()
app.attributes("-fullscreen", True)
app.mainloop()


