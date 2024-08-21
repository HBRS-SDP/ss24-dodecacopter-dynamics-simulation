import serial.tools.list_ports as Ports
from typing import List,Callable
from collections import defaultdict
import serial
import re
import numpy as np
import rospy
from sensor_msgs.msg import Joy
    
# Final version. Class + data is readed byte by byte


ports = Ports.comports()
for port in ports:
    print(f"Port: {port.device}, Description: {port.description}")


CRC16_XMODEM_TABLE = [
        0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50a5, 0x60c6, 0x70e7,
        0x8108, 0x9129, 0xa14a, 0xb16b, 0xc18c, 0xd1ad, 0xe1ce, 0xf1ef,
        0x1231, 0x0210, 0x3273, 0x2252, 0x52b5, 0x4294, 0x72f7, 0x62d6,
        0x9339, 0x8318, 0xb37b, 0xa35a, 0xd3bd, 0xc39c, 0xf3ff, 0xe3de,
        0x2462, 0x3443, 0x0420, 0x1401, 0x64e6, 0x74c7, 0x44a4, 0x5485,
        0xa56a, 0xb54b, 0x8528, 0x9509, 0xe5ee, 0xf5cf, 0xc5ac, 0xd58d,
        0x3653, 0x2672, 0x1611, 0x0630, 0x76d7, 0x66f6, 0x5695, 0x46b4,
        0xb75b, 0xa77a, 0x9719, 0x8738, 0xf7df, 0xe7fe, 0xd79d, 0xc7bc,
        0x48c4, 0x58e5, 0x6886, 0x78a7, 0x0840, 0x1861, 0x2802, 0x3823,
        0xc9cc, 0xd9ed, 0xe98e, 0xf9af, 0x8948, 0x9969, 0xa90a, 0xb92b,
        0x5af5, 0x4ad4, 0x7ab7, 0x6a96, 0x1a71, 0x0a50, 0x3a33, 0x2a12,
        0xdbfd, 0xcbdc, 0xfbbf, 0xeb9e, 0x9b79, 0x8b58, 0xbb3b, 0xab1a,
        0x6ca6, 0x7c87, 0x4ce4, 0x5cc5, 0x2c22, 0x3c03, 0x0c60, 0x1c41,
        0xedae, 0xfd8f, 0xcdec, 0xddcd, 0xad2a, 0xbd0b, 0x8d68, 0x9d49,
        0x7e97, 0x6eb6, 0x5ed5, 0x4ef4, 0x3e13, 0x2e32, 0x1e51, 0x0e70,
        0xff9f, 0xefbe, 0xdfdd, 0xcffc, 0xbf1b, 0xaf3a, 0x9f59, 0x8f78,
        0x9188, 0x81a9, 0xb1ca, 0xa1eb, 0xd10c, 0xc12d, 0xf14e, 0xe16f,
        0x1080, 0x00a1, 0x30c2, 0x20e3, 0x5004, 0x4025, 0x7046, 0x6067,
        0x83b9, 0x9398, 0xa3fb, 0xb3da, 0xc33d, 0xd31c, 0xe37f, 0xf35e,
        0x02b1, 0x1290, 0x22f3, 0x32d2, 0x4235, 0x5214, 0x6277, 0x7256,
        0xb5ea, 0xa5cb, 0x95a8, 0x8589, 0xf56e, 0xe54f, 0xd52c, 0xc50d,
        0x34e2, 0x24c3, 0x14a0, 0x0481, 0x7466, 0x6447, 0x5424, 0x4405,
        0xa7db, 0xb7fa, 0x8799, 0x97b8, 0xe75f, 0xf77e, 0xc71d, 0xd73c,
        0x26d3, 0x36f2, 0x0691, 0x16b0, 0x6657, 0x7676, 0x4615, 0x5634,
        0xd94c, 0xc96d, 0xf90e, 0xe92f, 0x99c8, 0x89e9, 0xb98a, 0xa9ab,
        0x5844, 0x4865, 0x7806, 0x6827, 0x18c0, 0x08e1, 0x3882, 0x28a3,
        0xcb7d, 0xdb5c, 0xeb3f, 0xfb1e, 0x8bf9, 0x9bd8, 0xabbb, 0xbb9a,
        0x4a75, 0x5a54, 0x6a37, 0x7a16, 0x0af1, 0x1ad0, 0x2ab3, 0x3a92,
        0xfd2e, 0xed0f, 0xdd6c, 0xcd4d, 0xbdaa, 0xad8b, 0x9de8, 0x8dc9,
        0x7c26, 0x6c07, 0x5c64, 0x4c45, 0x3ca2, 0x2c83, 0x1ce0, 0x0cc1,
        0xef1f, 0xff3e, 0xcf5d, 0xdf7c, 0xaf9b, 0xbfba, 0x8fd9, 0x9ff8,
        0x6e17, 0x7e36, 0x4e55, 0x5e74, 0x2e93, 0x3eb2, 0x0ed1, 0x1ef0,
        ]

