import eventlet
import time

# https://qiita.com/ttsubo/items/9afbbfe07be928c3d47b

def _sample_processing():
    print("aaa")
    for i in range(5):
        print(i)
        time.sleep(1)
    print("finish")

def main():
    opthread = eventlet.spawn(_sample_processing)
    opthread.wait()
if __name__=="__main__":
    print("test!!")
    