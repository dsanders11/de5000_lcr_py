import argparse
import time
import datetime

import serial

from de5000_lcr import DE5000


def main(port, interval):
    print("Starting DE-5000 monitor...")
    exit_code = 0

    try:
        lcr = DE5000(port)

        while True:
            print("")
            print(datetime.datetime.now())
            lcr.pretty_print(disp_norm_val=True)

            time.sleep(interval)
    except serial.SerialException:
        print("Serial port error.")
        exit_code = 1
    except KeyboardInterrupt:
        print("")
        print("Exiting DE-5000 monitor.")

    return exit_code


def commandline():
    parser = argparse.ArgumentParser(
        description="Monitor DE-5000 serial output")
    parser.add_argument('--serial', dest='serial_port', action='store',
                        default='/dev/ttyUSB0',
                        help="Serial port to use (default: /dev/ttyUSB0)")
    parser.add_argument('--interval', dest='interval', action='store',
                        default=1.0, type=float,
                        help="Polling interval, in seconds (default: 1.0)")

    args = parser.parse_args()

    return main(args.serial_port, args.interval)
