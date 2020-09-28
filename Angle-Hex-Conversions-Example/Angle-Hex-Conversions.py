# 09-27-2020
# This python script is for example,
# created by Dorian White for Haverford Systems
# using Python 3.8.6, for Windows 7
#
# The specification for the application follows:
#
#
# Description
# This is a simple python application that is broken down 
# into two simple parts.  The first part is angles and radians. 
# Here the user should be able to enter an angle in degrees and 
# the application outputs that angle in radians, 
# or the user can enter an angle in radians and the application 
# should output the value in degrees. 
# The second part should allow a user to enter an integer and 
# the output is hexadecimal, 
# or the user can enter a hexadecimal value and an integer is outputted.
#
# Requirements
# 1. The application must allow user inputs.
# 2. The application must output correct values based on the user's input.
# 3. The application must respond with an error message 
#    for incorrect user inputs.
# 4. The application's inputs and outputs must be properly labeled.
# 5. For the hex values section, the calculated hex value should 
#    always be four characters long 
#    and the input must be whole numbers only.

# ----------------------------------------------------------
# ----------------------------------------------------------
# Begin Script----------------------------------------------
# The following modules are used:

# Math module for constant PI
import math

# GUI module for Application Window
import tkinter as tk

# ----------------------------------------------------------
# ----------------------------------------------------------
# The functions for converting input values are first
def degrees_to_radians():
    # Convert the value for degrees to radians 
    # and insert the result into lbl_deg_2_rad.

	# Read the degree entry
    degree_val = ent_degree.get()
	
	# If the input value is a valid real number convert it, 
	# otherwise print an error message  
    try: 
        radian_val = (math.pi/180) * float(degree_val)
        lbl_deg_rad_result["text"] = str(round(radian_val,4)) + " rad."
    except ValueError:
        lbl_deg_rad_result["text"] = "Input Value must be a decimal!"
	
# ----------------------------------------------------------
def radians_to_degrees():
    # Convert the value for radians to degrees 
    # and insert the result into lbl_rad_2_deg.
    
	# Read the radian entry
    radian_val = ent_radian.get()

	# If the input value is a valid real number convert it, 
	# otherwise print an error message  
    try: 
        degree_val = (180/math.pi) * float(radian_val)
        lbl_rad_deg_result["text"] = str(round(degree_val,4)) + " deg."
    except ValueError:
        lbl_rad_deg_result["text"] = "Input Value must be a decimal!"

# ----------------------------------------------------------
def int_to_hex():
    # Convert the value for integer to hex 
    # and insert the result into lbl_int_2_hex.
    
	# Read the integer entry
    integer_val = ent_integer.get()

	# If the input value is a valid whole number convert it, 
	# otherwise print an error message  
    try: 
        hex_val = format((int(integer_val)),"04x")
        if ((int(integer_val)-65535) > 0):
            lbl_int_hex_result["text"] = "Input Value is too large"
        else:
            lbl_int_hex_result["text"] = str(hex_val) + " hex."
    except ValueError:
        lbl_int_hex_result["text"] = "Input Value must be an integer!"

# ----------------------------------------------------------
def hex_to_int():
    # Convert the value for hex to integer 
    # and insert the result into lbl_hex_2_int.
    
	# Read the Hexadecimal entry
    hex_val = ent_hex.get()

	# If the input value is a valid hexadecimal convert it, 
	# otherwise print an error message  
    try: 
        integer_val = int(hex_val,16)
        lbl_hex_int_result["text"] = str(integer_val) + " int."
    except ValueError:
        lbl_hex_int_result["text"] = "Input Value must be a hexadecimal!"
	

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
# Set-up the Angle-Hex-Conversions Window
# and Initialize and Display all conversion Functions

window = tk.Tk()
window.title("Angle-Hex-Conversions")
window.resizable(width=False, height=False)

# -----------------------------------------------------
# ------Grid Row 0-------------------------------------
# Convert Degree to Radians Initialization and Display-
# --------Start----------------------------------------
# -----------------------------------------------------

# Create the Degrees-Radians Conversion frame 
# with an Entry Widget and Label inside of it
frm_entry = tk.Frame(master=window)
ent_degree = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text=" deg.")

# Layout the Degree Entry and Label in frm_entry
# using the .grid() geometry manager
ent_degree.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the Conversion Button and Result Display Label
btn_convert_deg_rad = tk.Button(
    master=window,
    text="Convert to Radians",
    command=degrees_to_radians
)
lbl_deg_rad_result = tk.Label(master=window, text=" ----- rad.")

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert_deg_rad.grid(row=0, column=1, pady=10)
lbl_deg_rad_result.grid(row=0, column=2, padx=10)
# -----------------------------------------------------
# ------Grid Row 0-------------------------------------
# Convert Degree to Radians----------------------------
# --------End------------------------------------------
# -----------------------------------------------------

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

