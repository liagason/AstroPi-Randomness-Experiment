import os
import csv
import random
import datetime
import hashlib
from time import sleep
from logzero import logger, logfile
from sense_hat import SenseHat

# ----------------------------------------------------
# Team:               Entro PI
# School:             17th Primary School of Agrinio
# Country:            Greece
# Teacher/Instructor: Liagkas Sotirios
# Students:           Dipla Iliana
#                     Bazoni Melina
#                     Papachristos Evangelos
#                     Serleme Lamprini
#                     Tegas Georgios
#                     Chrysanthakopoulou Alexadra
# ----------------------------------------------------
# README: The following code collects data from the
# magnetometer/gyroscope/accelerometer/temperature/
# pressure/humidity sensors and saves them in two
# files (data01.csv, data03.csv). This data is used
# as "seed" in order to produce random integers from
# 0 to 9, that are saved in data02.csv and data04.csv.
#
# All values, in their raw form, are used as "seed"
# to produce random integers using Python's Mersenne
# Twister algorithm as generator. After that, these
# values get "hashed", using Python's SHA256 hash
# function, in order to get more entropic and then
# used, again as "seed", to produce another series of
# random integers between 0 and 9.
#
# The objective of this experiment is to collect data
# in order to analyze it back on Earth and determine
# if using values of natural phenomena as seed is an
# effective way to produce random numbers in the
# controlled enviroment of the ISS.
# ----------------------------------------------------

# Set file paths to save recorded and/or produced data.
dir_path = os.path.dirname(os.path.realpath(__file__))
logfile(dir_path + "/entro_pi.log")
try:
    data_file_01 = dir_path + "/data01.csv"
    data_file_02 = dir_path + "/data02.csv"
    data_file_03 = dir_path + "/data03.csv"
    data_file_04 = dir_path + "/data04.csv"
    logger.info("All file paths were successfully set.")
except:
    logger.error("Failed to set file paths.")
    
# Write headers to data01.csv.
# Raw values, obtained from SenseHAT sensors, will be saved here.
with open(data_file_01, "w") as f:
    writer = csv.writer(f)
    header = ("Date", "Time", "Temperature", "Humidity", "Pressure", "Compass",\
        "Accelerometer_raw_x", "Accelerometer_raw_y", "Accelerometer_raw_z", \
        "Compass_raw_x", "Compass_raw_y", "Compass_raw_z", \
        "Gyroscope_raw_x", "Gyroscope_raw_y", "Gyroscope_raw_z")
    writer.writerow(header)
    logger.info("Added headers to data01.csv.")

# Write headers to data02.csv.
# Random data produced from raw values, obtained from SenseHAT sensors, will be saved here.
with open(data_file_02, "w") as f:
    writer = csv.writer(f)
    header = ("Date", "Time", "Temperature", "Humidity", "Pressure", "Compass",\
        "Accelerometer_raw_x", "Accelerometer_raw_y", "Accelerometer_raw_z", \
        "Compass_raw_x", "Compass_raw_y", "Compass_raw_z", \
        "Gyroscope_raw_x", "Gyroscope_raw_y", "Gyroscope_raw_z", "Default")
    writer.writerow(header)
    logger.info("Added headers to data02.csv.")

# Write headers to data03.csv.
# Hashed (SHA256) values, obtained from SenseHAT sensors, will be saved here.
with open(data_file_03, "w") as f:
    writer = csv.writer(f)
    header = ("Date", "Time", "Temperature", "Humidity", "Pressure", "Compass")
    writer.writerow(header)
    logger.info("Added headers to data03.csv.")

# Write headers to data04.csv.
# Random data produced from hashed (SHA256) values, obtained from SenseHAT sensors, will be saved here.
with open(data_file_04, "w") as f:
    writer = csv.writer(f)
    header = ("Date", "Time", "Temperature", "Humidity", "Pressure", "Compass", "Default")
    writer.writerow(header)
    logger.info("Added headers to data04.csv.")

