import uasyncio as asyncio

def dot():
    pass
    
def dash():
    pass

async def main():
    while True:
        await asyncio.sleep(.01)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        print('goodbye')