def crc16_cal(data : List[int], length : int) -> str:
    ''' 
    data : List of bytes
    length : Length of data 
    '''
    crc = 0x0000
    for i in range(length):
        temp = (crc >> 8) & 0xFF
        crc = ((crc << 8) & 0xFFFF) ^ CRC16_XMODEM_TABLE[(data[i] ^ temp) & 0xFF]
    
    crc = hex(crc)[2:]
    crc_byte1 = crc[:2]  # crc16 might not always be 4 characters! Need to reverse it byte by byte
    crc_byte2 = crc[2:]
    crc_reversed = crc_byte2 + crc_byte1
    return crc_reversed


class Initializer():

    ''' 
    Creates the initializer massage Request Channel Data
    '''
    
    def __init__(self,
                 STX: str = '5566',
                 CTRL  : str = '01',
                 Data_len : str = '0100', 
                 SEQ   : str = '0000', 
                 CMD_ID   : str = '4202', 
                 CRC16 : Callable = crc16_cal
                 ) -> None:
        
        self.STX = STX
        self.CTRL = CTRL
        self.Data_len = Data_len
        self.SEQ = SEQ
        self.CMD_ID = CMD_ID
        self.CRC16 = CRC16

    def initialize(self) -> str :

        data = self.STX+self.CTRL+self.Data_len+self.SEQ+self.CMD_ID

        byte_list = [int(data[i:i+2], 16) for i in range(0, len(data), 2)]
        
        crc16 = self.CRC16(byte_list,len(byte_list))

        return data+crc16
        

class JoyPublisher:
    def __init__(self) :
        rospy.init_node('joy_publisher', anonymous=True)
        self.publisher = rospy.Publisher('joy', Joy, queue_size=10)
        self.rate = rospy.Rate(10)  # 10 Hz
        

    def publish_joy_message(self, data : list[int]):
        while not rospy.is_shutdown():
            joy_msg = Joy()
            
            # Simulate joystick axes
            joy_msg.axes = data

            self.publisher.publish(joy_msg)
            rospy.loginfo(f'Published Joy message: Axes: {joy_msg.axes}, Buttons: {joy_msg.buttons}')
            self.rate.sleep()