# Get start time and current time in order run the main loop for 178 minutes.
try:
    start_time = datetime.datetime.now()
    now_time = datetime.datetime.now()
    logger.info("Successfully got start time and current time.")
except:
    logger.error("Failed to get start time and current time.")

# Start SenseHAT sensors.
try:
    sense = SenseHat()
    logger.info("Successfully started SenseHAT sensors.")
except:
    logger.error("Failed to start SenseHAT sensors.")

# Set a variable to count how many times has the main loop run.
i = 0

# Display a random message to inform the ISS crew that the script is running.
# Part 1 (1/3)
def doing_stuff_message():  
    try:    
        # Get a random message...
        temp = random.randint(1,4)
        if temp == 1:
            sense.show_message("=> Doing stuff.")
        if temp == 2:
            sense.show_message("=> Still working.")
        if temp == 3:
            temp = "=> " + str(i*19) + " numbers."
            sense.show_message(temp)
        logger.info("Displayed a text message.")
    except:
        sense.show_message("=> Still in the loop.")
        logger.warning("Failed to display a text message.")
 
# Display an animation to inform the ISS crew that the script is running.
# Part 2 (2/3)
def falling_star_animation():
    try:
        x = [128,0,0]
        y = [220,180,60]
        z = [0,0,10]
        a = [0,100,0]
        b = [250,140,0]

        screen_0 = [
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            a,a,a,a,a,a,a,a
            ]
        
        screen_1 = [
            z,z,z,z,z,z,x,x,
            z,z,z,z,z,z,x,x,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            a,a,a,a,a,a,a,a
            ]

        screen_2 = [
            z,z,z,z,z,y,z,y,
            z,z,z,z,y,z,y,z,
            z,z,z,z,x,x,z,y,
            z,z,z,z,x,x,y,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            a,a,a,a,a,a,a,a
            ]

        screen_3 = [
            z,z,z,z,z,y,z,y,
            z,z,z,z,y,z,y,z,
            z,z,z,y,z,y,z,y,
            z,z,y,z,y,z,y,z,
            z,z,x,x,z,y,z,z,
            z,z,x,x,y,z,z,z,
            z,z,z,z,z,z,z,z,
            a,a,a,a,a,a,a,a
            ]

        screen_4 = [
            z,z,z,z,z,y,z,y,
            z,z,z,z,y,z,y,z,
            z,z,z,y,z,y,z,y,
            z,z,y,z,y,z,y,z,
            z,y,z,y,z,y,z,z,
            y,z,y,z,y,z,z,z,
            x,x,z,y,z,z,z,z,
            a,x,a,a,a,a,a,a
            ]

        screen_5 = [
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            x,z,z,z,z,z,z,z,
            z,z,x,z,z,z,z,z,
            x,x,z,z,z,z,z,z,
            x,x,b,a,a,a,a,a
            ]

        screen_6 = [
            z,z,z,z,z,z,z,z,
            z,z,z,z,z,z,z,z,
            z,z,b,z,z,z,z,z,
            z,z,z,z,b,z,z,z,
            x,z,x,z,x,z,z,z,
            z,z,x,z,z,b,z,z,
            x,b,z,x,z,z,z,z,
            x,x,b,x,a,a,a,a
            ]

        screen_7 = [
            b,z,x,z,x,z,z,b,
            z,z,z,b,z,b,z,z,
            b,x,z,z,z,z,z,x,
            z,b,z,x,z,b,z,z,
            x,z,z,b,z,x,z,x,
            b,z,x,z,x,z,b,z,
            x,x,z,z,x,z,z,x,
            x,x,b,x,b,a,x,b
            ]
        
        # Animation starts here.
        sense.set_pixels(screen_0)
        sleep(0.4)
        sense.set_pixels(screen_1)
        sleep(0.2)
        sense.set_pixels(screen_2)
        sleep(0.2)
        sense.set_pixels(screen_3)
        sleep(0.2)
        sense.set_pixels(screen_4)
        sleep(0.2)
        sense.set_pixels(screen_5)
        sleep(0.2)
        sense.set_pixels(screen_6)
        sleep(0.4)
        sense.set_pixels(screen_7)
        sleep(0.4)
        
        # Animation ends here.
        sense.clear()
    except:
        return None