# -----------------------------------------------------
# ------Grid Row 1-------------------------------------
# Convert Radians to Degrees Initialization and Display
# --------Start----------------------------------------
# -----------------------------------------------------
# Create the Radians-Degrees Conversion frame 
# with an Entry Widget and Label inside of it
frm_entry2 = tk.Frame(master=window)
ent_radian = tk.Entry(master=frm_entry2, width=10)
lbl_temp2 = tk.Label(master=frm_entry2, text=" rad.")

# Layout the Radian Entry and Label in frm_entry
# using the .grid() geometry manager
ent_radian.grid(row=0, column=0, sticky="e")
lbl_temp2.grid(row=0, column=1, sticky="w")

# Create the Conversion Button and Result Display Label
btn_convert_rad_deg = tk.Button(
    master=window,
    text="Convert to Degrees",
    command=radians_to_degrees
)
lbl_rad_deg_result = tk.Label(master=window, text=" ----- deg.")

# Set-up the layout using the .grid() geometry manager
frm_entry2.grid(row=1, column=0, padx=10)
btn_convert_rad_deg.grid(row=1, column=1, pady=10)
lbl_rad_deg_result.grid(row=1, column=2, padx=10)
# -----------------------------------------------------
# ------Grid Row 1-------------------------------------
# Convert Radians to Degrees---------------------------
# --------End------------------------------------------
# -----------------------------------------------------

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

# -----------------------------------------------------
# ------Grid Row 2-------------------------------------
# Convert Integer to Hexadecimal Init. and Display-----
# --------Start----------------------------------------
# -----------------------------------------------------
# Create the Integer-Hexadecimal Conversion frame 
# with an Entry Widget and Label inside of it
frm_entry3 = tk.Frame(master=window)
ent_integer = tk.Entry(master=frm_entry3, width=10)
lbl_temp3 = tk.Label(master=frm_entry3, text=" int.")

# Layout the Integer Entry and Label in frm_entry
# using the .grid() geometry manager
ent_integer.grid(row=0, column=0, sticky="e")
lbl_temp3.grid(row=0, column=1, sticky="w")

# Create the Conversion Button and Result Display Label
btn_convert_int_hex = tk.Button(
    master=window,
    text="Convert to Hex",
    command=int_to_hex
)
lbl_int_hex_result = tk.Label(master=window, text=" ----- hex.")

# Set-up the layout using the .grid() geometry manager
frm_entry3.grid(row=2, column=0, padx=10)
btn_convert_int_hex.grid(row=2, column=1, pady=10)
lbl_int_hex_result.grid(row=2, column=2, padx=10)
# -----------------------------------------------------
# ------Grid Row 2-------------------------------------
# Convert Integer to Hexadecimal-----------------------
# --------End------------------------------------------
# -----------------------------------------------------

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

# -----------------------------------------------------
# ------Grid Row 3-------------------------------------
# Convert Hexadecimal to Integer Init. and Display-----
# --------Start----------------------------------------
# -----------------------------------------------------
# Create the Hexadecimal-Integer Conversion frame 
# with an Entry Widget and Label inside of it
frm_entry4 = tk.Frame(master=window)
ent_hex = tk.Entry(master=frm_entry4, width=10)
lbl_temp4 = tk.Label(master=frm_entry4, text=" hex.")

# Layout the Hexadecimal Entry and Label in frm_entry
# using the .grid() geometry manager
ent_hex.grid(row=0, column=0, sticky="e")
lbl_temp4.grid(row=0, column=1, sticky="w")

# Create the Conversion Button and Result Display Label
btn_convert_hex_int = tk.Button(
    master=window,
    text="Convert to Integer",
    command=hex_to_int
)
lbl_hex_int_result = tk.Label(master=window, text=" ----- int.")

# Set-up the layout using the .grid() geometry manager
frm_entry4.grid(row=3, column=0, padx=10)
btn_convert_hex_int.grid(row=3, column=1, pady=10)
lbl_hex_int_result.grid(row=3, column=2, padx=10)
# -----------------------------------------------------
# ------Grid Row 3-------------------------------------
# Convert Hexadecimal to Integer-----------------------
# --------End------------------------------------------
# -----------------------------------------------------

# ----------------------------------------------------------
# ----------------------------------------------------------
# Run the application
window.mainloop()

# End of script
# ----------------------------------------------------------
# ----------------------------------------------------------