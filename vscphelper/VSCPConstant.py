VSCP_PRIORITY_0 =  0x00
VSCP_PRIORITY_1 =  0x20
VSCP_PRIORITY_2 =  0x40
VSCP_PRIORITY_3 =  0x60
VSCP_PRIORITY_4 =  0x80
VSCP_PRIORITY_5 =  0xA0
VSCP_PRIORITY_6 =  0xC0
VSCP_PRIORITY_7 =  0xE0

VSCP_PRIORITY_HIGH =  0x00
VSCP_PRIORITY_LOW =   0xE0
VSCP_PRIORITY_MEDIUM = 0xC0
VSCP_PRIORITY_NORMAL = 0x60

VSCP_HEADER_PRIORITY_MASK = 0xE0

VSCP_HEADER_HARD_CODED = 0x10    # If set node nickname is hardcoded
VSCP_HEADER_NO_CRC = 0x08    # Don't calculate CRC

VSCP_NO_CRC_CALC = 0x08    # If set no CRC is calculated

VSCP_MASK_PRIORITY =  0xE0
VSCP_MASK_HARDCODED = 0x10
VSCP_MASK_NOCRCCALC = 0x08

VSCP_LEVEL1_MAXDATA = 8
VSCP_LEVEL2_MAXDATA = (512 - 25)

VSCP_CAN_ID_HARD_CODED = 0x02000000  # Hard coded bit in CAN frame id

# GUID byte positions
VSCP_GUID_MSB = 0
VSCP_GUID_LSB = 15

# Bootloaders
VSCP_BOOTLOADER_VSCP = 0x00	# VSCP boot loader algorithm
VSCP_BOOTLOADER_PIC1 = 0x01	# PIC algorithm 0
VSCP_BOOTLOADER_AVR1 = 0x10	# AVR algorithm 0
VSCP_BOOTLOADER_LPC1 = 0x20	# NXP/Philips LPC algorithm 0
VSCP_BOOTLOADER_ST =   0x30	# ST STR algorithm 0
VSCP_BOOTLOADER_NONE = 0xff

# Data format masks
VSCP_MASK_DATACODING_TYPE = 0xE0  # Bits 5,6,7
VSCP_MASK_DATACODING_UNIT = 0x18  # Bits 3,4
VSCP_MASK_DATACODING_INDEX = 0x07  # Bits 0,1,2

# Theese bits are coded in the three MSB bytes of the first data byte
# in a paket and tells the type of the data that follows.
VSCP_DATACODING_BIT = 0x00
VSCP_DATACODING_BYTE = 0x20
VSCP_DATACODING_STRING =  0x40
VSCP_DATACODING_INTEGER = 0x60
VSCP_DATACODING_NORMALIZED =   0x80
VSCP_DATACODING_SINGLE =  0xA0	# single precision float
VSCP_DATACODING_RESERVED1 = 0xC0
VSCP_DATACODING_RESERVED2 = 0xE0
# * * * Standard VSCP registers * * *

# Register defines above 0x7f
VSCP_STD_REGISTER_ALARM_STATUS =  0x80

VSCP_STD_REGISTER_MAJOR_VERSION = 0x81
VSCP_STD_REGISTER_MINOR_VERSION = 0x82
VSCP_STD_REGISTER_SUB_VERSION =   0x83

# 0x84 - 0x88
VSCP_STD_REGISTER_USER_ID =       0x84

# 0x89 - 0x8C
VSCP_STD_REGISTER_USER_MANDEV_ID =0x89

# 0x8D -0x90
VSCP_STD_REGISTER_USER_MANSUBDEV_ID = 0x8D

VSCP_STD_REGISTER_NICKNAME_ID =   0x91

VSCP_STD_REGISTER_PAGE_SELECT_MSB =    0x92
VSCP_STD_REGISTER_PAGE_SELECT_LSB =     0x93

VSCP_STD_REGISTER_FIRMWARE_MAJOR =0x94
VSCP_STD_REGISTER_FIRMWARE_MINOR =0x95
VSCP_STD_REGISTER_FIRMWARE_SUBMINOR = 0x96

VSCP_STD_REGISTER_BOOT_LOADER =   0x97
VSCP_STD_REGISTER_BUFFER_SIZE =   0x98
VSCP_STD_REGISTER_PAGES_COUNT =   0x99

# 0xd0 - 0xdf
VSCP_STD_REGISTER_GUID = 0xD0

# 0xe0 - 0xff
VSCP_STD_REGISTER_DEVICE_URL =    0xE0

# Level I Decision Matrix
VSCP_LEVEL1_DM_ROW_SIZE = 8

VSCP_LEVEL1_DM_OFFSET_OADDR =     0
VSCP_LEVEL1_DM_OFFSET_FLAGS =     1
VSCP_LEVEL1_DM_OFFSET_CLASS_MASK =2
VSCP_LEVEL1_DM_OFFSET_CLASS_FILTER =   3
VSCP_LEVEL1_DM_OFFSET_TYPE_MASK = 4
VSCP_LEVEL1_DM_OFFSET_TYPE_FILTER =   5
VSCP_LEVEL1_DM_OFFSET_ACTION =    6
VSCP_LEVEL1_DM_OFFSET_ACTION_PARAM = 7

# Bits for VSCP server 16-bit capability code
# used by CLASS1.PROTOCOL, HIGH END SERVER RESPONSE
VSCP_SERVER_CAPABILITY_TCPIP =    (1<<15)
VSCP_SERVER_CAPABILITY_UDP =      (1<<14)
VSCP_SERVER_CAPABILITY_WEB =      (1<<13)
VSCP_SERVER_CAPABILITY_WEBSOCKET =(1<<12)
VSCP_SERVER_CAPABILITY_REST =     (1<<11)
VSCP_SERVER_CAPABILITY_IP6 =      (1<<6)
VSCP_SERVER_CAPABILITY_IP4 =      (1<<5)
VSCP_SERVER_CAPABILITY_SSL =      (1<<4)
VSCP_SERVER_CAPABILITY_TWO_CONNECTIONS =  (1<<3)


