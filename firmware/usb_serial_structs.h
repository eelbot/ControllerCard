//###########################################################################
//
// FILE:   usb_serial_structs.h
//
// TITLE:  USB serial device structure definitions.
//
//###########################################################################
// $TI Release: F2806x C/C++ Header Files and Peripheral Examples V150 $
// $Release Date: June 16, 2015 $
// $Copyright: Copyright (C) 2011-2015 Texas Instruments Incorporated -
//             http://www.ti.com/ ALL RIGHTS RESERVED $
//###########################################################################

#ifndef __USB_SERIAL_STRUCTS_H__
#define __USB_SERIAL_STRUCTS_H__

//*****************************************************************************
//
// The size of the transmit and receive buffers used for the redirected UART.
// This number should be a power of 2 for best performance.  256 is chosen
// pretty much at random though the buffer should be at least twice the size of
// a maxmum-sized USB packet.
//
//*****************************************************************************
#define UART_BUFFER_SIZE 256

extern uint32_t RxHandler(void *pvCBData, uint32_t ui32Event,
                               uint32_t ui32MsgValue, void *pvMsgData);
extern uint32_t TxHandler(void *pvi32CBData, uint32_t ui32Event,
                               uint32_t ui32MsgValue, void *pvMsgData);

extern const tUSBBuffer g_sTxBuffer;
extern const tUSBBuffer g_sRxBuffer;
extern tUSBDCDCDevice g_sCDCDevice;
extern uint8_t g_pui8USBTxBuffer[];
extern uint8_t g_pui8USBRxBuffer[];

#endif // __USB_SERIAL_STRUCTS_H__
