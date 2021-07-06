import uasyncio as asyncio
from machine import Pin
from async_switch import Switch

def dot():
    print('.')
    
def dash():
    pass

async def main():
    btn_red.close_func(dot)
    while True:
        await asyncio.sleep(.01)

if __name__ == "__main__":
    try:
        btn_red = Switch( Pin(18, Pin.IN, Pin.PULL_UP) )
        asyncio.run(main())
    finally:
        print('goodbye')
