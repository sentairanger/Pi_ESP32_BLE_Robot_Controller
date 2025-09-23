import asyncio
from bleak import BleakClient, uuids
from gpiozero import LED, Robot, PWMOutputDevice, Motor

connected = False   
pwm = PWMOutputDevice(12)
pwm2 = PWMOutputDevice(26)
led = LED(17)
robot = Robot(left=Motor(27, 22), right=Motor(13, 21))

# Replace with the MAC address of your ESP32
esp_32 = "9C:9C:1F:E9:FF:C2"


# Reference the ESP32 UUIDs
TEMP_UUID = "19b10001-e8f2-537e-4f6c-d104768a1214"
SERVICE_UUID = "19b10000-e8f2-537e-4f6c-d104768a1214"

async def receive_data_task(client):
    """Receive data from the peripheral device."""
    while True:
        try:
            # print("Central waiting for data from peripheral...")
            response = await client.read_gatt_char(TEMP_UUID)
            message = response.decode('utf-8').strip()
            values = [int(item.split('=')[1]) for item in message.split(',')]
            forward, backward, left, right, speed = values 
            forward_button = forward
            backward_button = backward
            left_button = left
            right_button = right
            speed = speed_value
            norm = max(0.0, min(1.0, speed_value / 4095.0))
            pwm.value = norm
            pwm2.value = norm 
            if forward_button == 0:
                robot.forward()
            elif backward_button == 0:
                robot.backward()
            elif left_button == 0:
                robot.left()
            elif right_button == 0:
                robot.right()
            else:
                robot.stop()
            await asyncio.sleep(0.1)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

async def blink_task():
    global connected 
    print("blink task started")
    toggle = True 
    while True:
        if toggle:
            led.on() 
        else:
            led.off()
        toggle = not toggle 
        blink = 1000  if connected else 250
        await asyncio.sleep(blink / 1000)



async def connect_and_communicate(address):
    global connected
    """Connect to the peripheral and manage data exchange."""
    print(f"Connecting to {address}...")

    async with BleakClient(address) as client:
        connected = client.is_connected
        print(f"Connected: {connected}")

        # Create tasks for sending and receiving data
        tasks = [
            asyncio.create_task(receive_data_task(client)),
            asyncio.create_task(blink_task())
        ]
        await asyncio.gather(*tasks)
    connected = False

# Run the connection and communication
loop = asyncio.get_event_loop()
loop.run_until_complete(connect_and_communicate(pico_address))