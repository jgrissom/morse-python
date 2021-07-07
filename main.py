import uasyncio as asyncio
from machine import Pin
from async_switch import Switch
from internal import TinyPICODotStar

def dot():
    print('.')
    t1 = asyncio.create_task(dotstar.async_flicker((191,64,191,.5), .1))
    
def dash():
    print('-')
    t1 = asyncio.create_task(dotstar.async_flicker((191,64,191,.5), .2))

async def main():
    btn_red.close_func(dot)
    btn_green.close_func(dash)
    while True:
        await asyncio.sleep(.01)

if __name__ == "__main__":
    try:
        btn_red = Switch( Pin(18, Pin.IN, Pin.PULL_UP) )
        btn_green = Switch( Pin(5, Pin.IN, Pin.PULL_UP) )
        dotstar = TinyPICODotStar()
        dotstar.off()
        asyncio.run(main())
    finally:
        print('goodbye')
        dotstar.kill()
