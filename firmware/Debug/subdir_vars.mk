################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CMD_SRCS += \
C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/cmd/F28069.cmd \
C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_headers/cmd/F2806x_Headers_nonBIOS.cmd 

LIB_SRCS += \
C:/ti/controlSUITE/device_support/f2806x/v150/MWare/driverlib/Debug/driverlib.lib \
C:/ti/controlSUITE/device_support/f2806x/v150/MWare/lib/usblib.lib 

ASM_SRCS += \
C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_CodeStartBranch.asm \
C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_usDelay.asm 

C_SRCS += \
C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_DefaultIsr.c \
C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_PieCtrl.c \
C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_PieVect.c \
../main.c \
C:/ti/controlSUITE/device_support/f2806x/v150/MWare/driverlib/sysctl.c \
C:/ti/controlSUITE/device_support/f2806x/v150/MWare/driverlib/usb.c \
../usb_serial_structs.c 

OBJS += \
./F2806x_CodeStartBranch.obj \
./F2806x_DefaultIsr.obj \
./F2806x_PieCtrl.obj \
./F2806x_PieVect.obj \
./F2806x_usDelay.obj \
./main.obj \
./sysctl.obj \
./usb.obj \
./usb_serial_structs.obj 

ASM_DEPS += \
./F2806x_CodeStartBranch.pp \
./F2806x_usDelay.pp 

C_DEPS += \
./F2806x_DefaultIsr.pp \
./F2806x_PieCtrl.pp \
./F2806x_PieVect.pp \
./main.pp \
./sysctl.pp \
./usb.pp \
./usb_serial_structs.pp 

C_DEPS__QUOTED += \
"F2806x_DefaultIsr.pp" \
"F2806x_PieCtrl.pp" \
"F2806x_PieVect.pp" \
"main.pp" \
"sysctl.pp" \
"usb.pp" \
"usb_serial_structs.pp" 

OBJS__QUOTED += \
"F2806x_CodeStartBranch.obj" \
"F2806x_DefaultIsr.obj" \
"F2806x_PieCtrl.obj" \
"F2806x_PieVect.obj" \
"F2806x_usDelay.obj" \
"main.obj" \
"sysctl.obj" \
"usb.obj" \
"usb_serial_structs.obj" 

ASM_DEPS__QUOTED += \
"F2806x_CodeStartBranch.pp" \
"F2806x_usDelay.pp" 

ASM_SRCS__QUOTED += \
"C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_CodeStartBranch.asm" \
"C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_usDelay.asm" 

C_SRCS__QUOTED += \
"C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_DefaultIsr.c" \
"C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_PieCtrl.c" \
"C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/source/F2806x_PieVect.c" \
"../main.c" \
"C:/ti/controlSUITE/device_support/f2806x/v150/MWare/driverlib/sysctl.c" \
"C:/ti/controlSUITE/device_support/f2806x/v150/MWare/driverlib/usb.c" \
"../usb_serial_structs.c" 


