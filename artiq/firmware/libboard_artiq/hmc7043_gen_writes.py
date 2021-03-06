#!/usr/bin/env python3

# The HMC7043 GUI exports register write lists into Python files.
# This script converts them into Rust arrays.

import sys
import runpy


class DUT:
    def __init__(self):
        self.writes = []

    def write(self, address, value):
        self.writes.append((address, value))


def main():
    dut = DUT()
    runpy.run_path(sys.argv[1], {"dut": dut})

    print("// This file was autogenerated by hmc7043_gen_writes.py")
    print("const HMC7043_WRITES: [(u16, u8); {}] = [".format(len(dut.writes)))
    for address, value in dut.writes:
        print("    (0x{:04x}, 0x{:02x}),".format(address, value))
    print("];")


if __name__ == "__main__":
    main()