# Display an animation for ~1 second to inform the ISS crew that the script is running.
# Using this ~1 extra second to avoid getting similar values many times in a row, in order to achieve better entropy.
# Part 3 (3/3)
def doing_stuff_indication():
    try:
        # Get a random RGB color value.
        x = random.randint(0,255)
        y = random.randint(0,255)
        z = random.randint(0,255)
        
        # Animation starts here.
        sense.set_pixel(0, 7, x, y, z)
        sense.set_pixel(0, 6, x, y, z)
        sense.set_pixel(1, 6, x, y, z)
        sense.set_pixel(1, 7, x, y, z)
        sleep(0.3)
        
        sense.set_pixel(3, 7, x, y, z)
        sense.set_pixel(3, 6, x, y, z)
        sense.set_pixel(4, 6, x, y, z)
        sense.set_pixel(4, 7, x, y, z)
        sleep(0.3)
        
        sense.set_pixel(6, 7, x, y, z)
        sense.set_pixel(7, 6, x, y, z)
        sense.set_pixel(6, 6, x, y, z)
        sense.set_pixel(7, 7, x, y, z)
        sleep(0.4)
        
        # Animation ends here.
        sense.clear()
        
    except:
        # Just clear the SenseHAT screen.
        logger.warning("Failed to display animation message.")
        sense.clear()
        return None

# Get a value from a SenseHAT sensor or return None if an error occurs.
def temperature_func():
    try:
        temp = sense.get_temperature()
        return temp
    except:
        logger.warning("Failed to get temperature data.")
        return None

# Get a value from a SenseHAT sensor or return None if an error occurs.
def humidity_func():
    try:
        temp = sense.get_humidity()
        return temp
    except:
        logger.warning("Failed to get humidity data.")
        return None

# Get a value from a SenseHAT sensor or return None if an error occurs.
def pressure_func():
    try:
        temp = sense.get_pressure()
        return temp
    except:
        logger.warning("Failed to get pressure data.")
        return None

# Get a value from a SenseHAT sensor or return None if an error occurs.
def compass_func():
    try:
        temp = sense.get_compass()
        return temp
    except:
        logger.warning("Failed to get compass data.")
        return None

# Get some values from a SenseHAT sensor or return None if an error occurs.
def compass_raw_func():
    try:
        temp = sense.get_compass_raw()
        x = temp['x']
        y = temp['y']
        z = temp['z']
        return x, y, z
    except:
        logger.warning("Failed to get magnetometer data.")
        return None, None, None

# Get some values from a SenseHAT sensor or return None if an error occurs.
def accelerometer_raw_func():
    try:
        temp = sense.get_accelerometer_raw()
        x = temp['x']
        y = temp['y']
        z = temp['z']
        return x, y, z
    except:
        logger.warning("Failed to get accelerometer data.")
        return None, None, None

# Get some values from a SenseHAT sensor or return None if an error occurs.
def gyroscope_raw_func():
    try:
        temp = sense.get_gyroscope_raw()
        x = temp['x']
        y = temp['y']
        z = temp['z']
        return x, y, z
    except:
        logger.warning("Failed to get gyroscope data.")
        return None, None, None

# Produce and return a random number (from 0 to 9) using values from SenseHAT sensors as seed.
def get_random(temp):
    try:
        # Change Python's default seed to a value obtained from SenseHAT sensors.
        random.seed(temp)
        # Produce a random integer (from 0 to 9) using Python's Mersenne Twister as generator.
        temp = random.randint(0,9)
        return temp
    except:
        logger.warning("Failed to produce random data.")
        return None

