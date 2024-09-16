# import pvporcupine
# import pvrhino

# import pyaudio
# from playsound import playsound
# from pvrecorder import PvRecorder

# # Getting Audio Frames using Pyaudio
# # from here we can change the Frame rate and frame per buffer

# # ======================= Audio Frame Input =========================

# class argos_wakeword(): 

#     def pyaudio_str(self,rate,frames_per_buffer): # Using Pyaudio
#         pa = pyaudio.PyAudio() 
#         audio_stream = pa.open(
#             rate=rate,
#             channels=1,
#             format=pyaudio.paInt16,
#             input=True,
#             frames_per_buffer=frames_per_buffer)
#         return audio_stream,pa 

#     def argos(self):
        
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Device Control Panel")

# Create a larger canvas widget to accommodate all labels
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# Draw five circles (devices) with initial color red (off)
light_1 = canvas.create_oval(50, 50, 150, 150, fill="red")
canvas.create_text(100, 170, text="LIGHT-1")

light_2 = canvas.create_oval(200, 50, 300, 150, fill="red")
canvas.create_text(250, 170, text="LIGHT-2")

fan_1 = canvas.create_oval(350, 50, 450, 150, fill="red")
canvas.create_text(400, 170, text="FAN-1")

fan_2 = canvas.create_oval(50, 200, 150, 300, fill="red")
canvas.create_text(100, 320, text="FAN-2")

cooler = canvas.create_oval(200, 200, 300, 300, fill="red")
canvas.create_text(250, 320, text="COOLER")

# Functions to toggle devices on (green) and off (red)
def light_1_on():
    canvas.itemconfig(light_1, fill="green")

def light_1_off():
    canvas.itemconfig(light_1, fill="red")

def light_2_on():
    canvas.itemconfig(light_2, fill="green")

def light_2_off():
    canvas.itemconfig(light_2, fill="red")

def fan_1_on():
    canvas.itemconfig(fan_1, fill="green")

def fan_1_off():
    canvas.itemconfig(fan_1, fill="red")

def fan_2_on():
    canvas.itemconfig(fan_2, fill="green")

def fan_2_off():
    canvas.itemconfig(fan_2, fill="red")

def cooler_on():
    canvas.itemconfig(cooler, fill="green")

def cooler_off():
    canvas.itemconfig(cooler, fill="red")

root.mainloop()
