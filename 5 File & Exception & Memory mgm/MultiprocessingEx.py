
  
import multiprocessing

def sq(n):
    return n**2

if __name__ =="__main__":
    with multiprocessing.Pool(processes=3) as pool:
        op = pool.map(sq, [1,2,3,4,5,6])
    print(op)

