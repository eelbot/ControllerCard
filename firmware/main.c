/*
 * main.c
 */

#include "F2806x_Device.h"
#include "F2806x_Examples.h"

#include "inc/hw_memmap.h"
#include "inc/hw_types.h"
#include "inc/hw_ints.h"
#include "driverlib/debug.h"
#include "driverlib/interrupt.h"
#include "driverlib/sysctl.h"
#include "driverlib/systick.h"
#include "usblib/usblib.h"
#include "usblib/usbhid.h"
#include "usblib/usbcdc.h"
#include "usblib/f2806x_usbWrapper.h"
#include "usblib/device/usbdevice.h"
#include "usblib/device/usbdcomp.h"
#include "usblib/device/usbdcdc.h"
#include "usblib/device/usbdhid.h"
#include "usblib/device/usbdhidmouse.h"
#include "usb_structs.h"

__interrupt void cpu_timer(void);
void usb_setup(void);
void spi_setup(void);

int main(void) {
	
	InitSysCtrl();
	DINT;
	InitPieCtrl();
	IER = 0x0000;
	IFR = 0x0000;
	InitPieVectTable();

	EALLOW;
	PieVectTable.TINT0 = &cpu_timer;
	EDIS;

	InitCpuTimers();
	ConfigCpuTimer(&CpuTimer0, 90, 1000000);
	CpuTimer0Regs.TCR.all = 0x4001;

	EALLOW;
	GpioCtrlRegs.GPBMUX1.bit.GPIO34 = 0;
	GpioCtrlRegs.GPBDIR.bit.GPIO34 = 1;
	EDIS;

	IER |= M_INT1;

	PieCtrlRegs.PIEIER1.bit.INTx7 = 1;

	EINT;
	ERTM;

	return 0;
}

__interrupt void cpu_timer(void){

	CpuTimer0.InterruptCount++;
	GpioDataRegs.GPBTOGGLE.bit.GPIO34 = 1;
	PieCtrlRegs.PIEACK.all = PIEACK_GROUP1;
}
