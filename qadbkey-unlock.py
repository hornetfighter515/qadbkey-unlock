#!/usr/bin/env python3
#
#   Original by igem, https://xnux.eu/devices/feature/qadbkey-unlock.c
#
#   Authors: hornetfighter515, FatherlyFox
#
#   P.S. Thankyou for making a functional script hornetfighter515 ❤
#
import sys
def generateUnlockKey(sn):
    """
    @param sn:  the serial number to generate an unlock key for
    """
    salt = "$1${0}$".format(sn)
    # [0:len(sn) if len(sn) < 128 else 128]
    c = crypt("SH_adb_quectel", salt)
    c = c[12:28]
    # c = c[0:16] + str(0) + c[16+1:len(c)]
    print("Salt: {0}\nCrypt: {1}".format(salt, c))
    return c

def main():
    if len(sys.argv) != 2:
        print('USAGE: ./qadbkey-unlock.py <serial>')
        print('Use \'AT+QADBKEY?\' to get serial.')
        exit(1)
    else:
        # set SN to your serial number
        c = generateUnlockKey(sys.argv[1])      
        print('AT+QADBKEY="{0}"'.format(c));
        print('AT+QCFG="usbcfg",0x2C7C,0x125,1,1,1,1,1,1,0');
        print('To disable ADB, run: (beware that modem will not be able to enter sleep with ADB enabled!!)');
        print('AT+QCFG="usbcfg",0x2C7C,0x125,1,1,1,1,1,0,0');

if __name__ == "__main__":
    try:
        from crypt import crypt
        main()
    except ImportError:
        print("This script cannot be run on Windows, 'crypt' is unsupported.")
    