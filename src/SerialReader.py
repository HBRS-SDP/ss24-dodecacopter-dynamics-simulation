import serial.tools.list_ports as Ports
from typing import List,Callable
import serial
import re
import time
import threading
    
#  old version .py Class but data is not readen per byte


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
        


class SerialReader():

    def __init__(self,
                 port : str,
                 baud_rate  : int = 9600 ,
                 timeout    : int = None , 
                 initilizer : str = None,
                 callback   : Callable = None,
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
        self.crc16 = crc16
        self.callback = callback

        # Initializeing the serial port
        self.ser.write(bytes.fromhex(self.initilizer))

        # Creating the threads
        # self.t1 = threading.Thread(target= self.read)
        # # self.t2 = threading.Thread(target= self.write())
        # self.t3 = threading.Thread(target= self.stop)

        # self.t1.daemon = True  # Ensuring the thread will exit when the main program exits
        # self.t3.daemon = True 

        # # Keeping threads alive
        # self.t1.start()
        # # self.t2.start()
        # self.t3.start()

    
    def read(self) -> str:

        buffer = ''
        data_stream = ''

        while self.running:

            if not self.ser.is_open:
                self.ser.open()

            if self.ser.in_waiting > 0 :
                data_stream += self.ser.read(50).hex()
                # data_stream = self.ser.read(min(self.ser.in_waiting, 420)).hex()

                # byte = self.ser.read(1).hex()
                # data_stream += byte

                if data_stream and '5566' in data_stream:
                    
                    # Find length of data for the first match starting with 5566
                    raw_len = self.datalen_finder(data_stream)  
                    # print(raw_len)
                    if raw_len:
                        # Put it in right order
                        reversed_len = self.reverse(raw_len)       
                        # Find number of data length in hex characters
                        data_len = self.datalen_hex(reversed_len) 
                        # Reading the first match in the input stream 
                        pattern_string = fr'5566.{{12}}.{{{data_len}}}.{{4}}'    
                        pattern = re.compile(pattern_string, re.IGNORECASE)
                        match = pattern.search(data_stream)

                        if match:

                            found_data = match.group()

                            # Seprating Checksum and data
                            data = found_data[:len(found_data)-4]
                            recieved_crc16 = found_data[-4:]
                            
                            # Converting data to a list of integer values to calculate checksum for it
                            byte_list = [int(data[i:i+2], 16) for i in range(0, len(data), 2)] 
                            crc_calculated = crc16_cal(byte_list, len(byte_list))

                            # Verifying data validity, updating data_stream and buffer registers
                            if recieved_crc16 == crc_calculated:
                                buffer += found_data                            
                                data_stream = data_stream.replace(found_data,'')
                            else:
                                # Data not valid, discard
                                data_stream = data_stream.replace(found_data,'')

                            # Send the data to Ros node and clean the buffer
                            if buffer:
                                if len(buffer) < data_len :
                                    buffer = ''
                                else:
                                    print(buffer)
                                    # self.callback(buffer)
                                    buffer = ''

            else:
                time.sleep(0.0001)   

    
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
        This function calculates the data length in hexadecimal characters. 
        '''
        byte_value = bytes.fromhex(f'{revised_len}')
        decimal_value = int.from_bytes(byte_value)
        # print('Data length in bytes:',decimal_value)  
        # print('Data length in hex:',decimal_value *2)

        return decimal_value *2

ser = SerialReader(port = '/dev/cu.usbmodemN32G45x1',
                   baud_rate=57600,
                   initilizer='556601010000004202b5c0'
                        )
try:
    ser.read()

except KeyboardInterrupt:
    ser.stop()
    print("KeyboardInterrupt caught! Stopping the runner...")
    print("Exiting gracefully.")
        
