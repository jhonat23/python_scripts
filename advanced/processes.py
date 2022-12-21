#importaciones
import os
import asyncio
from multiprocessing import Pool
from multiprocessing import Process

# Scripts para entender como funciona la programación asíncrona
async def test():
    print('Esto debe de llegar')

async def run():
    await test()

asyncio.run(run())

#Multiprocessing
def f(x):
    return x*x

def fa(name):
    print('hello', name)

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

        info('main line')
        p = Process(target=fa, args=('bob',))
        p.start()
        p.join()