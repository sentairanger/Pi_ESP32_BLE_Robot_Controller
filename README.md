# Pi_ESP32_BLE_Robot_Controller
In this project, The ESP32 works as a BLE robot controller controlling a Raspberry Pi Robot.

In the folder, `esp32_robot.py` runs on the Pi. Yes, the filename is confusing but I assure you that it's correct since it connects to the ESP32. To get this to run, inside this folder, create a virtual environment and call it whatever you like. I would call it `blue` since we're using BLE. Do this by running `python3 -m venv blue`. Then activate with `source blue/bin/activate`. Then you need to install pigpio. gpiozero and bleak with `pip`. After that you're ready to go. 

On the ESP32 side `robot_bleak.py` is the code for the controller. You need to install `aioble` either using the Tools menu in Thonny or do what I did which is clone the micropython-libs repository, create a libs directory in the ESP32 and then copy the `aioble` folder inside the `libs` directory. Whatever you choose when you're done you're ready to go. Note, be sure you installed micropython in your ESP32 first. Once you're done run the code on Thonny first and then on the Pi you can run the code once the ESP32 advertises. Once you're done you can start controlling your robot.

![picture](https://github.com/sentairanger/Pi_ESP32_BLE_Robot_Controller/blob/main/robot_bb.jpg)