# Produce and return a random number (from 0 to 9) using Python's default settings.
# This data will help our team later, when we'll compare Python's default seed with our seed (based off) of SenseHAT's sensors.
def get_default_random():
    try:
        temp = random.randint(0,9)
        return temp
    except:
        logger.warning("Failed to produce random data with default Python settings.")
        return None

# Produce and return a random number (from 0 to 9) using hashed (SHA256) values from SenseHAT sensors as seed.
# SHA256 was choosen because it is considered to be secure & relatively fast. It, also, returns highly entropic hashes.
def get_hashed_seed_random(temp):
    try:
        temp = str(temp)
        # Encoding value from SenseHAT sensor in order to get its hash.
        temp = temp.encode('utf-8')
        # Get SHA256 hash from value.
        temp = hashlib.sha256(temp)
        hashed_var = temp.hexdigest()
        random.seed(hashed_var)
        temp = random.randint(0,9)
        return hashed_var, temp
    except:
        logger.warning("Failed to get SHA256 hash from value and/or produce random data.")
        return None 

# Write obtained/produced data to its appropriate file(s).
def add_csv_data(data_file, data):
    with open(data_file, "a") as f:
        try:
            writer = csv.writer(f)
            writer.writerow(data)
        except:
            logger.warning("Failed to write data to file.")

# Display a welcome message to the ISS crew.
logger.info("Displaying welcome message.")
try:
    sense.show_message("=> Starting.")
except:
    logger.warning("Failed to display welcome message.")
    