class SerialReader():

    def __init__(self,
                 port : str,
                 baud_rate  : int = 9600 ,
                 timeout    : int = None , 
                 initilizer : str = None,
                 desired_idx: list[int] = None,  # A list specifying the desired order or channel data, range [0-16)
                 crc16      : Callable = crc16_cal
                 ) -> None :
        
        '''
        Parameters:
        port (str): The serial port to connect to.
        baud_rate (int): The baud rate to use.
        timeout (int): The time to wait for a response.
        initilizer (str): The initial message to send to the serial port.
        callback (Callable): The callback function to send the buffer data to ROS node.
        '''

        self.ser = serial.Serial(
                                port=port, 
                                baudrate=baud_rate,
                                timeout= timeout
                                ) 
        self.initilizer = initilizer
        self.running = True
        self.desired_idx = desired_idx
        self.callback_node = JoyPublisher()
        self.crc16 = crc16

        # Initializeing the serial port
        self.ser.write(bytes.fromhex(self.initilizer))

    def read(self) -> str:

        buffer = ''
        channel_data_dict = defaultdict()
        num_of_channels = 16
        i = 1
        n = 0


        while self.running:

            if not self.ser.is_open:
                self.ser.open()


            buffer += self.ser.read(1).hex()

            if buffer == '55':
                buffer += self.ser.read(1).hex()
            else:
                buffer = ''

            if buffer == '5566':
                    buffer += self.ser.read(6).hex()
                    data_len = self.datalen_hex(self.reverse(self.datalen_finder(buffer)))
                    buffer += self.ser.read(int(data_len)).hex()
                    buffer += self.ser.read(2).hex()
            else:
                buffer = ''

            data = buffer[:len(buffer)-4]
            recieved_crc16 = buffer[-4:]

            # Converting data to a list of integer values to calculate checksum for it
            byte_list = [int(data[i:i+2], 16) for i in range(0, len(data), 2)] 
            crc_calculated = crc16_cal(byte_list, len(byte_list))

            # Verifying data validity
            if recieved_crc16 == crc_calculated and len(buffer)> int(data_len) :

                while i <= num_of_channels:
                
                    # channel_data_dict[f'CH[{i}]'] = int(data[16:][n:n+4],16) if data[16:][n:n+4] else None
                    channel_data_dict[f'CH[{i}]'] = data[16:][n:n+4] if data[16:][n:n+4] else None

                    n+=4
                    i += 1
                else:
                    i = 1
                    n = 0

                print(channel_data_dict)

                # Again, reversing the order of MSB and LSB for hex data in each channel!

                for key,value in channel_data_dict.items():

                    if value is not None:
                        channel_data_dict[key] = int(self.reverse(value),16)
                
                print(channel_data_dict)


                # Mapping data into desired output channel order, needs to be specified initially.

                ordered_data = self.ch_data_transformer(channel_data_dict,self.desired_idx)
                
                #Publishing data to ROS node

                self.callback_node.publish_joy_message(ordered_data)

                buffer = ''
            else:
                print('Received data has INVALID CRC!')
                buffer = ''



    def stop(self):
       
        self.running = False
        self.ser.close()

        return None

    def datalen_finder(self, data_stream : str) -> str:
        ''' 
        This function extracts the initial-raw length from the stream of input data.
        '''

        # Find '5566' followed by any two characters and capture the next four characters
        pattern_string = r'5566..(.{4})'
        pattern = re.compile(pattern_string, re.IGNORECASE)

        # Find the first matche
        match = pattern.search(data_stream)
        
        return match.group()[-4:]


    def reverse(self, input : str) -> str:

        '''
        This function resolves the LSM front issue in the datasheet, putting MSB in front
        '''
        input_byte1 = input[:2]  
        input_byte2 = input[2:]
        reversed = input_byte2 + input_byte1

        return reversed


    def datalen_hex(self, revised_len : str) -> int:
        ''' 
        This function calculates the data length in bytes (or can be used for hexadecimal characters). 
        '''
        byte_value = bytes.fromhex(f'{revised_len}')
        decimal_value = int.from_bytes(byte_value)
        # print('Data length in bytes:',decimal_value)  

        return decimal_value 
    
    def ch_data_transformer (self,ch_data_dict : dict, desired_idx : list[int]) -> list[int] :

        channel_data_list = list(ch_data_dict.values())
        out_list = np.zeros(16)

        # Mapping the channel dsata based on the desired output channel index

        for in_idx,out_idx in enumerate(desired_idx):
            
            out_list[in_idx] =  channel_data_list[out_idx] 

        return out_list


# Replace this with your own desired output channel data order, must be range [0-16) 
desired_idx = [13,6,0,4,3,8,9,12,10,15,14,1,7,11,1,2]

ser = SerialReader(port = '/dev/cu.usbmodemN32G45x1',
                   baud_rate=57600,
                   desired_idx= desired_idx,
                   initilizer= Initializer().initialize()
                        )
try:
    ser.read()

except KeyboardInterrupt:
    ser.stop()
    print("KeyboardInterrupt caught! Stopping the runner...")
    print("Exiting gracefully.")
        
