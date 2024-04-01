#for socket programming find TheAlgorithms/Pythonb
#####################################################################################################
####################Importing Module###############################################################
#####################################################################################################
##123456
# from pymodbus.client import ModbusTcpClient

# =============================================================================
# 
# =============================================================================

import uuid

mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
              for ele in range(0,8*6,8)][::-1])
print("MAC address:", mac_address)



from ALARM_INDV import Alarm_INDV
try:
    with open('ALARM/text_0.txt', 'w') as file:
        file.truncate(0)
except:
    pass

from important_Classes import ResizingCanvas      
            
# =============================================================================
# 
#
# =============================================================================


from PIL import ImageGrab
# import openpyxl
from tkinter import filedialog
from tkinter import *      #Tkinter for GUI 
from tkinter import ttk     #Tkinter for GUI ttk
             
from win.Field_Function1 import field_function1      
from win.Field_Function2 import field_function2    
                     
from fourwindow import _fourwindows   #for Four windows MIMICS,Trends,Bar Graph,Alarms

from _3d_Logo_of_TSPL import place_logo_of_TSPL,logo_spin_when_start,logo_stop_when_Freeze #for _3d_Logo_of_TSP

import webbrowser  #to open TSPL website


from Interlock_New import Interlock_ #for Interlock

from PIL import Image, ImageTk #for Images

# from _3D_MIMIC_INDV import CALL_3D_MIMIC#from _3D_MIMIC import _3d_mimic

# from MIMIC_INDV import CALL_MIMIC #Menu of Indiviual MIMIC

from Call_MIMIC import Call_MIMIC

from win.Load_Database import Database_window #Database window

from tkinter import messagebox as mb #messagebox for close window

import globals_gui  as glbg #global gui text varible
import globals_var as gl
import globals_var2 as gl2
from MIMICS_1.Unit_Protection_1 import Unit_Protection_1
# from Graph_INDV import Trends_

# import matplotlib.animation as animation


from BTEMP.Bearing_Temp import Calculate_Temp

# from MIMICS_1.SAT import SAT
# from MIMICS_1.SSP import SSP


from MIMICS_1.SAT_new import SAT_NEW
from MIMICS_1.SSP_NEW import SSP_NEW
# from Graph_123 import Trends001

from MIMICS_1.GSA import GSA

from Graph_INDV1 import Trends_Indv

# from ALARM_INDV import Alarm_INDV
from BAR_GRAPH_INDV import Bar_Graph_Indv
from Status_of_alarms2 import write_alarm_in_text_file
from win.About_Tspl import About_Tspl
from win.MALFUNCTION import MALFUNCTION_WINDOW
# # from MIMIC_INDV_GEN2 import CALL_MIMIC_GEN2
# from win.MALFUNCTION2 import MALFUNCTION_WINDOW_2
from UNIT_PROT_Button import UP_BUTTON_FUN


import time
            
            ##123456---------------------constatnt-------------------------.----