# Main loop of the script starts here. The loop will run for 178 minutes.
# Every loop last ~1.5 seconds.
logger.info("Starting main loop of the script.")
while (now_time < start_time + datetime.timedelta(minutes = 178)):

    # Get temperature value from SenseHAT sensor.
    # Use its raw form as seed in order to produce and return a random number.
    # Use its hashed (SHA256) form as seed in order to produce and return a random number.
    temperature_data = temperature_func()
    temperature_random_data = get_random(temperature_data)
    temperature_hashed_seed, temperature_hashed_seed_random_data = get_hashed_seed_random(temperature_data)

    # Get humidity value from SenseHAT sensor.
    # Use its raw form as seed in order to produce and return a random number.
    # Use its hashed (SHA256) form as seed in order to produce and return a random number.    
    humidity_data = humidity_func()
    humidity_random_data = get_random(humidity_data)
    humidity_hashed_seed, humidity_hashed_seed_random_data = get_hashed_seed_random(humidity_data)

    # Get pressure value from SenseHAT sensor.
    # Use its raw form as seed in order to produce and return a random number.
    # Use its hashed (SHA256) form as seed in order to produce and return a random number.
    pressure_data = pressure_func()
    pressure_random_data = get_random(pressure_data)
    pressure_hashed_seed, pressure_hashed_seed_random_data = get_hashed_seed_random(pressure_data)

    # Get compass value from SenseHAT sensor.
    # Use its raw form as seed in order to produce and return a random number.
    # Use its hashed (SHA256) form as seed in order to produce and return a random number.
    compass_data = compass_func()
    compass_random_data = get_random(compass_data)
    compass_hashed_seed, compass_hashed_seed_random_data = get_hashed_seed_random(compass_data)

    # Produce and return a random number using Python's default settings.
    default_random = get_default_random()

    # Get accelerometer values from SenseHAT sensor.
    # Use their raw form as seed in order to produce and return three random numbers.
    # Use their hashed (SHA256) form as seed in order to produce and return three random numbers.
    accelerometer_raw_data_x, accelerometer_raw_data_y, accelerometer_raw_data_z = accelerometer_raw_func()
    accelerometer_raw_random_data_x = get_random(accelerometer_raw_data_x)
    accelerometer_raw_random_data_y = get_random(accelerometer_raw_data_y)
    accelerometer_raw_random_data_z = get_random(accelerometer_raw_data_z)

    # Get magnetometer values from SenseHAT sensor.
    # Use their raw form as seed in order to produce and return three random numbers.
    # Use their hashed (SHA256) form as seed in order to produce and return three random numbers.
    compass_raw_data_x, compass_raw_data_y, compass_raw_data_z = compass_raw_func()
    compass_raw_random_data_x = get_random(compass_raw_data_x)
    compass_raw_random_data_y = get_random(compass_raw_data_y)
    compass_raw_random_data_z = get_random(compass_raw_data_z)

    # Get gyroscope values from SenseHAT sensor.
    # Use their raw form as seed in order to produce and return three random numbers.
    # Use their hashed (SHA256) form as seed in order to produce and return three random numbers.
    gyroscope_raw_data_x, gyroscope_raw_data_y, gyroscope_raw_data_z = gyroscope_raw_func()
    gyroscope_raw_random_data_x = get_random(gyroscope_raw_data_x)
    gyroscope_raw_random_data_y = get_random(gyroscope_raw_data_y)
    gyroscope_raw_random_data_z = get_random(gyroscope_raw_data_z)

    # Prepare raw data obtained from SenseHAT sensors to be saved and save it to data01.csv.
    data = now_time , temperature_data, humidity_data, pressure_data, compass_data, \
        accelerometer_raw_data_x, accelerometer_raw_data_y, accelerometer_raw_data_z, \
        compass_raw_data_x, compass_raw_data_y, compass_raw_data_z, \
        gyroscope_raw_data_x, gyroscope_raw_data_y, gyroscope_raw_data_z
    add_csv_data(data_file_01, data)
 
    # Prepare randomly produced data to be saved and save it to data02.csv.   
    random_data = now_time , temperature_random_data, humidity_random_data, pressure_random_data, compass_random_data, \
        accelerometer_raw_random_data_x, accelerometer_raw_random_data_y, accelerometer_raw_random_data_z, \
        compass_raw_random_data_x, compass_raw_random_data_y, compass_raw_random_data_z, \
        gyroscope_raw_random_data_x, gyroscope_raw_random_data_y, gyroscope_raw_random_data_z, default_random
    add_csv_data(data_file_02, random_data)

    # Prepare hashed (SHA256) data obtained from SenseHAT sensors to be saved and save it to data03.csv.
    hashed_seed = now_time , temperature_hashed_seed, humidity_hashed_seed, pressure_hashed_seed, compass_hashed_seed
    add_csv_data(data_file_03, hashed_seed)

    # Prepare randomly produced data to be saved and save it to data04.csv.
    hashed_seed_random_data = now_time , temperature_hashed_seed_random_data, humidity_hashed_seed_random_data, \
        pressure_hashed_seed_random_data, compass_hashed_seed_random_data, default_random
    add_csv_data(data_file_04, hashed_seed_random_data)

    # Update now_time to check if 178 minutes have passed.
    try:
        now_time = datetime.datetime.now()
    except:
        logger.warning("Failed to update current time.")

    # Just sleep for some milliseconds to avoid getting too similar values and achieve better entropy!
    sleep(1)

    # Update i variable to count already finished loops and calculate the total number of randomly produced integers.
    i = i + 1
    
    # Determine if it's time to display a message to the ISS crew (once every 1001 loops).
    if i % 1001 == 0:
        falling_star_animation()
    
    # Determine if it's time to display a message to the ISS crew (once every 101 loops).
    if i % 101 == 0:
        # Display a text message to show that the script is still running.
        doing_stuff_message()
        
    if i % 5 == 0:
        # Display an animation for ~1 second (once every 5 loops).
        doing_stuff_indication()
        logger.info("{} loops completed.".format(i))

# After exit from main loop.
try:  
    # Display a goodbye message and terminate the script.
    sense.show_message("=> Terminated. Goodbye, astronauts.")
    logger.info("Terminated. {} loops completed.".format(i))
except:
    logger.warning("Failed to display goodbye message. {} loops completed.".format(i))