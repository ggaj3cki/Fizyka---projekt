import numpy as np
import math
from tkinter import *
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

G = 9.81 # Gravitational constant
V0 = 0 
while(V0 < 10 or V0 > 30):
    try:
        V0 = int(input("Podaj prędkość początkową w m/s (od 10 do 30 - liczba musi być liczbą całkowitą): ")) # initial velocity (in mps)
    except ValueError:
        print("Wprowadzona wartość jest niepoprawna. Spróbuj ponownie")
angle = 0 # initial launch angle (between 0 and 90)
while(angle < 15 or V0 > 75):
    try:
        angle = int(input("Podaj kąt (od 15 do 75 - liczba musi być liczbą całkowitą): "))
    except ValueError:
        print("Wprowadzona wartość jest niepoprawna. Spróbuj ponownie")
currentDistance= 0 # distance value between 0 and totalRange on x axis (in meters)
currentTime = 0 # time value between 0 and tc (in seconds)
mass = 0 # if greater than 0 - as another parameter (in kg)
while(mass < 1 or mass > 20):
    try:
        mass = int(input("Podaj masę obiektu w kg (od 1 do 20 - liczba musi być liczbą całkowitą): "))
    except ValueError:
        print("Wprowadzona wartość jest niepoprawna. Spróbuj ponownie")
work = 0 # if greater than 0 - used as another parameter (in J)


radianOfAngle = math.radians(angle) # convert from degrees to radians to make used functions work (math.radian() function)
Vh = V0 * math.cos(radianOfAngle) # horizontal velocity (in mps) - constant (never change in value)
Vv0 = V0 * math.sin(radianOfAngle) # initial vertical velocity (in mps)
tm = Vv0 / G # time of a projectile motion to the maximum height
tc = 2 * tm # total time of a projectile motion (in s)
totalRange = Vh * tc # total horizontal range of a projectile motion (in meters)

def furthestPossible(): #for scaling x axis in plot
    radianOfAngle = math.radians(45)
    Vv0 = V0 * math.sin(radianOfAngle)
    tc = 2*(Vv0 / G)
    return round((math.cos(math.radians(45))*V0)*tc, 2)

def highestPossible(): # for scaling y axis in plot
    radianOfAngle = math.radians(90)
    vh = V0 * math.cos(radianOfAngle)
    Vv0 = V0 * math.sin(radianOfAngle)
    tc = 2*(Vv0 / G)
    x = (vh*tc)/2
    return round((x * math.tan(radianOfAngle) - ((G*math.pow(x,2))/(2*math.pow(V0,2)*math.pow(math.cos(radianOfAngle),2)))),2)

def equationOfMotion(x):
    return round((x * math.tan(radianOfAngle) - ((G*math.pow(x,2))/(2*math.pow(V0,2)*math.pow(math.cos(radianOfAngle),2)))),2) #functon y(x),

def equationOfMotionByTime(time):
    return  (Vv0 * time) - ((G*math.pow(t,2))/2) #function y(t)

def maxHeight():
    return equationOfMotion(totalRange/2)

def verticalVelocity(t):
    return abs(round(Vv0 - G*t, 2))

def velocity(t): # velocity value based on time
    return math.pow((math.pow(verticalVelocity(t),2)+math.pow(Vh,2)),0.5)

def distanceInTime(t):
    return Vh * t

def heightInTime(t):
    x = distanceInTime(t)
    return equationOfMotion(x)

def distVelocity(distance): # velosity value based on distance
    t = distance / Vh
    return velocity(t)

def initialVelosityKe(w, m): # initial velocity (in mps) using mass and work (kinetic energy)
    return round(math.pow(((2*w)/m),0.5), 2)

def massCount(w, v): # mass count usint work and velocity
    return round((math.pow(V0, 2)/(2*work)), 2)

def workCount(): # work count using mass and velocity
    return round(0.5*mass*math.pow(V0, 2),2)


def plot(): 
  
    fig = Figure(figsize = (10, 10), 
                 dpi = 100) 

    # arrays of values used for generating the graph
    ploty = np.array([equationOfMotion(i.item()) for i in np.linspace(0, totalRange, 100)])
    plotx = np.array([round(i.item(), 2) for i in np.linspace(0, totalRange, 100)])
  
    # adding the subplot 
    plot1 = fig.add_subplot()
    plot1.set_xlabel("Odleglosc (m)")
    plot1.set_ylabel("Wysokosc (m)")
    plot1.set_title("Trajektoria rzutu")
    plot1.set_xlim(0, (furthestPossible()+0.01)*1.1)
    plot1.set_ylim(0, (highestPossible()+0.01)*1.1)
  
    # plotting the graph 
    plot1.plot(plotx, ploty)
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
# the main Tkinter window 
window = Tk() 
  
# setting the title  
window.title('Grzegorz Gajecki - Projekt: Wykres Rzutu Ukośnego') 
  
# dimensions of the main window 
window.geometry("800x800")
  
# button that displays the plot 
plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,
                     font=(12),  
                     width = 10, 
                     text = "Wykres") 
  
# place the button  
# in main window 
plot_button.pack()

printHorizontalVelocity = Label(window,
              text=f"Prędkość pozioma: {round(Vh, 2)} m/s",
              font=(12),
              compound='bottom')
printHorizontalVelocity.pack()

printVerticalVelocity = Label(window,
              text=f"Prędkość pionowa początkowa: {round(Vv0, 2)} m/s",
              font=(12),
              compound='bottom')
printVerticalVelocity.pack()

printRange = Label(window,
              text=f"Odległość maksymalna: {round(totalRange, 2)} m",
              font=(12),
              compound='bottom')
printRange.pack()

printMaxHeight = Label(window,
              text=f"Maksymalna wysokość: {round(maxHeight(), 2)} m",
              font=(12),
              compound='bottom')
printMaxHeight.pack()

printTotalTime = Label(window,
              text=f"Całkowity czas lotu: {round(tc, 2)} s",
              font=(12),
              compound='bottom')
printTotalTime.pack()

printWork = Label(window,
              text=f"Praca wykonana podczas rzutu: {round(workCount(), 2)} J",
              font=(12),
              compound='bottom')
printWork.pack()
  
# run the gui 
window.mainloop()