if True:            
                                        
            fourwindow_array_for_root=[0,0,0,0]
            
            flag_as_all_four_window_are_close=False
            
            
            
            
            
            
            
            #####################################################################################################
            ###################-------Main root Window-----------################################################
            #####################################################################################################
            
            toplevel_for_mimic_click=False
            
            toplevel_for_Trends_click=False
            
            toplevel_for_Bar_Graph_click=False
            
            toplevel_for_Alarms_click=False
            
            root_window_click=True
            
            click_event=0
            
            CURRENT_MIMIC=1#tracking which mimic is on window
            
            # =============================================================================
            # ##123456-------------------About Main root WIndow-----------------------------
            # =============================================================================
            
            
            
            
            root = Tk()   
            
            height_of_monitor = root.winfo_screenheight() #height of monitor
             
            width_of_monitor = root.winfo_screenwidth()  # width of monitor
            # print(width_of_monitor)
            
            # root.attributes('-topmost',True)
            
            
            # root.withdraw()
             
            # # SPLASH SCREEN CODE
            # splash_screen = Toplevel(background="white")
            # splash_screen.attributes('-topmost',True)
            # splash_screen.overrideredirect(True)
            # splash_screen.title("Splash Screen")
            # screen_resol=str(width_of_monitor-500)+'x'+str(height_of_monitor-500)
            # splash_screen.geometry(screen_resol)
            # splash_screen.configure(background='black')
             
            # image_1 = Image.open("Images/splash.jpg")
            
            
            # img1_copy = image_1.copy()
            # image1 = image_1.resize((width_of_monitor-400,height_of_monitor-400), Image.ANTIALIAS)
              
            # background_image = ImageTk.PhotoImage(image1)
            # label = Label(splash_screen, image = background_image)
            # label.place(relx=0.15,rely=0.2)
            # splash_screen.update()
             
            # # MAIN WINDOW CODE + Other Processing
            # # time.sleep(7)
            # splash_screen.attributes('-topmost',0) 
            # # Start the event loop
            # root.deiconify()
            
            
            temp_var_count=0
            # def wait_function():
            #     global temp_var_count
            #     temp_var_count+=1
            #     print(temp_var_count)
            #     splash_screen.after(1000,wait_function())
            
            
            # wait_function()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                               #Initializing root window
            
            glbg.global_root_var=root
            
            root.configure(background='#5A5A5A')
            
            root.focus_force()               #foucs to window
            
            root.title('HYDRO POWER PLANT SIMULATOR')  #Title of root window
            
            root.state(newstate='normal')   #deafult form normal=on screen ,Iconic=on taskbar
            
            root.iconbitmap("images/logo.ico")  # icon of root window
            
            
            
            
            root.geometry(str(width_of_monitor)+'x'+str(height_of_monitor-70)) # size of root window as state is zoomed(line no 30) this line have no affect
            
            root.state("zoomed")      # window will automatically adjusted to screen  
            
            root.resizable(1,1)       # window resize (width,height) 0=not resize,1=resize allow    
            
            root.withdraw()
            # ============================================================================
            # --------------------End of Main window----------------------------------------
            # =============================================================================
            
            
            
            
            # =============================================================================
            # 
            # =============================================================================
            
            
            
            # =============================================================================
            # 
            # =============================================================================
            
            
            
            
            
            
            
            # =============================================================================
            # -----------------------MAIN PAGE--------------------------------------------
            # =============================================================================
            
            #class for to allow to resize the canvas
            
            
            
            
            
            
            #Frame to divide window
            Frame1 = Frame(root) #Frame for Heading
            
            Frame1.place(relx=0.0, rely=0.0, relheight=0.05, relwidth=1.008) #location and size of frame
            
            Frame1.configure(relief='groove') #frame groove
            
            Frame1.configure(borderwidth="2") #border
            
            Frame1.configure(highlightbackground="Black", highlightthickness=5 ) #border color size 5
            
            Frame1.configure(background="grey") #background grey
            
            
            Frame2 = Frame(root) #Frame for Mainframe
            
            Frame2.place(relx=0.0, rely=0.05, relheight=0.83, relwidth=1.008) #location and size of frame
            
            Frame2.configure(relief='groove') #frame groove
            
            Frame2.configure(borderwidth="2") #border
            
            Frame2.configure(background="#5A5A5A") #background lightgrey
            
            
            
            Frame3 = Frame(root) #Frame for  Toolbar
            
            Frame3.place(relx=0.0, rely=0.875, relheight=0.075, relwidth=1.008) #location and size of frame
            
            Frame3.configure(relief='groove') #frame groove
            
            Frame3.configure(borderwidth="2") #border
            
            Frame3.configure(background="#5A5A5A") #background lightgrey
            
            
            
            
            Frame4 = Frame(root) #Frame for Status Bar
            
            Frame4.place(relx=0.0, rely=0.95, relheight=0.05, relwidth=1.008) #location and size of frame
            
            Frame4.configure(relief='groove') #frame groove
            
            Frame4.configure(borderwidth="2") #border
            
            Frame4.configure(background="#5A5A5A")#background lightgrey
            
            
            
            
            
            
            
            # =============================================================================
            # ----------------------Upper Heading-----------------------------------------
            # =============================================================================
            
            
            
            Frame1_for_Heading=Frame1 #creating varible for use 
              
            img= (Image.open("Images\LOGO.png")) #getting Image
              
            resized_image= img.resize((40,30), Image.LANCZOS) #resize image
            
            new_image= ImageTk.PhotoImage(resized_image) #Making it into IMGAETK form
              
            label_ = Label(Frame1_for_Heading, image = new_image) #placeing onto Label
            
            label_.place(relx=0.005,rely=0) #placing Image relx=relative x axis,rely=relative y axis
              
              
            L_label=Label(Frame1_for_Heading,text='HYDRO POWER PLANT SIMULATION BY TSPL',anchor='w' ,font=('Times 18'),background='Grey',foreground='White') #create Label
            
            L_label.place(relx=0.05,rely=0.3,relheight=0.6,relwidth=0.5)
              
            
            glbg.Heading_Name='MAIN MENU'
            
            label_heading=Label(Frame1_for_Heading,text=glbg.Heading_Name,anchor='w',font=('Times 18'),background='Grey',foreground='White')
            
            label_heading.place(relx=0.5,rely=0.3,relheight=0.6,relwidth=0.5)
            
            label_heading_time=Label(Frame1_for_Heading,text='000',anchor='w',font=('Times 18'),background='Grey',foreground='White')
            
            label_heading_time.place(relx=0.8,rely=0.3,relheight=0.6,relwidth=0.5)
            
            
            # def check_Heading_Name():
                
               
                
            #     root.after(100,check_Heading_Name)
            
            
            # check_Heading_Name()
            
            def on_resize(event): #it change vlue of varible of width and height of monitor
            
                global width_of_monitor,height_of_monitor
                
                width_of_monitor = event.width #set new width
                
                height_of_monitor = event.height #set new height
                
                width = event.width
                height = event.height
                
                screen_width =root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                width_percent = (width / screen_width) * 100
                height_percent = (height / screen_height) * 100
                val=width_percent*height_percent
               
                x=val*20/9000
                # print(x)
                if x<10:
                    x=10
                new_font='Times '+str(int(x))
                # L_label.configure(font=new_font)
                # label_heading.configure(font=new_font)
                # label_heading_time.configure(font=new_font)
              
            
            
            
            # root.bind("<Configure>", on_resize) #call fun when resize or 
            
             # =============================================================================
             # ----------------------Upper Heading End-----------------------------------------
             # =============================================================================
            
            
            
            class ResizingNotebook(ttk.Notebook):
                def __init__(self, parent, **kwargs):
                    ttk.Notebook.__init__(self, parent, **kwargs)
                    parent.bind("<Configure>", self.on_resize)
            
                def on_resize(self, event):
                    self.configure(width=event.width, height=event.height)
            
            
            
            
            class main_page_:
            
               def __init__(self,root):
                   # canvas=canvas
                       self.root = root
                       self.window=root
                       self.frames = []
                       self.current_frame = 0
                       self.number=0
                       self.create_frames()
                   
                     

               def create_frames(self):
                  self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                   
                  self.frame.config(background='#5A5A5A')
                  self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

             
                  B1 = Button(self.frame, text ="1)  UNIT PROTECTION", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_1_fun)
                  B2 = Button(self.frame, text ="2)  SEQUENCE AFTER TRIP", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_2_fun)
                  B3 = Button(self.frame, text ="3)  SEQUENCE OF STOP PROCEDURE", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_3_fun)
                  
                  B5 = Button(self.frame, text ="4)  INTERLOCK", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_5_fun)
                  B6 = Button(self.frame, text ="5)  TRIP LOGIC", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_6_fun)
                  # B7 = Button(self.frame, text ="6)  PLANT ARCHITECTURE", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_7_fun)
                  
                  B8 = Label( self.frame, text ="GENERATOR ", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='n',font=('Times 16'))
                  B4 = Button(self.frame, text ="7)  MIMIC MENU", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_4_fun)
                  B9 = Button(self.frame, text ="8)  TRENDS MENU", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_9_fun)
                  B10 = Button(self.frame, text ="9)  ALARM MENU", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_10_fun)
                  B11 = Button(self.frame, text ="10)  BAR GRAPH MENU", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_11_fun)
                  # B12 = Label(self.frame, text ="GENERATOR 2", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='n',font=('Times 16'))
                  # B13 = Button(self.frame, text ="Bar Graph Menu", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_13_fun)
                  # B13 = Button(self.frame, text ="11)  MIMIC MENU", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_13_fun)
                  # B14 = Button(self.frame, text ="12)  TRENDS MENU", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_9_fun)
                  # B15 = Button(self.frame, text ="13)  ALARM MENU", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_10_fun)
                  # B16 = Button(self.frame, text ="14)  BAR GRAPH MENU", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_11_fun)
                  # B14 = Button(self.frame, text ="Mimic Menu", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_14_fun)
                  # B15 = Button(self.frame, text ="Panel Menu", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_15_fun)
                  # B16 = Button(self.frame, text ="All Pictures", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_10_fun)
                  # B17 = Button(self.frame, text ="Alarm Menu", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_11_fun)
                  # B18 = Button(self.frame, text ="Trend Menu", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_12_fun)
                  # B19 = Button(self.frame, text ="Bar Graph Menu", relief=SUNKEN ,background='#5A5A5A',foreground='White',width=120,anchor='w',font=('Times 16'),command=self.button_13_fun)
                
                 
                  L1=Label(self.frame,text='Hydro Power Plant Simulation By TSPL',font=('Times 18'),background='#5A5A5A',foreground='White',anchor=CENTER )
                  L1.place(relx=0.1,rely=0.0,relwidth=0.8,relheight=0.05)
                  
           
             
                  B1.place(relx=0.02,rely=0.05,relwidth=0.9,relheight=0.05)
                  B2.place(relx=0.02,rely=0.10,relwidth=0.9,relheight=0.05)
                  B3.place(relx=0.02,rely=0.15,relwidth=0.9,relheight=0.05)
                  B4.place(relx=0.02,rely=0.45,relwidth=0.9,relheight=0.05)
                  
                  B5.place(relx=0.02,rely=0.20,relwidth=0.9,relheight=0.05)
                  B6.place(relx=0.02,rely=0.25,relwidth=0.9,relheight=0.05)
                  # B7.place(relx=0.02,rely=0.30,relwidth=0.9,relheight=0.05)
                  
                  B8.place(relx=0.02,rely=0.375,relwidth=0.9,relheight=0.05)
                  B9.place(relx=0.02,rely=0.50,relwidth=0.9,relheight=0.05)
                  B10.place(relx=0.02,rely=0.55,relwidth=0.9,relheight=0.05)
                  B11.place(relx=0.02,rely=0.60,relwidth=0.9,relheight=0.05)
                  
                  
                  # B12.place(relx=0.02,rely=0.675,relwidth=0.9,relheight=0.05)
                  # B13.place(relx=0.02,rely=0.75,relwidth=0.9,relheight=0.05)
                  # B14.place(relx=0.02,rely=0.80,relwidth=0.9,relheight=0.05)
                  # B15.place(relx=0.02,rely=0.85,relwidth=0.9,relheight=0.05)
                  # B16.place(relx=0.02,rely=0.90,relwidth=0.9,relheight=0.05)
                  # B17.place(relx=0.05,rely=0.85,relwidth=0.9,relheight=0.05)
                  # B18.place(relx=0.05,rely=0.90,relwidth=0.9,relheight=0.05)
                  # B19.place(relx=0.05,rely=0.95,relwidth=0.8,relheight=0.05)
                              
                 

                        
                      
              
               def button_1_fun(self):
                   
                   
                   self.frame.destroy()
                   self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                    
                   self.frame.config(background='#5A5A5A')
                   self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                   Unit_Protection_1(self.frame, self.root)
                   
                   #self.Notebook_main_page.select(1)
                   glbg.var_to_track_notebook_page=1
                   
                   glbg.Heading_Name=('UNIT PROTECTION MENU')
                 
                   # MIMIC(self.canvas_1,self.window) 
               
               
               def button_2_fun(self):
                   
                   self.frame.destroy()
                   self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                    
                   self.frame.config(background='#5A5A5A')
                   self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                   SAT_NEW(self.frame, self.root)
                   
                   #self.Notebook_main_page.select(2)
                   glbg.var_to_track_notebook_page=2
                   
                  
                   # MIMIC(self.canvas_1,self.window) 
               
               def button_3_fun(self):
                   
                   
                   
                 self.frame.destroy()
                 self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                  
                 self.frame.config(background='#5A5A5A')
                 self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                 SSP_NEW(self.frame, self.root)#self.Notebook_main_page.select(3)
                 glbg.var_to_track_notebook_page=3
                   
                  
                   # CALL_3D_MIMIC(self.canvas_3,self.window)
                   
               def button_4_fun(self):
                   
                  self.frame.destroy()
                  self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                   
                  self.frame.config(background='#5A5A5A')
                  self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                  self.MIMIC_INDV_OBJ=Call_MIMIC(self.frame)#self.Notebook_main_page.select(4)
                  glbg.var_to_track_notebook_page=4
                  glbg.Heading_Name='GENERATOR 1 MIMIC MENU'
                  
                   # MIMIC(self.canvas_1,self.window) 
               
               def button_5_fun(self):
                   self.frame.destroy()
                   self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                    
                   self.frame.config(background='#5A5A5A')
                   self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                   self.Interlock_obj=Interlock_(self.frame, self.root,self.root)#self.Notebook_main_page.select(5)
                   glbg.var_to_track_notebook_page=5
                   self.Interlock_obj.Trip_not_logic()     
                   
                  
                   glbg.Heading_Name='INTERLOCK'
                   # Interlock_(self.canvas_5,self.window)
               
               def button_6_fun(self):
                   self.frame.destroy()
                   self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                    
                   self.frame.config(background='#5A5A5A')
                   self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                   self.Interlock_obj=Interlock_(self.frame, self.root,self.root)#self.Notebook_main_page.select(5)
                   self.Interlock_obj.Trip_logic()
                   glbg.var_to_track_notebook_page=5
                   glbg.Heading_Name='TRIP'
                   self.Interlock_obj.Trip_logic()
                   
                   # self.Interlockt.Trip_logic()
                   
                  
                   
                  
                   # MIMIC(self.canvas_1,self.window) 
               
               
               def button_7_fun(self):
                   
                
                 Unit_Protection_1(self.frame, self.root)#self.Notebook_main_page.select(7)
                 glbg.var_to_track_notebook_page=7
                  
                   # MIMIC(self.canvas_1,self.window) 
               
               
               def button_8_fun(self):
                   
                   
                  self.frame.destroy()
                  self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                   
                  self.frame.config(background='#5A5A5A')
                  self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                  Unit_Protection_1(self.frame, self.root)#self.Notebook_main_page.select(8)
                  glbg.var_to_track_notebook_page=8
                  # ani_1 = animation.FuncAnimation(self.graph.fig1, self.graph.animate, interval = 1000, 
                  #                                 fargs=())
                   # __mimic__(self.canvas_1,self.window) 
                   
                   
                   
               def button_9_fun(self):
                   
                   self.frame.destroy()
                   self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                    
                   self.frame.config(background='#5A5A5A')
                   self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                   self.Trends_Indv_OBJ=Trends_Indv(self.frame, self.root,self.root)#self.Notebook_main_page.select(9)
                   glbg.Heading_Name='TRENDS MENU'
                   glbg.var_to_track_notebook_page=9
                   
                  
                   # CALL_MIMIC(self.canvas_9,self.window)
                   
               def button_10_fun(self):
                      glbg.Heading_Name='ALARM MENU'
                      self.frame.destroy()
                      self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                       
                      self.frame.config(background='#5A5A5A')
                      self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                      self.ALARM_INDV_OBJ=Alarm_INDV(self.frame, self.root, self.root)#self.Notebook_main_page.select(10)
                      glbg.var_to_track_notebook_page=10
                      # self.Interlockt.Trip_logic()
                  
                   # __mimic__(self.canvas_1,self.window) 
               
               def button_11_fun(self):
                   glbg.Heading_Name='BAR GRAPH MENU'
                   self.frame.destroy()
                   self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                    
                   self.frame.config(background='#5A5A5A')
                   self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                   self.BAR_Indv_OBJ=Bar_Graph_Indv(self.frame, self.root, self.root)#self.Notebook_main_page.select(11)
                   glbg.var_to_track_notebook_page=11
                   # __mimic__(self.canvas_1,self.window) 
               
               
               def button_12_fun(self):
                   
                  self.frame.destroy()
                  self.frame = Frame(self.root,highlightbackground='Black', highlightthickness=5)
                   
                  self.frame.config(background='#5A5A5A')
                  self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Initially show frame1

                  Unit_Protection_1(self.frame, self.root)#self.Notebook_main_page.select(12)
                  glbg.var_to_track_notebook_page=12
                   
                  
                    
                    
               
                    
                     
            
            
            
            
            
            
            
            main_page_obj=main_page_(Frame2)
            glbg.MAINFRAME_OBJ=main_page_obj
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            ##123456
            #####################################################################################################################
            ###########-------creating canvas for 4 windows------################################################################# 
            ####################################################################################################################  
            
            # canvas_for_four_window=Canvas(root)
            
            # canvas_for_four_window.place(x=0,y=0)
            
            #####################################################################
            #---------------connected to file fourwindows.py--------------------
            #####################################################################
            
            four_windows=_fourwindows(root)#  creating instace of class as it has self
            
            
            #####################################################################
            #-------------canvas_for_four_window winodw  End------------------------
            #####################################################################
            # print(width_of_monitor)
            
            toplevel_for_mimic=Toplevel(root)
            toplevel_for_mimic.wm_transient(root)
            window_for_mimic_size_and_loc_org=str(width_of_monitor//2)+'x'+str(int((height_of_monitor//2.725)))+'+'+'0'+'+'+'45'
            
            toplevel_for_mimic.geometry(window_for_mimic_size_and_loc_org)
            #--------------------------------------------------------------------------
            #--------------------------------------------------------------------------
            toplevel_for_Trends=Toplevel(root)
            toplevel_for_Trends.wm_transient(root)
            open_Trends_window_size_and_loc=str(width_of_monitor//2)+'x'+str(int((height_of_monitor//2.725)))+'+'+str(width_of_monitor//2)+'+'+str(int((height_of_monitor//2.725)+45+30))
            
            toplevel_for_Trends.geometry( open_Trends_window_size_and_loc)
            #--------------------------------------------------------------------------
            #--------------------------------------------------------------------------
            
            
            toplevel_for_Bar_Graph=Toplevel(root)
            toplevel_for_Bar_Graph.wm_transient(root)
            open_Bar_Graph_window_size_and_loc=str(width_of_monitor//2)+'x'+str(int((height_of_monitor//2.725)))+'+'+str(width_of_monitor//2)+'+'+'45'
             
            toplevel_for_Bar_Graph.geometry(open_Bar_Graph_window_size_and_loc)
            
            #--------------------------------------------------------------------------
              #--------------------------------------------------------------------------
            toplevel_for_Alarms=Toplevel(root)
            toplevel_for_Alarms.wm_transient(root)
            open_Alarms_window_size_and_loc=str(width_of_monitor//2)+'x'+str(int((height_of_monitor//2.725)))+'+'+'0'+'+'+str(int((height_of_monitor//2.725)+45+30))
            
            
            toplevel_for_Alarms.geometry(open_Alarms_window_size_and_loc)
            
            
            # =============================================================================
            # =============================================================================
            # # 
            
            
            
            
            
            
            # =============================================================================
            # =============================================================================
            # # 
            # =============================================================================
            # =============================================================================
            
            toplevel_for_Alarms.withdraw()
            toplevel_for_Bar_Graph.withdraw()
            toplevel_for_mimic.withdraw()
            toplevel_for_Trends.withdraw()
            
            
            
            
            
            # =============================================================================
            # =============================================================================
            # # 
            # =============================================================================
            # =============================================================================
            
            
            root.withdraw()
             
            # SPLASH SCREEN CODE
            splash_screen = Toplevel(background="white")
            splash_screen.attributes('-topmost',True)
            splash_screen.overrideredirect(True)
            splash_screen.title("Splash Screen")
            screen_resol=str(width_of_monitor )+'x'+str(height_of_monitor )
            splash_screen.geometry(screen_resol)
            splash_screen.configure(background='black')
             
            image_1 = Image.open("Images/splash.jpg")
            
            
            img1_copy = image_1.copy()
            image1 = image_1.resize((width_of_monitor-400,height_of_monitor-400), Image.LANCZOS)
              
            background_image = ImageTk.PhotoImage(image1)
            label = Label(splash_screen, image = background_image)
            label.place(relx=0.15,rely=0.2)
            splash_screen.update()
             
            # MAIN WINDOW CODE + Other Processing
            # time.sleep(7)
            splash_screen.attributes('-topmost',0) 
            # Start the event loop
            
            
            # =============================================================================
            # =============================================================================
            Four_window_Trends_obj=four_windows.open_Trends_window(toplevel_for_Trends)
            
            Four_window_Bar_Graph_obj=four_windows.open_Bar_Graph_window(toplevel_for_Bar_Graph)
            
            Four_window_Alarms_obj=four_windows.open_Alarms_window(toplevel_for_Alarms)
            
            Four_window_Mimic_obj=four_windows.open_mimic_window(toplevel_for_mimic)
            
          
            
          
            ##123456 
            
            
            ##123456----------------------------Menubar----------------------------------
            #################################################################################################
            #-----------------------------Menu bar---------------------------------------------------------------
            #################################################################################################
            # =============================================================================
            # MODbus 22-3-23
            # =============================================================================
            
            

            # print(r_values.registers)
            # client1.close()
            
            
            # import threading
             
            
            
            
            
            # thread1 = thread("GFG", 1000)
            # thread1.start()    
                
            
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            def Store_value_of_array():
                
                    
                
                # tb_temp_arr=[0]
                if glbg.Run_command_of_simulator_var:
                    if not gl.ST_CBLV :
                        gl.V_STHV_kV=0    #station hv side voltage    
                        gl.V_STLV_kV=0 
                    
                    
                    
                    gl.tb_temp_arr.append(gl.tb_temp)
                    
                    # ugb_temp_arr=[0]
                    gl.ugb_temp_arr.append(gl.ugb_temp)
                    
                    # lgb_temp_arr=[0]
                    gl.lgb_temp_arr.append(gl.lgb_temp)
                    
                    # tgb_temp_arr=[0]
                    gl.tgb_temp_arr.append(gl.tgb_temp)
                    
                    # xfr_oil_temp_arr=[0]
                    gl.xfr_oil_temp_arr.append(gl.xfr_oil_temp)
                    
                    # xfrm_stn_oil_temp_arr=[0]
                    gl.xfrm_stn_oil_temp_arr.append(gl.xfrm_stn_oil_temp)
                    
                    # gen_aircool_temp_arr=[0]
                    gl.gen_aircool_temp_arr.append(gl.gen_aircool_temp)
                    
                    # Temp_of_Oil_of_UAT_arr=[0]
                    gl.Temp_of_Oil_of_UAT_arr.append(gl.Temp_of_Oil_of_UAT)
                    
                    # Ho_in_m_arr=[0]
                    gl.Ho_in_m_arr.append(gl.Ho_in_m)
                    
                    # g1_arr=[0]
                    gl.g1_arr.append(gl.Gate_OP_var )
                    
                    # fgen_Hz1_arr=[0]
                    gl.fgen_Hz1_arr.append(gl.fgen_Hz1)
                    
                    # U1_mps_arr=[0]
                    gl.U1_mps_arr.append(gl.U1_mps)
                    
                    gl.water_diss_arr.append(gl.Water_Discharge)
                 
                    # I_exc_kA1_arr=[0]
                    gl.I_exc_kA1_arr.append(gl.I_exc_kA1)
                    
                    # Pgen_MW1_arr=[0]
                    gl.Pgen_MW1_arr.append(gl.Pgen_MW1)
                    
                    # Qgen_MVAr1_arr=[0]
                    gl.Qgen_MVAr1_arr.append(gl.Qgen_MVAr1)
                    
                    # E_exc_kV1_arr=[0]
                    gl.E_exc_kV1_arr.append(gl.E_exc_kV1)
                    
                    # wrpm1_arr=[0]
                    gl.wrpm1_arr.append(gl.wrpm1)
                    
                    # Vgen_RMS1_arr=[0]
                    gl.Vgen_RMS1_arr.append(gl.Vgen_RMS1)
                    
                    # Igen_RMS1_arr=[0]
                    gl.Igen_RMS1_arr.append(gl.Igen_RMS1*1000)
                   
                    
                    # print('-----------------',gl.Vref1,gl.Pref1,gl.wref1)
                    
                    
                    
                    
                    gl.GRAPH_1_LIST_ARRAY=[gl.tb_temp_arr,gl.ugb_temp_arr,gl.lgb_temp_arr,gl.tgb_temp_arr]
                    gl.GRAPH_2_LIST_ARRAY=[gl.xfr_oil_temp_arr,gl.xfrm_stn_oil_temp_arr,gl.gen_aircool_temp_arr,gl.Temp_of_Oil_of_UAT_arr]
                    
                    gl.GRAPH_3_LIST_ARRAY=[gl.Ho_in_m_arr,gl.g1_arr,gl.fgen_Hz1_arr,gl.U1_mps_arr]
                    gl.GRAPH_4_LIST_ARRAY=[gl.water_diss_arr,gl.Vgen_RMS1_arr,-1,-1]
                    gl.GRAPH_5_LIST_ARRAY=[gl.Pgen_MW1_arr,gl.Qgen_MVAr1_arr,-1,-1]
                    gl.GRAPH_6_LIST_ARRAY=[gl.E_exc_kV1_arr,gl.wrpm1_arr,-1,-1]
                    
                    gl.GRAPH_7_LIST_ARRAY=[gl.I_exc_kA1_arr,gl.Igen_RMS1_arr,-1,-1]
                    
                    
                    
                    
# =============================================================================
#                     
# =============================================================================
                    

                                        
                    gl2.tb_temp_arr_2.append(gl2.tb_temp_2)
                    gl2.ugb_temp_arr_2.append(gl2.ugb_temp_2)
                    gl2.lgb_temp_arr_2.append(gl2.lgb_temp_2)
                    gl2.tgb_temp_arr_2.append(gl2.tgb_temp_2)
                    
                    gl2.xfr_oil_temp_arr_2.append(gl2.xfr_oil_temp_2)
                    gl2.xfrm_stn_oil_temp_arr_2.append(gl2.xfrm_stn_oil_temp_2)
                    gl2.gen_aircool_temp_arr_2.append(gl2.gen_aircool_temp_2)
                    gl2.Temp_of_Oil_of_UAT_arr_2.append(gl2.Temp_of_Oil_of_UAT_2)
                    
                    gl2.Ho_in_m_arr_2.append(gl.Ho_in_m)
                    gl2.g2_arr_2.append(gl2.Gate_OP_var2)
                    gl2.fgen_Hz2_arr_2.append(gl2.fgen_Hz2)
                    gl2.U2_mps_arr_2.append(gl2.U2_mps)
                    
                    # U1_mps_arr.append(
                    gl2.water_diss_arr_2.append(gl2.Water_Discharge2 )
                    gl2.I_exc_kA2_arr_2.append(gl2.I_exc_kA2)
                    
                    gl2.Pgen_MW2_arr_2.append(gl2.Pgen_MW2)
                    gl2.Qgen_MVAr2_arr_2.append(gl2.Qgen_MVAr2)
                    
                    gl2.E_exc_kV2_arr_2.append(gl2.E_exc_kV2)
                    gl2.wrpm2_arr_2.append(gl2.wrpm2)
                    
                    gl2.Vgen_RMS2_arr_2.append(gl2.Vgen_RMS2)
                    gl2.Igen_RMS2_arr_2.append(gl2.Igen_RMS2)
                    
                    
                    gl2.GRAPH_1_LIST_ARRAY=[gl2.tb_temp_arr_2,gl2.ugb_temp_arr_2 , gl2.lgb_temp_arr_2 , gl2.tgb_temp_arr_2]
                    gl2.GRAPH_2_LIST_ARRAY=[gl2.xfr_oil_temp_arr_2 , gl2.xfrm_stn_oil_temp_arr_2 , gl2.gen_aircool_temp_arr_2 , gl2.Temp_of_Oil_of_UAT_arr_2]

                    gl2.GRAPH_3_LIST_ARRAY=[gl2.Ho_in_m_arr_2 , gl2.g2_arr_2 , gl2.fgen_Hz2_arr_2 , gl2.U2_mps_arr_2]
                    gl2.GRAPH_4_LIST_ARRAY=[gl2.water_diss_arr_2 , gl2.I_exc_kA2_arr_2 , -1 , -1]
                    gl2.GRAPH_5_LIST_ARRAY=[gl2.Pgen_MW2_arr_2 , gl2.Qgen_MVAr2_arr_2 , -1 , -1]
                    gl2.GRAPH_6_LIST_ARRAY=[gl2.E_exc_kV2_arr_2 , gl2.wrpm2_arr_2 , -1 , -1]
                    gl2.GRAPH_7_LIST_ARRAY=[gl2.Vgen_RMS2_arr_2 , gl2.Igen_RMS2_arr_2 , -1 , -1]
                    
                    
                    
                    
                    
                
                
               

                
                
                    
                    
                
                root.after(1000,Store_value_of_array)
            
            #############################################################################################################
            #####################----------Function of Menu -------------#####################################
            #######################################################################################################
            
            
            
           
                
            is_Run_function_called=False
            countdown_flage=True
            def LOOP():
               
                # print('123')
                try:
                    glbg.global_root_var.update()
                    print("refresh")
                except:
                    pass
                root.after(1,LOOP)
            # LOOP()
             
            def Run_command_of_simulator():  
                  global is_Run_function_called ,countdown_flage ## it will spin the 3d logo
                  if not is_Run_function_called:
                        print("Run Mode")
                        logo_spin_when_start()
                        state_of_mimic.configure(text='Run')
                        glbg.countdown_flage_1=True
                        Count_time()
                       
                        from main_program import Run_Prgram
                        import threading
                        
                        gl.ST_CBHV=1
                        gl.ST_CBLV=1
                        gl.V_220_kV=200.0  
                        # gl.ST_UAT1_CB=1
                        gl.V_STHV_kV=29.94    #station hv side voltage    
                        gl.V_STLV_kV=0.44 
                        
                        
                        
                        is_Run_function_called=True
                        
                        Store_value_of_array()
                        # t1=threading.Thread(target=Store_value_of_array)
                        # t1.start()
                        glbg.Run_command_of_simulator_var=True
                        glbg.SIMULATION_START=True
                        
                        Calculate_Temp()
                        # Run_Prgram()
                        t2=threading.Thread(target=Run_Prgram)
                        t2.start()
                        LOOP()
                        # t3=threading.Thread(target=LOOP)
                        # t3.start()
                        
                        # Run_Prgram()
                        # ModBUS_data_send()
                        
                
            # glbg.Run_command_of_simulator_var=Run_command_of_simulator
            def Continue_command_of_simulator():
                global is_Run_function_called,countdown_flage ## it will stop the 3d logo
                is_Run_function_called=True
                glbg.countdown_flage_1=True
                glbg.Run_command_of_simulator_var=True
                state_of_mimic.configure(text='Run')
                
                logo_spin_when_start()
            def Freeze_command_of_simulator():     
                        global is_Run_function_called,countdown_flage ## it will stop the 3d logo
                        is_Run_function_called=False
                        glbg.countdown_flage_1=False
                        glbg.Run_command_of_simulator_var=False
                        state_of_mimic.configure(text='Freeze')
                        
                        logo_stop_when_Freeze()
            
            
            
            def Design_cold_fun():
                global hours,minutes,seconds,countdown_flage
                hours=0
                minutes=0
                seconds=0
                glbg.countdown_flage_1=False
                # countdown_flage=False
                gl.Design_cold=True
                gl.load_database=False
                
                gl.load_database_40_mw=False
                
                # gl.Design_cold_fuction()
                
            def destroy_all_windows():  # Quite To windows Button on Menubar
            
                      on_closing()
                        
                      
                    
            import threading
            import cv2
            import os
            import numpy as np
            class ScreenRecorder:
                def __init__(self,root):
                    self.root=root
                   
            
                def start_recording(self):
                    self.recording = True
                    
                    Session_.entryconfig("Start Recording", state="disable")
                    Session_.entryconfig("Stop Recording", state="normal")
                    
                  
                
                    threading.Thread(target=self.record_screen).start()
            
                def stop_recording(self):
                    self.recording = False
                    Session_.entryconfig("Start Recording", state="normal")
                    Session_.entryconfig("Stop Recording", state="disable")
                    # self.start_button.configure(state="normal")
                    # self.stop_button.configure(state="disabled")
            
                    # Prompt for saving the video file
                    file_path = filedialog.asksaveasfilename(defaultextension=".avi")
                    if file_path:
                        self.save_video(file_path)
            
                def record_screen(self):
                    screen_width = self.root.winfo_screenwidth()
                    screen_height = self.root.winfo_screenheight()
                    screen_size = (screen_width, screen_height)
            
                    # Video settings
                    output_file = 'screen_record.avi'
                    fps = 30.0
                    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                    self.video_out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)
            
                    while self.recording:
                        # Capture screen
                        img = ImageGrab.grab()
                        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            
                        # Write frame to video file
                        self.video_out.write(frame)
            
                def save_video(self, file_path):
                    # Release resources
                    self.video_out.release()
            
                    # Rename output file
                    os.rename('screen_record.avi', file_path)
                        
                    
            Screen_recoder=ScreenRecorder(root)
            
            
            menubar = Menu(root) #Declaring Menu
            
            
            #add_command=Normal Button
            #add_radiobutton=radio button
            #add_separator=Seprator
            #
            #------------------------------Menu Session Start-------------------------------------------
            #---------------------------------------------------------------------------------------------
            
            Session_ = Menu(menubar, tearoff = 0)
            
            #-------------------sub menu for  Initialize-----------------------------------------------
            
            sub_menu_Initialize = Menu(Session_, tearoff=0)
            
            sub_menu_Initialize.add_command(label='Design')
            
            sub_menu_Initialize.add_command(label='Cold',command=Design_cold_fun )
            
            
            #-------------------sub menu for  Bakctrack---------------------------------------------
            
            # sub_menu_for_Bakctrack = Menu(Session_, tearoff=0)
            
            # sub_menu_for_Bakctrack.add_radiobutton(label='Enable')
            
            # sub_menu_for_Bakctrack.add_radiobutton(label='Disable')
            
            menubar.add_cascade(label ='Session', menu = Session_)
            
            Session_.add_command(label ='Continue', command = Continue_command_of_simulator)
            
            Session_.add_cascade(label="Initialize",menu=sub_menu_Initialize)
            
            Session_.add_separator()
            
            # Session_.add_command(label ='Snapshot', command = None)
            
            # Session_.add_cascade(label ='Bakctrack', menu=sub_menu_for_Bakctrack)
               
            Session_.add_command(label ='Run', command = Run_command_of_simulator)
            
            Session_.add_command(label ='Freez', command = Freeze_command_of_simulator)
             
            Session_.add_separator()
            Session_.add_command(label ='Start Recording', command = Screen_recoder.start_recording )
            
            Session_.add_command(label ='Stop Recording', command = Screen_recoder.stop_recording)
            Session_.add_separator()
            
            Session_.add_command(label ='Quite to windows', command = destroy_all_windows)
            
            
            #------------------------Menu Session  END -------------------------------------------
            def show_database_loaded_message(root):
                # create the top-level window
                top = Toplevel(root)

                # set the title and size of the window
                top.title("Database Loaded")
                top.geometry("300x100")

                # calculate the position of the window to center it on the screen
                screen_width = top.winfo_screenwidth()
                screen_height = top.winfo_screenheight()
                x = int((screen_width - top.winfo_reqwidth()) / 2)
                y = int((screen_height - top.winfo_reqheight()) / 2)
                top.geometry("+{}+{}".format(x, y))

                # create a label with the message
                label = Label(top, text="The database has already been loaded.")
                label.place(relx=0.15,rely=0.1)

                # create an OK button that closes the window when clicked
                ok_button = Button(top, text="OK", command=top.destroy,width=10)
                ok_button.place(relx=0.35,rely=0.5)

            def Database_window_load(event):
                
                if not gl.is_database_is_loaded:
                    database_toplvel=Toplevel(root)
                    database_toplvel.wm_transient(root)
                    Database_window(database_toplvel,root)
                    
                else:
                    show_database_loaded_message(root)
            
            
            # =============================================================================
            # =============================================================================
            # # CTLR+S SAVE
            # =============================================================================
            # =============================================================================
            # def Save_Data_Into_Database(e):
                
                
               
               
                
            #     filename = filedialog.asksaveasfilename(filetypes = (("xlsx files", "*.xlsx"), ("All files", "*.*")),defaultextension='.xlsx')
                
                
                
                
            #     wrkb = openpyxl.Workbook()
            #     ws = wrkb.worksheets[0]
            #     row_number = 2
              
                
               
              
                
             
                
               
             
                
            #     a="tb_temp"
            #     b="ugb_temp"
            #     c="lgb_temp"
            #     d="tgb_temp"
                
            #     e="xfr_oil_temp"
            #     f="xfrm_stn_oil_temp"
            #     g="gen_aircool_temp"
            #     h="Temp_of_Oil_of_UAT"
                
            #     i="Ho_in_m"
            #     j="Gate_OP_var"
            #     k="fgen_Hz1"
            #     l="U1_mps"
                
            #     m="Vgen_RMS1"
            #     n="Water_Discharge"
                
            #     o="Pgen_MW1"
            #     p="Qgen_MVAr1"
                
            #     q="E_exc_kV1"
            #     r="wrpm1"
                
            #     s="I_exc_kA1"
            #     t="Igen_RMS1"
            #     Array_of_var=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
            #     # A_1.insert(0,a)
            #     # rate.insert(0,b)
            #     for i, value in enumerate(Array_of_var, start=1):
            #         ws.cell(row=1, column=i).value = value
            # # =============================================================================
            # #         
            # # =============================================================================
                
            #     for i, value in enumerate(gl.tb_temp_arr , start=row_number):
            #         ws.cell(row=i, column=1).value = value
                    
            #     for i, value in enumerate(gl.ugb_temp_arr , start=row_number):
            #         ws.cell(row=i, column=2).value = value
                
            #     for i, value in enumerate(gl.lgb_temp_arr , start=row_number):
            #         ws.cell(row=i, column=3).value = value
                
            #     for i, value in enumerate(gl.tgb_temp_arr , start=row_number):
            #         ws.cell(row=i, column=4).value = value
            # # =============================================================================
            # #      e="xfr_oil_temp"
            #  # f="xfrm_stn_oil_temp"
            #  # g="gen_aircool_temp"
            #  # h="Temp_of_Oil_of_UAT"
            # # =============================================================================
            #     for i, value in enumerate(gl.xfr_oil_temp_arr , start=row_number):
            #         ws.cell(row=i, column=5).value = value
                    
            #     for i, value in enumerate(gl.xfrm_stn_oil_temp_arr , start=row_number):
            #         ws.cell(row=i, column=6).value = value
                    
            #     for i, value in enumerate(gl.gen_aircool_temp_arr , start=row_number):
            #         ws.cell(row=i, column=7).value = value
                    
            #     for i, value in enumerate(gl.Temp_of_Oil_of_UAT_arr , start=row_number):
            #         ws.cell(row=i, column=8).value = value
            # # =============================================================================
            # #          i="Ho_in_m"
            #  # j="Gate_OP_var"
            #  # k="fgen_Hz1"
            #  # l="U1_mps"
            # # =============================================================================
            #     for i, value in enumerate(gl.Ho_in_m_arr , start=row_number):
            #         ws.cell(row=i, column=9).value = value
                    
            #     for i, value in enumerate(gl.g1_arr , start=row_number):
            #         ws.cell(row=i, column=10).value = value
                    
            #     for i, value in enumerate(gl.fgen_Hz1_arr , start=row_number):
            #         ws.cell(row=i, column=11).value = value
                    
            #     for i, value in enumerate(gl.U1_mps_arr , start=row_number):
            #         ws.cell(row=i, column=12).value = value
            # # =============================================================================
            # #     
            #  # m="Vgen_RMS1"
            #  # n="Water_Discharge"
             
            #  # o="Pgen_MW1"
            #  # p="Qgen_MVAr1" 
            # # =============================================================================
            #     for i, value in enumerate(gl.Vgen_RMS1_arr , start=row_number):
            #         ws.cell(row=i, column=13).value = value
                    
            #     for i, value in enumerate(gl.water_diss_arr , start=row_number):
            #         ws.cell(row=i, column=14).value = value
                    
            #     for i, value in enumerate(gl.Pgen_MW1_arr , start=row_number):
            #         ws.cell(row=i, column=15).value = value
                    
            #     for i, value in enumerate(gl.Qgen_MVAr1_arr , start=row_number):
            #         ws.cell(row=i, column=16).value = value
                    
            # # =============================================================================
            # #          q="E_exc_kV1"
            #  # r="wrpm1"
             
            #  # s="I_exc_kA1"
            #  # t="Igen_RMS1"
            # # =============================================================================
                   
            #     for i, value in enumerate(gl.E_exc_kV1_arr , start=row_number):
            #         ws.cell(row=i, column=17).value = value
                    
            #     for i, value in enumerate(gl.wrpm1_arr , start=row_number):
            #         ws.cell(row=i, column=18).value = value
                    
            #     for i, value in enumerate(gl.I_exc_kA1_arr , start=row_number):
            #         ws.cell(row=i, column=19).value = value
                    
            #     for i, value in enumerate(gl.Igen_RMS1_arr , start=row_number):
            #         ws.cell(row=i, column=20).value = value
            # # =============================================================================
            # #          
            # # =============================================================================
                
                    
            
                
            #     wrkb.save(filename)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            #------------------------Menu edit Start-------------------------------------------------
            #---------------------------------------------------------------------------------------------
            
            edit = Menu(menubar, tearoff = 0)
            
            menubar.add_cascade(label ='Edit', menu = edit)
            
            edit.add_command(label ='Load        Ctrl+L', command = lambda a=1: Database_window_load(a))
            
            edit.add_command(label ='Save        Ctrl+S', command =lambda a=1:  savedata(a) )
            
            # edit.add_command(label ='Delete      Ctrl+D', command = None)
            
            #------------------------Menu Exercise END------------------------------------------------
            
            
            FIELD_FUNCTION_WINODW_IS_ON=False
            MALFUNCTION_WINODW_IS_ON=False
            
            
            def FeildFunction_2_Field():
                global FIELD_FUNCTION_WINODW_IS_ON
                if not FIELD_FUNCTION_WINODW_IS_ON:
                    FIELD_FUNCTION_WINODW_IS_ON=True
                    top_for_field=Toplevel(root)
                    top_for_field.title(glbg.FF_Heading_Name)
                    top_for_field.geometry('500x400')
                    top_for_field.resizable(0,0)
                    top_for_field.transient(root)
                    
                
                    field_function2(top_for_field)
                    def top_for_field_colse_func():
                        global FIELD_FUNCTION_WINODW_IS_ON
                        top_for_field.destroy()
                        FIELD_FUNCTION_WINODW_IS_ON=False
                        
                    top_for_field.protocol("WM_DELETE_WINDOW",top_for_field_colse_func )
            
            
            
            
            
            
            
            
            
            def FeildFunction_1_Field():
                global FIELD_FUNCTION_WINODW_IS_ON
                if not FIELD_FUNCTION_WINODW_IS_ON:
                    FIELD_FUNCTION_WINODW_IS_ON=True
                    top_for_field=Toplevel(root)
                    top_for_field.title(glbg.FF_Heading_Name)
                    top_for_field.geometry('500x400')
                    top_for_field.resizable(0,0)
                    top_for_field.transient(root)
                    
                
                    field_function1(top_for_field)
                    def top_for_field_colse_func():
                        global FIELD_FUNCTION_WINODW_IS_ON
                        top_for_field.destroy()
                        FIELD_FUNCTION_WINODW_IS_ON=False
                        
                    top_for_field.protocol("WM_DELETE_WINDOW",top_for_field_colse_func )
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            #------------------------MalFunction_ edit Start-------------------------------------------------
            #---------------------------------------------------------------------------------------------
            
            FeildFunction_ = Menu(menubar, tearoff = 0)
            
            menubar.add_cascade(label ='FeildFunction', menu = FeildFunction_)
            
            # FeildFunction_.add_command(label ='Elec Field', command = None)
            FeildFunction_.add_command(label ='Field1', command = FeildFunction_1_Field)
            # FeildFunction_.add_command(label ='Field2', command = FeildFunction_2_Field)
            #------------------------MalFunction_ edit END-------------------------------------------------
            
            
            
            
            #------------------------MalFunction_ edit Start-------------------------------------------------
            #---------------------------------------------------------------------------------------------
            
            def MALFUNCTION_CALLING_FUN_2():
                global MALFUNCTION_WINODW_IS_ON
                if not MALFUNCTION_WINODW_IS_ON:
                    MALFUNCTION_WINODW_IS_ON=True
                    top_for_mal=Toplevel(root)
                    top_for_mal.title(glbg.FF_Heading_Name)
                    top_for_mal.geometry('500x400')
                    top_for_mal.resizable(0,0)
                    top_for_mal.transient(root)
                    
                
                    MALFUNCTION_WINDOW_2( top_for_mal)
                    def top_for_mal_colse_func():
                        global MALFUNCTION_WINODW_IS_ON
                        top_for_mal.destroy()
                        MALFUNCTION_WINODW_IS_ON=False
                        
                    top_for_mal.protocol("WM_DELETE_WINDOW",top_for_mal_colse_func )
            
            
            
            
            def MALFUNCTION_CALLING_FUN():
                global MALFUNCTION_WINODW_IS_ON
                if not MALFUNCTION_WINODW_IS_ON:
                    MALFUNCTION_WINODW_IS_ON=True
                    top_for_mal=Toplevel(root)
                    top_for_mal.title(glbg.FF_Heading_Name)
                    top_for_mal.geometry('500x400')
                    top_for_mal.resizable(0,0)
                    top_for_mal.transient(root)
                    
                
                    MALFUNCTION_WINDOW( top_for_mal)
                    def top_for_mal_colse_func():
                        global MALFUNCTION_WINODW_IS_ON
                        top_for_mal.destroy()
                        MALFUNCTION_WINODW_IS_ON=False
                        
                    top_for_mal.protocol("WM_DELETE_WINDOW",top_for_mal_colse_func )
            
            
            
            
            
            
            
            
            
            def selection_A_or_M():
                sim_status=RADIO_VAR_AUTO_MAN.get()  
                print(sim_status)
                if sim_status==2:
                    glbg.AUTO_PLANT=True
                else:
                    glbg.AUTO_PLANT=False
                 
            
            
  
            MalFunction_ = Menu(menubar, tearoff = 0)
            
            menubar.add_cascade(label ='MalFunction', menu = MalFunction_)
            
            MalFunction_.add_command(label ='Instructors MalFunction 1', command = MALFUNCTION_CALLING_FUN)
            # MalFunction_.add_command(label ='Instructors MalFunction 2', command = MALFUNCTION_CALLING_FUN_2)
            
            
            #------------------------MalFunction_ edit END-------------------------------------------------
# =============================================================================
#             
# =============================================================================
         
            
            def selection():
                sim_status=RADIO_VAR_SIMULATION.get()  
               
                if sim_status==1:
                    gl.IS_SIMULATION_ON=True
                else:
                    gl.IS_SIMULATION_ON=False
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# =============================================================================
#             
# =============================================================================
            
            #------------------------Menu Logs  Start-------------------------------------------------
            #---------------------------------------------------------------------------------------------
            RADIO_VAR_SIMULATION = IntVar(value=1)  
            
            
            
            Logs_ = Menu(menubar, tearoff = 0)
            
            menubar.add_cascade(label ='Simulation', menu = Logs_)
            
            # Logs_.add_command(label ='Simulation Status', command = None)
            Logs_.add_radiobutton(label="Simulation ON" ,variable=RADIO_VAR_SIMULATION, value=1,  
                              command=selection )
            Logs_.add_radiobutton(label="Simulation OFF",variable=RADIO_VAR_SIMULATION, value=2,  
                              command=selection)

            
            
            
            #------------------------Menu Logs_  END-------------------------------------------------
            
            #------------------------Menu Views_  Start-------------------------------------------------
            #---------------------------------------------------------------------------------------------
            
            # Views_ = Menu(menubar, tearoff = 0)
            
            # menubar.add_cascade(label ='Views', menu = Views_)
            
            # Views_.add_checkbutton(label ='ToolBar', command = None, onvalue=1, offvalue=0)
            
            # Views_.add_checkbutton(label ='Status Bar', command = None, onvalue=1, offvalue=0)
            
            # Views_.add_checkbutton(label ='Instrument', command = None, onvalue=1, offvalue=0)
            
            #------------------------Menu Views_  END-------------------------------------------------
            
            #------------------------Menu windows_  Start-------------------------------------------------
            #---------------------------------------------------------------------------------------------
            
            ############################################################################################
            #####################------Menu windows_-------#############################################
            ############################################################################################
            
            #####################------Menu windows_Function-------#############################################
            
            
            def menu_windows_close_all_window(): #close all windows
                
                        toplevel_for_mimic.withdraw()
                        toplevel_for_Alarms.withdraw()
                        toplevel_for_Bar_Graph.withdraw()
                        toplevel_for_Trends.withdraw()
                        Clear_all_button_untick_func()
                        
                       
            
            
            
            def menu_windows_View_all_window():  # View All window
                        
                        four_windows.resize_Alarm_window_small(1)
                        four_windows.resize_Bar_Graph_window_small(1)
                        four_windows.resize_Mimic_window_small(1)
                        four_windows.resize_Trends_window_small(1)
                        
                        toplevel_for_mimic.deiconify()
                        toplevel_for_Alarms.deiconify()
                        toplevel_for_Bar_Graph.deiconify()
                        toplevel_for_Trends.deiconify()
                        Open_all_button_tick_func()
                        
                        
            
            
            
            def menu_windows_Tile():  # resize all 4 window to Tile
                    
                        four_windows.resize_Alarm_window_Tile()
                        
                        four_windows.resize_Bar_Graph_window_Tile()
                        
                        four_windows.resize_Trends_window_Tile()
                       
                        four_windows.resize_Mimic_window_Tile()
                
            
            
            def menu_window_Cascade(): # resize all 4 window to Cascade
            
                        four_windows.resize__Bar_Graph_window_for_cascade()
                        
                        four_windows.resize__Alarm_window_for_cascade()
                        
                        four_windows.resize__Trends_window_for_cascade()
                        
                        four_windows.resize__Mimic_window_for_cascade()
            
            
            
            
            
            
            windows_ = Menu(menubar, tearoff = 0)   
            
            menubar.add_cascade(label ='Windows', menu = windows_ )
            
            windows_.add_command(label ='Cascade', command = menu_window_Cascade)
            
            windows_.add_command(label ='Tile', command = menu_windows_Tile)
            
            windows_.add_separator()
            
            windows_.add_command(label ='View All', command = menu_windows_View_all_window)
            
            windows_.add_command(label ='Close All', command = menu_windows_close_all_window)
            
            # windows_.add_separator()
            
            # windows_.add_command(label ='Full Screen', command = None)
            
            # windows_.add_command(label ='Animated Interface', command = None)
            
            # windows_.add_separator()
            
            
            
            ##########################################################################################
            #------------------------Menu Logs_  END-------------------------------------------------
            ##########################################################################################
            
            
            
            
            ##################################################################################################
            ###########################--------TSPL Official Button------#######################################
            ######################################################################################################
            
            
            def open_TSPL_website(): #To open Tspl website
                
            
            
                webbrowser.open('https://www.trianglesimulation.com/')
            
            
            
            
            
            
            # =============================================================================
            # =============================================================================
            # #  ABout Tspl Window
            # =============================================================================
            # =============================================================================
            image = Image.open("Images/logo.png")
            
            # Resize the image using resize() method
            resize_image = image.resize((75, 75))
            
            img_for_About_tspl = ImageTk.PhotoImage(resize_image)
            
            top_for_About_tspl=Toplevel(root)
            top_for_About_tspl.attributes('-topmost', 'true')
            
            About_Tspl(img_for_About_tspl,top_for_About_tspl)
            
            top_for_About_tspl.withdraw()
            def tpl_About_tspl_withdraw():
                top_for_About_tspl.withdraw()
            
            
            top_for_About_tspl.protocol("WM_DELETE_WINDOW",tpl_About_tspl_withdraw )
                
             
            def to_deiconify_about_tspl():
                top_for_About_tspl.deiconify()
            
            
            
            
            
            
            
            
            
            
            
            ######################################################################################################
            #------------------------Menu help_  Start-------------------------------------------------
            ######################################################################################################
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            help_ = Menu(menubar, tearoff = 0)
            
            menubar.add_cascade(label ='Help', menu = help_)
            
            help_.add_command(label ='Contents', command = None)
            
            help_.add_separator()
            
            help_.add_command(label ='About Training Simulator', command = to_deiconify_about_tspl)
            
            help_.add_command(label ='TSPL Official', command = open_TSPL_website)
            
            #------------------------Menu help_  END-------------------------------------------------
            
            
            #------------------------------- Display Menu-----------------------------------------------------
            
            root.config(menu = menubar)
            ##123456
            ################################################################################################################
            #------------------------------- END Menu-----------------------------------------------------
            ##################################################################################################################
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            ########################################################################################
            #----------------------------Status_Bar Start--------------------------------------------
            ##############################################################################################
            
            
            
            
            
            
            
            
            
            
            #=-----------------------------------------------------------------------------------------
            
            
            ##%%-------------------------------------------Status Bar-----------------------------------
            ############################################################################################
            
            Status_Bar=Frame4
            
            # Status_Bar.configure(background='BLUE')
            
            # # Status_Bar.pack(fill = BOTH, expand=True)
            
            # mid_pos_for_text=width_of_monitor//15
            
            # half_scrren=width_of_monitor/2
            
            
            
            
            
            name_of_mimic=Label(Status_Bar,text='   HYDROPOWER PLANT SIMULATION  :-'+str(glbg.Heading_Name),anchor='w',relief="sunken",width=5,height=2,borderwidth=5)
            
            name_of_mimic.place(relx=0,rely=0,relwidth=.3)
            
            model_no_of_mimic=Label(Status_Bar,text='   TSPL PVT. LTD.',anchor='w',width=1000,height=2, relief="sunken",borderwidth=5)
            
            model_no_of_mimic.place(relx=0.3,rely=0,relwidth=.15)
            
            state_of_mimic=Label(Status_Bar,text='Freeze',anchor='w',width=1000,height=2, relief="sunken",borderwidth=5)
            
            state_of_mimic.place(relx=0.45,rely=0,relwidth=.15)
            
            time2=''
            
            Date_and_Time=Label(Status_Bar,textvariable=time2,anchor='w',width=1000,height=2, relief="sunken",borderwidth=5)
            
            Date_and_Time.place(relx=0.60,rely=0,relwidth=.15)
            
            _time=Label(Status_Bar,text='   0:0:0',anchor='w',width=1000,height=2, relief="sunken",borderwidth=5)
            
            _time.place(relx=0.75,rely=0,relwidth=.15)
            
            
            x_y_cord=Label(Status_Bar,text='0:0',anchor='w',width=1000,height=2, relief="sunken",borderwidth=5)
            
            x_y_cord.place(relx=0.9,rely=0,relwidth=.1)
            
            # #################################################################################
            # ####################Live Time & Date ###################################################
            # ################################################################################
            
            time_date=''
            
            # def change_MIMIC_name_on_status_bar():
                # global name_of_mimic
                # name_of_mimic.configure(text='   HYDROPOWER PLANT SIMULATION  :- '+str( glbg.Heading_Name))
                # root.after(100,change_MIMIC_name_on_status_bar)
            
            
            # change_MIMIC_name_on_status_bar()
            
            def changeLabel(): 
                
                        global time_date
                        
                        time_date = time.strftime('   %Y-%m-%d // %H:%M:%S')
                        time_only = time.strftime('   %H:%M:%S')
                        
                        Date_and_Time.configure(text=time_date)
                        label_heading_time.configure(text=time_only)
                        write_alarm_in_text_file()
                        global name_of_mimic
                        name_of_mimic.configure(text='   HYDROPOWER PLANT SIMULATION  :- '+str( glbg.Heading_Name))
                        # glbg.global_root_var.update()
                        label_heading.configure(text=glbg.Heading_Name)
                        root.after(10, changeLabel)
                
                
            changeLabel()
            
            hours=0
            minutes=0
            seconds=0
            
            def Count_time(): 
                        global hours,minutes,seconds,countdown_flage
                        # print(countdown_flage)
                        
                        if countdown_flage:
                            countdown=f'{hours:02d}:{minutes:02d}:{seconds:02d}'
                            _time.configure(text=countdown)
                            # time.sleep(1)
                            seconds += 1
                            if seconds == 60:
                                seconds = 0
                                minutes += 1
                            if minutes == 60:
                                minutes = 0
                                hours += 1
                        if glbg.countdown_flage_1:
                            countdown_flage=True
                        else:
                            countdown_flage=False
                            
                        root.after(1000, Count_time)
                
                
            
            
            #----------------------------Status Bar End--------------------------------------------
            ##123456
            
            
            ##123456
            ########################################################################################
            #----------------------------Tool_Bar Start--------------------------------------------
            ###################################################################################
            
            #################################################################################
            ##############-----------Tool_Bar button function------------#####################
            ##################################################################################
            
            
            
            
            
            '''
                        #click event 
                        0=Main Root Window
                        1=Mimic Toplevel Window
                        2=Trends Toplevel Window
                        3=barGraph Toplevel Window
                        4=Alarms Toplevel Window
                        click_event=0
                        
            
            
                        toplevel_for_mimic_click=False
                        toplevel_for_Trends_click=False
                        toplevel_for_Bar_Graph_click=False
                        toplevel_for_Alarms_click=False
                        root_window_click=False
            
            
            
            '''
            
            
            
            key_allow=False #to allow or not allow to move mimic by a,s,w,d.
            
            def check_all_four_window_are_close():
                 global fourwindow_array_for_root,flag_as_all_four_window_are_close
                 var_001=fourwindow_array_for_root
                 if not var_001[0]:
                     if not var_001[1]:
                         if not var_001[2]:
                             if not var_001[3]:
                                 flag_as_all_four_window_are_close=True
                
                
                
                
                
                
            
            #mainframe02=Interlock_(root)
            #mainframe01=mainframe(root)
            
            def open_mimic_by_button():
                
                        # check_all_four_window_are_close()
                        window='mimic'
                        
                        if toplevel_for_mimic_click:
                            
                            four_windows.on_replace_mimic_window(window)
                        
                        
                        
                        if toplevel_for_Bar_Graph_click:
                            
                            four_windows.on_replace_Bar_Graph_window(window)
                            
                            
                            
                        if toplevel_for_Alarms_click:
                             
                             four_windows.on_replace_Alarms_window(window)
                             
                             
                             
                        if toplevel_for_Trends_click:
                             pass
                             
                             four_windows.on_replace_Trends_window(window)
                        
                        
                       
                        if flag_as_all_four_window_are_close:
                            pass
                          
                           # mainframe01.open_mimic_by_button()
                    
            
            
            
            def open_Bar_graph_by_button():
                
                        # check_all_four_window_are_close()
                        
                        window='Bar_graph'
                        
                        if toplevel_for_mimic_click:
                            
                            four_windows.on_replace_mimic_window(window)
                        
                        
                        
                        if toplevel_for_Bar_Graph_click:
                            
                            four_windows.on_replace_Bar_Graph_window(window)
                            
                            
                            
                        if toplevel_for_Alarms_click:
                             
                             four_windows.on_replace_Alarms_window(window)
                             
                             
                             
                        if toplevel_for_Trends_click:
                            
                             
                             four_windows.on_replace_Trends_window(window)
                        
                        
                        if flag_as_all_four_window_are_close:
                            pass
                            
                           # mainframe01.open_Bar_graph_by_button()
                        
                        
            
            
            
            def open_Alarms_by_button():
                
                        # check_all_four_window_are_close()
                        window='Alarms'
                        
                        
                        if toplevel_for_mimic_click:
                            
                            four_windows.on_replace_mimic_window(window)
                        
                        
                        
                        if toplevel_for_Bar_Graph_click:
                            
                            four_windows.on_replace_Bar_Graph_window(window)
                            
                            
                            
                        if toplevel_for_Alarms_click:
                             
                             four_windows.on_replace_Alarms_window(window)
                             
                             
                             
                        if toplevel_for_Trends_click:
                             
                             
                             four_windows.on_replace_Trends_window(window)
                        
                        
                        if flag_as_all_four_window_are_close:
                            pass
                           
                               # mainframe01.open_Alarms_by_button()
                        
                    
            
            
            
            def open_Line_graph_by_button():
                
                        
                        # check_all_four_window_are_close()
                        
                        window='Trends'
                        
                        if toplevel_for_mimic_click:
                            
                            four_windows.on_replace_mimic_window(window)
                        
                        
                        
                        if toplevel_for_Bar_Graph_click:
                            
                            four_windows.on_replace_Bar_Graph_window(window)
                            
                            
                            
                        if toplevel_for_Alarms_click:
                             
                             four_windows.on_replace_Alarms_window(window)
                             
                             
                             
                        if toplevel_for_Trends_click:
                             
                             
                             four_windows.on_replace_Trends_window(window)
                        
                        if flag_as_all_four_window_are_close:
                            pass
                            
                                  #  mainframe01.open_Line_graph_by_button()
                        
                        
                        
                 
                   
               
            
            
            
            
            
            
            
            
            
            
            
            
            
            Tool_Bar_canvas=Canvas(Frame3,relief='sunken' ,width=width_of_monitor,height=65, command = None) #creating canvas for Toolbar
            
            Tool_Bar_canvas.configure(background='grey')  #setting background color to grey
            root.configure(background='#5A5A5A')
            Tool_Bar_canvas.pack(side = BOTTOM, fill = X) #placing canvas
            
            ##123456
            #----------------------------Tool Bar Button Start--------------------------------------------
            
            ##123456
            #####################################################################
            #-------------Tocanvas for logo of TSPL  winodw------------------------
            #---------------connected to file _3d_Logo_of_TSPL.py--------------------
            #####################################################################
            
            # canvas_for_TSPL_logo=Canvas(Tool_Bar_canvas,width=0,height=0)
            
            # canvas_for_TSPL_logo.place(x=0,y=0)
            
            
            place_logo_of_TSPL(Tool_Bar_canvas)
            
            def REFRESH_PAGES():
                try:
                    
                    main_page_obj.BAR_GRAPH_BUTTON_FUN.Bar_Graph_Indv_1.redraw(1)
                    main_page_obj.BAR_GRAPH_BUTTON_FUN.Bar_Graph_Indv_2.redraw(1)
                    main_page_obj.BAR_GRAPH_BUTTON_FUN.redraw(1)
                    main_page_obj.TREND_BUTTON_FUN.Trends_Indv_1.redraw(1)
                    main_page_obj.TREND_BUTTON_FUN.Trends_Indv_2.redraw(1)
                    main_page_obj.TREND_BUTTON_FUN.redraw(1)
                    main_page_obj.MIMIC_BUTTON_FUN.MIMIC_2_INDV_OBJ.redraw(1)
                    main_page_obj.MIMIC_BUTTON_FUN.MIMIC_INDV_OBJ.redraw(1)
                    main_page_obj.MIMIC_BUTTON_FUN.redraw(1)
                except:
                    pass
                
                
                
                
                
            def __Open_BAR_GRAPH():
                 global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
                 print(toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click)
                   
                # print(root_window_click)
                 # glbg.global_root_var.update()
                 if toplevel_for_Alarms_click:
                     four_windows.on_replace_Alarms_window("Bar_graph")
                 
                 if toplevel_for_Trends_click:
                     four_windows.on_replace_Trends_window("Bar_graph")
                 
                 if toplevel_for_Bar_Graph_click :
                     four_windows.on_replace_Bar_Graph_window("Bar_graph")
                 
                 if toplevel_for_mimic_click :
                     four_windows.on_replace_mimic_window("Bar_graph")
                 # glbg.global_root_var.update()
                 
                 
                 # glbg.Heading_Name='BAR GRAPH MENU'
                 # REFRESH_PAGES()
                 # main_page_obj.button_11_fun()
                 # main_page_obj.BAR_Indv_OBJ.redraw(1)
             
             
            def __Open_Trends():
                 global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
                 print(toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click)
                   
                # print(root_window_click)
                 # glbg.global_root_var.update()
                 if toplevel_for_Alarms_click:
                     four_windows.on_replace_Alarms_window("Trends")
                 
                 if toplevel_for_Trends_click:
                     four_windows.on_replace_Trends_window("Trends")
                 
                 if toplevel_for_Bar_Graph_click :
                     four_windows.on_replace_Bar_Graph_window("Trends")
                 
                 if toplevel_for_mimic_click :
                     four_windows.on_replace_mimic_window("Trends")
                 # glbg.global_root_var.update()
                 
                 
                 # glbg.Heading_Name='TRENDS MENU'
                 # REFRESH_PAGES()
                 # main_page_obj.button_9_fun()
                 # main_page_obj.Trends_Indv_OBJ.redraw(1)
             
             
            def __Open_mimic():
                 global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
                  # print(root_window_click)
                 print(toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click)
                    
                
                 # glbg.global_root_var.update()
                 if toplevel_for_Alarms_click:
                     four_windows.on_replace_Alarms_window("mimic")
                 
                 if toplevel_for_Trends_click:
                     four_windows.on_replace_Trends_window("mimic")
                 
                 if toplevel_for_Bar_Graph_click :
                     four_windows.on_replace_Bar_Graph_window("mimic")
                 
                 if toplevel_for_mimic_click :
                     four_windows.on_replace_mimic_window("mimic")
                 # glbg.global_root_var.update()
                      
                  
                 
                  
                  
                 # four_windows.on_replace_mimic_window("Trends") 
                 # # print("ekadun hotay")
                 # if root_window_click:
                 #     glbg.Heading_Name='MIMIC MENU'
                 #     # REFRESH_PAGES()
                     
                 #     main_page_obj.button_4_fun()
                     
                 #     main_page_obj.MIMIC_BUTTON_FUN.redraw(1)
                 # # if toplevel_for_mimic_click:
                 #     open_mimic_by_button()
             
            def __Open_ALARM():
                 global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
                 print(toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click)
                   
                 # glbg.global_root_var.update()
                 if toplevel_for_Alarms_click:
                     four_windows.on_replace_Alarms_window("Alarms")
                 
                 if toplevel_for_Trends_click:
                     four_windows.on_replace_Trends_window("Alarms")
                 
                 if toplevel_for_Bar_Graph_click :
                     four_windows.on_replace_Bar_Graph_window("Alarms")
                 
                 if toplevel_for_mimic_click :
                     four_windows.on_replace_mimic_window("Alarms")
                 # glbg.global_root_var.update()
                 
                 
                 # glbg.Heading_Name='ALARM MENU'
                 # main_page_obj.button_10_fun()
                 # REFRESH_PAGES()
                 # main_page_obj.ALARM_INDV_OBJ.redraw(1)
# =============================================================================
#             
# =============================================================================
           
            def Take_screen_shot():
                
                x, y = root.winfo_rootx() + Frame2.winfo_x(), root.winfo_rooty() + Frame2.winfo_y()
                width, height = Frame2.winfo_width(), Frame2.winfo_height()

                # capture a screenshot of the entire screen
                screenshot = ImageGrab.grab()

                # crop the screenshot to the region of interest
                screenshot = screenshot.crop((x, y, x + width, y + height))

                # save the screenshot as an image file
                file_path = filedialog.asksaveasfilename(defaultextension=".png")

                # save the screenshot as an image file
                if file_path:
                    screenshot.save(file_path)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# =============================================================================
#             
# =============================================================================
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            #####################################################################
            #-------------_3d_Logo_of_TSPL on  winodw End------------------------
            #####################################################################
            ##123456
            
            ##123456
            Buttton_for_Mimics=Button(Tool_Bar_canvas,text='Mimics', command = __Open_mimic,borderwidth=5) #creating Button for Opening Mimic
            
            Buttton_for_Mimics.place(relx=0.005,rely=0.16,relwidth=0.05,relheight=0.7)
            
            Buttton_for_Trends=Button(Tool_Bar_canvas,text='Trends', command = __Open_Trends,borderwidth=5) #creating Button for Opening line graph
            
            Buttton_for_Trends.place(relx=0.055,rely=0.16,relwidth=0.05,relheight=0.7)
            
            Buttton_for_Bar_Graph=Button(Tool_Bar_canvas,text='Bar Graph', command = __Open_BAR_GRAPH,borderwidth=5) #creating Button for Opening Bar Graph
            
            Buttton_for_Bar_Graph.place(relx=0.105,rely=0.16,relwidth=0.05,relheight=0.7)
            
            Buttton_for_Alarms=Button(Tool_Bar_canvas,text='Alarms', command = __Open_ALARM,borderwidth=5)  #creating Button for Opening Alarm
            
            Buttton_for_Alarms.place(relx=0.155,rely=0.16,relwidth=0.05,relheight=0.7)
            
            Buttton_for_Print=Button(Tool_Bar_canvas,text='Print', command = Take_screen_shot,borderwidth=5)
            
            Buttton_for_Print.place(relx=0.205,rely=0.16,relwidth=0.05,relheight=0.7)
            
            # Buttton_for_Link=Button(Tool_Bar_canvas,text='Link', command = None,borderwidth=5)
            
            # Buttton_for_Link.place(relx=0.255,rely=0.16,relwidth=0.05,relheight=0.7)
            
            # Buttton_for_Ack_Sum=Button(Tool_Bar_canvas,text='Ack Sum', command = None,borderwidth=5)
            
            # Buttton_for_Ack_Sum.place(relx=0.305,rely=0.16,relwidth=0.05,relheight=0.7)
            
            #----------------------------Tool Bar Arrow Button Start--------------------------------------------
            
            
            
            #----------------------------Tool Bar Arrow Button End--------------------------------------------
            ##123456
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            MIMIC_is_OPEN_OR_NOT_VAR=0
            
            
            
                 
            ##123456
            '''
                 toplevel_for_mimic=Toplevel()
                 toplevel_for_Trends=Toplevel()
                 toplevel_for_Bar_Graph=Toplevel()
                 toplevel_for_Alarms=Toplevel()
                 
                 #fourwindow_array_for_root=[0,0,0,0]
            '''
            
            
            
            def mimic_checkbox_function():
                        global fourwindow_array_for_root
                
                        if Mimic_checkbox_var.get()==1:
                              fourwindow_array_for_root[0]=1  
                              four_windows.resize_Mimic_window_small(1)
                              toplevel_for_mimic.deiconify()
                                
                           
                        if Mimic_checkbox_var.get()==0:
                             fourwindow_array_for_root[0]=0
                             toplevel_for_mimic.withdraw()
                              
                               #four_windows.on_close_Mimic_window()
                            
            
            
            
            def Bar_Graph_checkbox_function():
                        global fourwindow_array_for_root
                        if Bar_Graph_checkbox_var.get()==1:
                            fourwindow_array_for_root[1]=1    
                            four_windows.resize_Bar_Graph_window_small(1)
                            toplevel_for_Bar_Graph.deiconify()
                            
                        if Bar_Graph_checkbox_var.get()==0:
                               fourwindow_array_for_root[1]=0 
                               toplevel_for_Bar_Graph.withdraw()
                            
            
            
            
            def Alarms_checkbox_function():
                        global fourwindow_array_for_root
                        if Alarms_checkbox_var.get()==1:
                               fourwindow_array_for_root[2]=1 
                               four_windows.resize_Alarm_window_small(1)
                               toplevel_for_Alarms.deiconify()
                            
                        if Alarms_checkbox_var.get()==0:
                                #print(fourwindow_array_for_root)
                                fourwindow_array_for_root[2]=0
                                toplevel_for_Alarms.withdraw()
                    
            
            
            
            def Trends_checkbox_function():
                        global fourwindow_array_for_root
                        if Trends_checkbox_var.get()==1:
                            fourwindow_array_for_root[3]=0
                            four_windows.resize_Trends_window_small(1)
                            toplevel_for_Trends.deiconify()
                            
                        if Trends_checkbox_var.get()==0:
                            fourwindow_array_for_root[3]=1
                            toplevel_for_Trends.withdraw()
                   
               
            
            
            
            class checkbox_of_windows:
                def __init__(self):
                    pass
                
            
                
                def untick_of_mimic_checkbox(self):
                    global Mimic_checkbox_var
                    fourwindow_array_for_root[0]=0
                    Mimic_checkbox_var.set(value=0)        
                
            
                
                def untick_of_Bar_Graph_checkbox(self):
                    global Bar_Graph_checkbox_var
                    fourwindow_array_for_root[1]=0
                    Bar_Graph_checkbox_var.set(value=0)    
                
              
                
                def untick_of_Alarms_checkbox(self):
                    global Alarms_checkbox_var
                    fourwindow_array_for_root[2]=0
                    Alarms_checkbox_var.set(value=0)    
                    
               
                
                def untick_of_Trends_checkbox(self):
                    global Trends_checkbox_var
                    fourwindow_array_for_root[3]=0
                    Trends_checkbox_var.set(value=0) 
                
                def tick_of_mimic_checkbox(self):
                    global Mimic_checkbox_var
                    fourwindow_array_for_root[0]=1
                    Mimic_checkbox_var.set(value=1)        
                
            
                
                def tick_of_Bar_Graph_checkbox(self):
                    global Bar_Graph_checkbox_var
                    fourwindow_array_for_root[1]=1
                    Bar_Graph_checkbox_var.set(value=1)    
                
              
                
                def tick_of_Alarms_checkbox(self):
                    global Alarms_checkbox_var
                    fourwindow_array_for_root[2]=1
                    Alarms_checkbox_var.set(value=1)    
                    
               
                
                def tick_of_Trends_checkbox(self):
                    global Trends_checkbox_var
                    fourwindow_array_for_root[3]=1
                    Trends_checkbox_var.set(value=1) 
            
            
            ##123456    
            ##123456
            ##123456
            Mimic_checkbox_var = IntVar(value=0)
            
            Mimic_checkbox_=Mimic_checkbox=Checkbutton(Tool_Bar_canvas, text="Mimic", variable=Mimic_checkbox_var,background='grey',command=mimic_checkbox_function).place(relx=0.372,rely=.10)
            
            
            
            Bar_Graph_checkbox_var = IntVar(value=0)
            
            Bar_Graph_checkbox_=Checkbutton(Tool_Bar_canvas, text="Bar Graph", variable=Bar_Graph_checkbox_var,background='grey',command=Bar_Graph_checkbox_function).place(relx=0.431,rely=.10)
            
            
            
            
            
            Alarms_checkbox_var = IntVar(value=0)
            
            Alarms_checkbox_=Checkbutton(Tool_Bar_canvas, text="Alarms", variable=Alarms_checkbox_var,background='grey',command=Alarms_checkbox_function).place(relx=0.372,rely=.50)
            
            
            
            
            Trends_checkbox_var = IntVar(value=0)
            
            Trends_checkbox_=Checkbutton(Tool_Bar_canvas, text="Trends", variable=Trends_checkbox_var,background='grey',command=Trends_checkbox_function).place(relx=0.431,rely=.50)
            
            
            
            
            
            #opening all four windows As Deafualt
            
            # 
            
                
            ##123456
            
            
            
            
            
            # image1 = Image.open("images/up-arrow.jpg")
            
            # image2 = Image.open("images/down-arrow.png")
            
            # image3 = Image.open("images/left-arrow.png")
            
            # image4 = Image.open("images/right-arrow.png")
            
            # image5 = Image.open("images/back.png")
            
            # # Resize the image using resize() method
            
            # resize_image1 = image1.resize((35, 25))
            
            # resize_image2 = image2.resize((35, 25))
            
            # resize_image3 = image3.resize((35, 25))
            
            # resize_image4 = image4.resize((35, 25))
            
            # resize_image5 = image5.resize((50, 50))
            
            # img1_up = ImageTk.PhotoImage(resize_image1)
            
            # img2_down = ImageTk.PhotoImage(resize_image2)
            
            # img3_left = ImageTk.PhotoImage(resize_image3)
            
            # img4_right = ImageTk.PhotoImage(resize_image4)
            
            # back_image = ImageTk.PhotoImage(resize_image5)
            
            # mid=width_of_monitor//2
            
            
            
            
            
            
            # def Next_MIMIC():
            #             global CURRENT_MIMIC
                        
            #             CURRENT_MIMIC +=1
                        
            #             if CURRENT_MIMIC==0:
                            
            #                     CURRENT_MIMIC=4
                                
            #             if CURRENT_MIMIC==5:
                            
            #                     CURRENT_MIMIC=1
                        
            #             open_mimc_by_CURRENT_MIMIC()
                
            
            # def Prev_MIMIC(): 
                
            #             global CURRENT_MIMIC
                        
            #             CURRENT_MIMIC -=1
                        
            #             if CURRENT_MIMIC==0:
                            
            #                     CURRENT_MIMIC=4
                                
            #             if CURRENT_MIMIC==5:
                            
            #                     CURRENT_MIMIC=1
                                
            #             open_mimc_by_CURRENT_MIMIC()
                            
                        
                        
            
            # def open_mimc_by_CURRENT_MIMIC():
                
            #             global CURRENT_MIMIC
                        
            #             name_of_mimic.configure(text='   HydroPower Plant Simulation  :-'+str(CURRENT_MIMIC))
                        
            #           #  print(CURRENT_MIMIC)
                        
            #            # mimc_by_CURRENT_MIMIC()
            #             '''
                        
            #             if CURRENT_MIMIC==1:
                            
            #                     mainframe01.open_mimic001_by_button()
                            
            #             if CURRENT_MIMIC==2:
                            
            #                     mainframe01.open_mimic002_by_button()
                            
            #             if CURRENT_MIMIC==3:
                            
            #                     mainframe01.open_mimic003_by_button()
                            
            #             if CURRENT_MIMIC==4:
                            
            #                     mainframe01.open_mimic004_by_button()
                                
            #             '''
                        
            # =============================================================================
            #             HOME BUTTON AND BACK BUTTON
            #             
            # =============================================================================
                        
                            
            def pass_fun(e):
                pass
            glbg.Back_button[0]=pass_fun
            
            def Home_mimic():
                global main_page_obj
                
                
                
                try:
                    main_page_obj.create_frames()
                except:
                    pass
                
                # try:
                #     temp_var=glbg.var_to_track_notebook_page
                   
                   
                #     glbg.Back_button[temp_var](1)
                        
                    
                    
                   
                # except:
                #     pass
                
                
                
                
                # try:
                   
                #     glbg.Heading_Name='MAIN MENU'
                    
                   
                    
                #     main_page_obj.Notebook_main_page.select(0)
                #     glbg.var_to_track_notebook_page=0
                    
                #     # self.Notebook_main_page.select(2)
                # except:
                #     pass
                    
                
            # def back_mimic():
                
                
                # try:
                #     temp_var=glbg.var_to_track_notebook_page
                #     # print('value of temp_var is ',temp_var)
                   
                   
                #     glbg.Back_button[temp_var](1)
                        
                    
                    
                   
                # except:
                #     pass
                    
               
            def back_mimic_event():
                temp_var=glbg.var_to_track_notebook_page
                # print(temp_var,glbg.MIMIC_BTN_INTR_1)
                # print("-----------------------")
                if temp_var==1:
                    main_page_obj.UP_BUTTON_FUN.redraw(1)
                    
                if temp_var==16:
                    x=glbg.MIMIC_BTN_INTR_1
                    if x==0:    
                        main_page_obj.BAR_GRAPH_BUTTON_FUN.redraw(1)
                    if x==1:
                      
                        main_page_obj.BAR_GRAPH_BUTTON_FUN.Bar_Graph_Indv_1.redraw(1)
                    if  x==2:
                     
                        main_page_obj.BAR_GRAPH_BUTTON_FUN.Bar_Graph_Indv_2.redraw(1)
                    
                
                
                if temp_var==15:
                    x=glbg.MIMIC_BTN_INTR_1
                    if x==0:    
                        main_page_obj.TREND_BUTTON_FUN.redraw(1)
                    if x==1:
                      
                        main_page_obj.TREND_BUTTON_FUN.Trends_Indv_1.redraw(1)
                    if  x==2:
                     
                      main_page_obj.TREND_BUTTON_FUN.Trends_Indv_2.redraw(1)
                    
                
                
                if temp_var==4:
                   main_page_obj.MIMIC_INDV_OBJ.create_frames()
                if temp_var==14:
                    x=glbg.MIMIC_BTN_INTR_1
                    if x==0:    
                        main_page_obj.MIMIC_BUTTON_FUN.redraw(1)
                    if x==1:
                      
                        main_page_obj.MIMIC_BUTTON_FUN.CALL_MIMIC_1.redraw(1)
                    if  x==2:
                     
                        main_page_obj.MIMIC_BUTTON_FUN.CALL_MIMIC_2_2.redraw(1)
                   
                
                if temp_var==13:
                    main_page_obj.MIMIC_2_INDV_OBJ.redraw(1)
                   
                if temp_var==9:
                    main_page_obj.Trends_Indv_OBJ.redraw(1)
                    
                if temp_var==11:
                    main_page_obj.BAR_Indv_OBJ.redraw(1)
                # try:
                   
                #     # print('value of temp_var is ',temp_var)
                   
                #     # print(glbg.Back_button[temp_var])
                #     glbg.Back_button[temp_var](1)
                        
                    
                    
                   
                # except:
                #     pass
                    
            def back_mimic_btn_event(e):
              
                  temp_var=glbg.var_to_track_notebook_page
                  print(temp_var,glbg.MIMIC_BTN_INTR_1)
                  print("-----------------------")
                  if temp_var==16:
                      x=glbg.MIMIC_BTN_INTR_1
                      if x==0:    
                          main_page_obj.BAR_GRAPH_BUTTON_FUN.redraw(1)
                      if x==1:
                        
                          main_page_obj.BAR_GRAPH_BUTTON_FUN.Bar_Graph_Indv_1.redraw(1)
                      if  x==2:
                       
                          main_page_obj.BAR_GRAPH_BUTTON_FUN.Bar_Graph_Indv_2.redraw(1)
                      
                  
                  
                  if temp_var==15:
                      x=glbg.MIMIC_BTN_INTR_1
                      if x==0:    
                          main_page_obj.TREND_BUTTON_FUN.redraw(1)
                      if x==1:
                        
                          main_page_obj.TREND_BUTTON_FUN.Trends_Indv_1.redraw(1)
                      if  x==2:
                       
                        main_page_obj.TREND_BUTTON_FUN.Trends_Indv_2.redraw(1)
                      
                  
                  
                  if temp_var==4:
                     main_page_obj.MIMIC_INDV_OBJ.redraw(1)
                  if temp_var==14:
                      x=glbg.MIMIC_BTN_INTR_1
                      if x==0:    
                          main_page_obj.MIMIC_BUTTON_FUN.redraw(1)
                      if x==1:
                        
                          main_page_obj.MIMIC_BUTTON_FUN.CALL_MIMIC_1.redraw(1)
                      if  x==2:
                       
                          main_page_obj.MIMIC_BUTTON_FUN.CALL_MIMIC_2_2.redraw(1)
                     
                  
                  if temp_var==13:
                      main_page_obj.MIMIC_2_INDV_OBJ.redraw(1)
                     
                  if temp_var==9:
                      main_page_obj.Trends_Indv_OBJ.redraw(1)
                      
                  if temp_var==11:
                      main_page_obj.BAR_Indv_OBJ.redraw(1)
                  # try:
                     
                  #     # print('value of temp_var is ',temp_var)
                           
               
                
               
            root.bind('<BackSpace>',back_mimic_btn_event) 
            
            # =============================================================================
            # =============================================================================
            # # 
            # =============================================================================
            # =============================================================================
            
            def Page_Up_button_Four_win(e):
                global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
                
                # temp_var=glbg.var_to_track_notebook_page
                if toplevel_for_Alarms_click:
                    
                
                    four_windows.frame_for_alarm.Down(1)
                    
                if toplevel_for_Trends_click:
                    four_windows.frame_for_trends.Down(1)
                    
                if toplevel_for_Bar_Graph_click :
                      
                  
                      four_windows.frame_for_Bar_graph.Down(1)
                      
                if toplevel_for_mimic_click:
                    
                      four_windows.frame_for_Mimic.Down(1)
                
                
                
                
                
             
                
            def Page_Down_Button_Four_win(e):
                global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
              
                # temp_var=glbg.var_to_track_notebook_page
                if toplevel_for_Alarms_click:
                    
                
                    four_windows.frame_for_alarm.UP(1)
                    
                if toplevel_for_Trends_click:
                    four_windows.frame_for_trends.UP(1)
                    
                if toplevel_for_Bar_Graph_click :
                      
                  
                      four_windows.frame_for_Bar_graph.UP(1)
                      
                if toplevel_for_mimic_click:
                    
                      four_windows.frame_for_Mimic.UP(1)
                
                
                
               
            
            
            
            
            
            def Page_Up_button(e):
                temp_var=glbg.var_to_track_notebook_page
                
                
                
                
                
                if temp_var==5:
                    main_page_obj.Interlock_obj.up(e)
                if temp_var==10:
                    main_page_obj.ALARM_INDV_OBJ.UP(e)
                
            def Page_Down_Button(e):
                temp_var=glbg.var_to_track_notebook_page
                
                
                
                
                if temp_var==5:
                    main_page_obj.Interlock_obj.down(e)
                if temp_var==10:
                    main_page_obj.ALARM_INDV_OBJ.DOWN(e)
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            def on_mouse_scroll(event):
                if event.delta>0:
                    Page_Up_button_Four_win(1)
                if event.delta<0:
                    Page_Down_Button_Four_win(1)
                
            
            
            root.bind('<Prior>',Page_Up_button) #page Up
            root.bind('<Next>',Page_Down_Button) #page Down
            
           
            toplevel_for_Alarms.bind('<MouseWheel>',on_mouse_scroll) #page Up
            toplevel_for_Bar_Graph.bind('<MouseWheel>',on_mouse_scroll) #page Up
            toplevel_for_Trends.bind('<MouseWheel>',on_mouse_scroll) #page Up
            toplevel_for_mimic.bind('<MouseWheel>',on_mouse_scroll) #page Up
            
            
            
            toplevel_for_Alarms.bind('<Prior>',Page_Up_button_Four_win) #page Up
            toplevel_for_Bar_Graph.bind('<Prior>',Page_Up_button_Four_win) #page Up
            toplevel_for_Trends.bind('<Prior>',Page_Up_button_Four_win) #page Up
            toplevel_for_mimic.bind('<Prior>',Page_Up_button_Four_win) #page Up
            
            toplevel_for_Alarms.bind('<Next>',Page_Down_Button_Four_win) #page Up
            toplevel_for_Bar_Graph.bind('<Next>',Page_Down_Button_Four_win) #page Up
            toplevel_for_Trends.bind('<Next>',Page_Down_Button_Four_win) #page Up
            toplevel_for_mimic.bind('<Next>',Page_Down_Button_Four_win) #page Up
            
            # =============================================================================
            # =============================================================================
            # # 
            # =============================================================================
            # =============================================================================
            
            # left_button = Button(Tool_Bar_canvas, image = img3_left, bd = 0,background='grey',command = Prev_MIMIC)
            
            # left_button.place(relx=0.568,rely=0.5)
            
            # down_button = Button(Tool_Bar_canvas, image = img2_down, bd = 0,background='grey',command=Prev_MIMIC )
            
            # down_button.place(relx=0.598,rely=0.5)
            
            
            # up_button = Button(Tool_Bar_canvas, image = img1_up, bd = 0,background='grey',command= Next_MIMIC)
            
            # up_button.place(relx=0.598,rely=0.1)
            
            # right_button = Button(Tool_Bar_canvas, image = img4_right, bd = 0,background='grey',command= Next_MIMIC)
            
            # right_button.place(relx=0.628,rely=0.5)
            # Buttton_for_Ack_Sum.place(relx=0.305,rely=0.16,relwidth=0.05,relheight=0.7)
            
            Home_button = Button(Tool_Bar_canvas,text='Home', bd = 3,font=('Times 10'),command= Home_mimic,)
            
            Home_button.place(relx=0.558,rely=0.2,relwidth=0.05,relheight=0.6)
            
            back_button = Button(Tool_Bar_canvas,text='Back', bd = 3,font=('Times 10'),command= back_mimic_event)
            
            back_button.place(relx=0.608,rely=0.2,relwidth=0.05,relheight=0.6)
            
            
            
            ##123456
            ###################################################################################################
            ######################## Mouse button Events #################################################
            #################################################################################################
            
            #####################################################################################################
            #-----------------------Track x and y cords -------------------------------------------------------##
            #####################################################################################################
            
            
            def motion(event):
                
                        global X_and_Y_coord
                        
                        x, y = event.x, event.y
                        x_percent = round((event.x / root.winfo_width()) * 100,2)
                        y_percent = round((event.y / root.winfo_height()) * 100,2)
                        
                        X_and_Y_coord=str(x_percent)+':'+str(y_percent)
                        
                        x_y_cord.configure(text=X_and_Y_coord)
                        
                        # _time_1.configure(text=X_and_Y_coord)
             ##123456          
            #####################################################################################################
            #-----------------------Track x and y cords -------------------------------------------------------##
            #####################################################################################################
            
            
            
            
            
            
            
            
            
            
            
            
            
            root.bind('<Motion>', motion)
            
            root.focus()
            
            root.state(newstate='normal')
            
            '''
                        toplevel_for_mimic=Toplevel()
                        toplevel_for_Trends=Toplevel()
                        toplevel_for_Bar_Graph=Toplevel()
                        toplevel_for_Bar_Graph=Toplevel()
            '''
            
            #####################################################################################################
            #-----------------------Move MIMIC with AWSD -------------------------------------------------------##
            #####################################################################################################
            ##123456
            
            ckbx_unitck=checkbox_of_windows()
            
            
            def tpl_mimic_close_func():
                
                ckbx_unitck.untick_of_mimic_checkbox()
                
                toplevel_for_mimic.withdraw()
                
            def tpl_Trends_close_func():
                
                ckbx_unitck.untick_of_Trends_checkbox()
                
                toplevel_for_Trends.withdraw()
                
                
            def tpl_Bar_Graph_close_func():
                
                ckbx_unitck.untick_of_Bar_Graph_checkbox()
                
                toplevel_for_Bar_Graph.withdraw()
                
            def tpl_Alarms_close_func():
                
                ckbx_unitck.untick_of_Alarms_checkbox()
                
                toplevel_for_Alarms.withdraw()
                
                
            def Clear_all_button_untick_func():
                
                ckbx_unitck.untick_of_Alarms_checkbox()
                
                ckbx_unitck.untick_of_Bar_Graph_checkbox()
                
                ckbx_unitck.untick_of_Trends_checkbox()
                
                ckbx_unitck.untick_of_mimic_checkbox()
                
                
                
                
            def Open_all_button_tick_func():
                
                ckbx_unitck.tick_of_Alarms_checkbox()
                
                ckbx_unitck.tick_of_Bar_Graph_checkbox()
                
                ckbx_unitck.tick_of_Trends_checkbox()
                
                ckbx_unitck.tick_of_mimic_checkbox()
                        
            #####################################################################################################
            #-----------------------TopLevel PRotocol -------------------------------------------------------##
            #####################################################################################################
                
            toplevel_for_mimic.protocol("WM_DELETE_WINDOW",tpl_mimic_close_func )
            
            toplevel_for_Trends.protocol("WM_DELETE_WINDOW", tpl_Trends_close_func)
            
            toplevel_for_Bar_Graph.protocol("WM_DELETE_WINDOW",tpl_Bar_Graph_close_func )
            
            toplevel_for_Alarms.protocol("WM_DELETE_WINDOW", tpl_Alarms_close_func)
            
            
            
            
            
            
            #####################################################################################################
            #-----------------------BInding arrow key change mimic -------------------------------------------------------##
            #####################################################################################################
               
            
            # def Next_MIMIC1(event):
                
            #             Next_MIMIC()
            
            # def Prev_MIMIC1(event):
                
            #             Prev_MIMIC()
            
            
            ##123456
            #####################################################################
            #-------------closing event of windows start------------------------
            #####################################################################
            
            
            def on_closing():
                
                            res = mb.askquestion('Exit Simulator',
                        						'Do you really want to exit')
                            
                            if res == 'yes' :
                               
                                    root.destroy()
                                   
                               
                            else :
                                    mb.showinfo('Return', 'Returning to TSPL HPP Simulator')
            
                    
                    
            
            root.protocol("WM_DELETE_WINDOW", on_closing)
            
            
            ##123456
            #####################################################################
            #-------------closing event of windows   End------------------------
            #####################################################################
            
            '''
                        toplevel_for_mimic=Toplevel()
                        toplevel_for_Trends=Toplevel()
                        toplevel_for_Bar_Graph=Toplevel()
                        toplevel_for_Alarms=Toplevel()
            
            
            
                        toplevel_for_mimic_click=False
                        toplevel_for_Trends_click=False
                        toplevel_for_Bar_Graph=False
                        toplevel_for_Alarms_click=False
                        root_window_click=False
            '''
            
            
            '''
            #click event 
            0=Main Root Window
            1=Mimic Toplevel Window
            2=Trends Toplevel Window
            3=barGraph Toplevel Window
            4=Alarms Toplevel Window
            click_event=0
            
            
            '''
            
            ##123456
            def toplevel_for_mimic_click_event(event):
               
                global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
                click_event=1
                
                toplevel_for_mimic_click=True
                
                toplevel_for_Trends_click=False
                
                toplevel_for_Bar_Graph_click=False
                
                toplevel_for_Alarms_click=False
                
                root_window_click=False
                
            
            
            def toplevel_for_Trends_click_event(event):
                global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
                click_event=2
                toplevel_for_mimic_click=False
                
                toplevel_for_Trends_click=True
                
                toplevel_for_Bar_Graph_click=False
                
                toplevel_for_Alarms_click=False
                
                root_window_click=False
                
            
            
            def toplevel_for_Bar_Graph_click_event(event):
                global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
               # print('clicking bar graph window')
                click_event=3
                
                toplevel_for_mimic_click=False
                
                toplevel_for_Trends_click=False
                
                toplevel_for_Bar_Graph_click=True
                
                toplevel_for_Alarms_click=False
                
                root_window_click=False
                
                
            
            def toplevel_for_Alarms_click_event(event):
                global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
               
                click_event=4
                
                toplevel_for_mimic_click=False
                
                toplevel_for_Trends_click=False
                
                toplevel_for_Bar_Graph_click=False
                
                toplevel_for_Alarms_click=True
                
                root_window_click=False
                
            
            
            
            
            
            
            
            
            
            
            
            # def root_click_event(e):
            #     global click_event,root_window_click,toplevel_for_Alarms_click,toplevel_for_Trends_click,toplevel_for_Bar_Graph_click,toplevel_for_mimic_click
               
            #     root_window_click=True
            #     toplevel_for_mimic_click=False
                
            #     toplevel_for_Trends_click=False
                
            #     toplevel_for_Bar_Graph_click=False
                
            #     toplevel_for_Alarms_click=False
            
            
            ##123456	
            
            toplevel_for_mimic.bind('<Button-1>',toplevel_for_mimic_click_event)
            
            toplevel_for_Trends.bind('<Button-1>',toplevel_for_Trends_click_event)
            
            toplevel_for_Bar_Graph.bind('<Button-1>',toplevel_for_Bar_Graph_click_event)
            
            toplevel_for_Alarms.bind('<Button-1>',toplevel_for_Alarms_click_event)
            # root.bind('<Button-1>',root_click_event)
                
            # root.bind('<Up>',Next_MIMIC1)  
            
            # root.bind('<Down>',Prev_MIMIC1)  
            
            # root.bind('<Left>',Prev_MIMIC1)  
            
            # root.bind('<Right>',Next_MIMIC1)  
            from win.Save_database import Save_Database_window
            def savedata(e):
                
                
                
                
                top=Toplevel(root)
                Save_Database_window(top,root)
                # print("save data")
                # gl.save_database("MW_10")
                
                
            
            root.bind("<Control-l>",lambda event : Database_window_load(event))
          # `  root.bind("<Control-s>",lambda event : Save_Data_Into_Database(event))
            root.bind("<Control-s>",lambda event : savedata(event))
            ##123456
            
            
            
            # open_mimic_by_button()   #calling first mimic as deafult
            # menu_windows_close_all_window()
            glbg.Heading_Name='MAIN MENU'
            
            root.withdraw()
            def wait_for_5_sec():
                time.sleep(5)
                
                
                splash_screen.withdraw()
                root.deiconify()
            
            wait_for_5_sec()
            
            root.mainloop()
else:
    from tkinter import * 
    from tkinter import messagebox as mb 
    root1=Tk()
    root1.configure(background='#5A5A5A')
    
    root1.focus_force()               #foucs to window
    
    root1.title('HYDRO POWER PLANT SIMULATOR')  #Title of root window
    
    root1.state(newstate='normal')   #deafult form normal=on screen ,Iconic=on taskbar
    
    root1.iconbitmap("images/logo.ico")  # icon of root window
    
    
    
    height_of_monitor = root1.winfo_screenheight() #height of monitor
     
    width_of_monitor = root1.winfo_screenwidth()  # width of monitor
    root1.geometry(str(width_of_monitor)+'x'+str(height_of_monitor-70)) # size of root window as state is zoomed(line no 30) this line have no affect
    
    mb.showerror("License Error", "License Key check Faild!!!" )

    
    root1.state("zoomed")      # window will automatically adjusted to screen  
    
    root1.resizable(1,1)       # window resize (width,height) 0=not resize,1=resize allow    
    
    root1.mainloop()
    
    
    
    