#!/usr/bin/env python3
from i2c_pkg.emc2301_pkg import emc2301

def get_speed(fan):
    speedRaw = fan.read_register('FAN_SETTING')
    speed = speedRaw/255*100
    rpm = fan.speed()[0]
    print(f'Speed Pecentage = {speed}, Speed RPM = {rpm}')

def set_speed(fan):
    speed = int(input("enter speed in percentage 1-100: ").strip())
    fan.write_register('FAN_SETTING', int(speed/100*255))

if __name__ == '__main__':
    fan = emc2301.EMC2301(busnum=10)
    cmd = None
    if fan.self_test() != 0 :
        while cmd != 0:
            cmd = int(input("""
            menu
            ----
            (0). exit
            (1). get speed
            (2). set speed
            """).strip())

            if cmd == 0:
                pass
            elif cmd == 1:
                get_speed(fan)
            elif cmd == 2:
            else:
                print('invalid cmd={}'.format(cmd))

            print('================================')


