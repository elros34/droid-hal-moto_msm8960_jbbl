# These and other macros are documented in dhd/droid-hal-device.inc

%define device moto_msm8960_jbbl
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Photon Q

%define installable_zip 1

%define enable_kernel_update 1

%define straggler_files \
/f2fs-fstab.qcom\
/f2fscheck.sh\
/init.class_main.sh\
/init.qcom.class_core.sh\
/init.qcom.early_boot.sh\
/init.qcom.sh\
/init.qcom.syspart_fixup.sh\
/init.qcom.usb.sh\
%{nil}

%define makefstab_skip_entries /sys/fs/pstore

%include rpm/dhd/droid-hal-device.inc
