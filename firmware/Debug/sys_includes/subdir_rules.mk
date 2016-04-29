################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Each subdirectory must supply rules for building sources it contributes
sys_includes/F2806x_GlobalVariableDefs.obj: ../sys_includes/F2806x_GlobalVariableDefs.c $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: C2000 Compiler'
	"C:/ti/ccsv6/tools/compiler/ti-cgt-c2000_6.4.6/bin/cl2000" -v28 -ml -mt --float_support=fpu32 --include_path="C:/ti/ccsv6/tools/compiler/ti-cgt-c2000_6.4.6/include" --include_path="C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_common/include" --include_path="C:/ti/controlSUITE/device_support/f2806x/v150/F2806x_headers/include" --include_path="C:/ti/controlSUITE/device_support/f2806x/v150/MWare" -g --define=DEBUG --define=ccs_c2k --diag_warning=225 --diag_suppress=10063 --preproc_with_compile --preproc_dependency="sys_includes/F2806x_GlobalVariableDefs.pp" --obj_directory="sys_includes" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '


