#!/bin/bash

SOC_PREFIX=$PREFIX/lib/python3.5/site-packages/artiq/binaries/kc705-nist_qc2
mkdir -p $SOC_PREFIX

V=1 $PYTHON -m artiq.gateware.targets.kc705_dds -H nist_qc2
cp misoc_nist_qc2_kc705/gateware/top.bit $SOC_PREFIX
cp misoc_nist_qc2_kc705/software/bootloader/bootloader.bin $SOC_PREFIX
cp misoc_nist_qc2_kc705/software/runtime/runtime.{elf,fbi} $SOC_PREFIX
