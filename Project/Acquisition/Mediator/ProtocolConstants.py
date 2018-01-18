## Written by Micah Terrell
## Updated for Protocol Version 0.1
## This file defines constants used for protocol messages

## Protocol OpCodes
CONNECT_OPCODE 							= 0x0001
CONNECT_ACK_OPCODE 						= 0x0002
GET_OPTION_OPCODE 						= 0x0010
SEND_OPTION_OPCODE 						= 0x0020
SET_PARAM_OPCODE 						= 0x0030
PARAM_SET_OPCODE 						= 0x0040
START_EXPERIMENT_OPCODE 				= 0x0100
EXPERIMENT_STARTED_OPCODE 				= 0x0200
STOP_EXPERIMENT_OPCODE 					= 0x0300
EXPERIMENT_STOPPED_OPCODE 				= 0x0400
EXPERIMENT_DONE_OPCODE 					= 0x0500
ERROR_OPCODE 							= 0xFFFF

## Protocol Parameter Codes
CHIRP_AMPLITUDE_PARAMETER_CODE 			= 0x01
INPUT_VOLTAGE_PARAMETER_CODE 			= 0x02
UPPER_FREQUENCY_PARAMETER_CODE 			= 0x03
LOWER_FREQUENCY_PARAMETER_CODE 			= 0x04
SAMPLE_RATE_PARAMETER_CODE 				= 0x05
CHIRP_DURATION_PARAMETER_CODE 			= 0x06
CHIRP_WINDOWING_PARAMETER_CODE 			= 0x07
SIGNAL_TYPE_PARAMETER_CODE 				= 0x08
NUMBER_OF_ACQUISITIONS_PARAMETER_CODE   = 0x09