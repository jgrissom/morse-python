import uasyncio as asyncio
from machine import Pin
from async_switch import Switch
from internal import TinyPICODotStar
from output import Output

MORSE_CODE = {
    '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H',
    '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P',
    '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X',
    '-.--':'Y', '--..':'Z', '.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5',
    '-....':'6', '--...':'7', '---..':'8', '----.':'9', '-----':'0', '--..--':',', '.-.-.-':'.',
    '..--..':'?', '-..-.':'/', '-....-':'-', '-.--.':'(', '-.--.-':')'}

def dot():
    morse.append('.')
    print(morse)
    t1 = asyncio.create_task(dotstar.async_flicker((191,64,191,.5), .1))
    
def dash():
    morse.append('-')
    print(morse)
    t1 = asyncio.create_task(dotstar.async_flicker((191,64,191,.5), .2))

def decode():
    morse_str = ''.join(map(str, morse))
    if morse_str in MORSE_CODE.keys():
        print(MORSE_CODE[morse_str])
    else:
        print('Invalid')
    morse.clear()

async def main():
    btn_red.close_func(dot)
    btn_green.close_func(dash)
    btn_blue.close_func(decode)
    while True:
        await asyncio.sleep(.01)

if __name__ == "__main__":
    try:
        btn_red = Switch( Pin(18, Pin.IN, Pin.PULL_UP) )
        btn_green = Switch( Pin(5, Pin.IN, Pin.PULL_UP) )
        btn_blue = Switch( Pin(22, Pin.IN, Pin.PULL_UP) )
        dotstar = TinyPICODotStar()
        dotstar.off()
        morse = []
        asyncio.run(main())
    finally:
        print('goodbye')
        dotstar.kill()