# Error Codes
VSCP_ERROR_SUCCESS =          0      # All is OK
VSCP_ERROR_ERROR =           -1      # Error
VSCP_ERROR_CHANNEL  =         7      # Invalid channel
VSCP_ERROR_FIFO_EMPTY =       8      # FIFO is empty
VSCP_ERROR_FIFO_FULL =        9      # FIFO is full
VSCP_ERROR_FIFO_SIZE =       10      # FIFO size error
VSCP_ERROR_FIFO_WAIT =       11      
VSCP_ERROR_GENERIC =         12      # Generic error
VSCP_ERROR_HARDWARE =        13      # Hardware error
VSCP_ERROR_INIT_FAIL =       14      # Initialization failed
VSCP_ERROR_INIT_MISSING =    15		
VSCP_ERROR_INIT_READY =      16
VSCP_ERROR_NOT_SUPPORTED =   17      # Not supported
VSCP_ERROR_OVERRUN =         18      # Overrun
VSCP_ERROR_RCV_EMPTY =       19      # Receive buffer empty
VSCP_ERROR_REGISTER  =       20      # Register value error
VSCP_ERROR_TRM_FULL  =       21      # Transmit buffer full
VSCP_ERROR_LIBRARY  =        28      # Unable to load library
VSCP_ERROR_PROCADDRESS =     29      # Unable get library proc. address
VSCP_ERROR_ONLY_ONE_INSTANCE=30      # Only one instance allowed
VSCP_ERROR_SUB_DRIVER =      31      # Problem with sub driver call
VSCP_ERROR_TIMEOUT  =        32      # Time-out
VSCP_ERROR_NOT_OPEN  =       33      # The device is not open.
VSCP_ERROR_PARAMETER =       34      # A parameter is invalid.
VSCP_ERROR_MEMORY =          35      # Memory exhausted.
VSCP_ERROR_INTERNAL  =       36      # Some kind of internal program error
VSCP_ERROR_COMMUNICATION =   37      # Some kind of communication error
VSCP_ERROR_USER =            38      # Login error user name
VSCP_ERROR_PASSWORD  =       39      # Login error password
VSCP_ERROR_CONNECTION =      40      # Could not connect   
VSCP_ERROR_OPERATION_FAILED =42      # Operation failed for some reason

VSCP_ERROR_NOT_AUTHORIZED =  43 	 #User is not authorized
VSCP_ERROR_SYNTAX =          44		 #Invalid syntax
VSCP_ERROR_DEFINED_VAR =     45		 #Variable is already defined
VSCP_ERROR_VAR_NOT_FOUND =   46      #Variable is not found

error_description = {
    VSCP_ERROR_SUCCESS:         "All is OK",
    VSCP_ERROR_ERROR:           "Error",
    VSCP_ERROR_CHANNEL:         "Invalid channel",#not used
    VSCP_ERROR_FIFO_EMPTY:      "FIFO is empty",#not used
    VSCP_ERROR_FIFO_FULL:       "FIFO is full",#not used
    VSCP_ERROR_FIFO_SIZE:       "FIFO size error",#not used
    VSCP_ERROR_FIFO_WAIT:       "FIFO error",   #not used
    VSCP_ERROR_GENERIC:         "Generic error",#not used
    VSCP_ERROR_HARDWARE:        "Hardware error",#not used
    VSCP_ERROR_INIT_FAIL:       "Initialization failed",#not used
    VSCP_ERROR_INIT_MISSING:    "Mission initialization",#not used
    VSCP_ERROR_INIT_READY:      "Initialization is not finished",#not used
    VSCP_ERROR_NOT_SUPPORTED:   "Not supported",
    VSCP_ERROR_OVERRUN:         "Overrun",#not used
    VSCP_ERROR_RCV_EMPTY:       "Receive buffer empty",#not used
    VSCP_ERROR_REGISTER:        "Register value error",#not used
    VSCP_ERROR_TRM_FULL:        "Transmit buffer full",
    VSCP_ERROR_LIBRARY:         "Unable to load library",#not used
    VSCP_ERROR_PROCADDRESS:     "Unable get library proc. address",#not used
    VSCP_ERROR_ONLY_ONE_INSTANCE: "Only one instance allowed",#not used
    VSCP_ERROR_SUB_DRIVER:      "Problem with sub driver call",#not used
    VSCP_ERROR_TIMEOUT:         "Time-out",#not used
    VSCP_ERROR_NOT_OPEN:        "The device is not open.",#not used
    VSCP_ERROR_PARAMETER:       "A parameter is invalid.",#not used
    VSCP_ERROR_MEMORY:          "Memory exhausted.",#not used
    VSCP_ERROR_INTERNAL:        "Some kind of internal program error",#not used
    VSCP_ERROR_COMMUNICATION:   "Some kind of communication error",#not used
    VSCP_ERROR_USER:            "Login error user name",#not used
    VSCP_ERROR_PASSWORD:        "Login error password",
    VSCP_ERROR_CONNECTION:      "Could not connect   ",
    VSCP_ERROR_OPERATION_FAILED:"Operation failed for some reason",
    
    VSCP_ERROR_NOT_AUTHORIZED:  "User is not authorized",
    VSCP_ERROR_SYNTAX:          "Invalid syntax",
    VSCP_ERROR_DEFINED_VAR:     "Variable is already defined",
    VSCP_ERROR_VAR_NOT_FOUND:   "Variable is not found" 
}