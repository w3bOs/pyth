# Invoke initial libs #
import os
import pyfiglet
import traceback
import json

# Do initial tasks #
os.system('title Pyth, a Python Console, 1.1')
print(pyfiglet.Figlet(font='slant').renderText('Pyth'))
pythcfg = {'defaultTraceback': True}


# Custom Pyth Functions #
def pyexec():
    filename = input(' Drag the .py file you want to execute here > ')
    try:
        exec(open(filename).read())
    except Exception as e:
        if pythcfg['defaultTraceback'] is False:
            print(type(e).__name__ + ': ' + str(e))
        elif pythcfg['defaultTraceback'] is True:
            traceback.print_exc()


def pytraceback():
    if pythcfg['defaultTraceback'] is False:
        pythcfg['defaultTraceback'] = True
        print('Default Python Traceback changed from false to true')
    elif pythcfg['defaultTraceback'] is True:
        pythcfg['defaultTraceback'] = False
        print('Default Python Traceback changed from true to false')


def clear():
    os.system('cls')
    print(pyfiglet.Figlet(font='slant').renderText('Pyth'))


def jsonbf():
    try:
        filename = input('Drop file here > ')
        try:
            filename = ''.join(filename.split('"'))
        except:
            pass
        text = open(filename, 'r').read()
        text = json.dumps(json.loads(text), indent=4)
        open(filename, 'w').write(text)
    except Exception as e:
        if pythcfg['defaultTraceback'] is False:
            print(type(e).__name__ + ': ' + str(e))
        elif pythcfg['defaultTraceback'] is True:
            traceback.print_exc()


def jsonb():
    try:
        text = input('Input JSON code > ')
        print(json.dumps(json.loads(text), indent=4))
    except Exception as e:
        if pythcfg['defaultTraceback'] is False:
            print(type(e).__name__ + ': ' + str(e))
        elif pythcfg['defaultTraceback'] is True:
            traceback.print_exc()


def changelog():
    print('Pyth 1.1:')
    print('- Defined pytraceback() function to enable/disable the python default traceback')
    print('- Defined clear() function to clear the Screen')
    print('- Defined jsonb() function to Beauty JSON Code')
    print('- Defined jsonbf() function to Beauty JSON Code from a file')
    print('- Imported json module')
    print('- Imported traceback module')
    print()
    print('Pyth 1.0:')
    print('- Defined pyexec() function to execute external .py files')
    print('- Defined changelog() function to print historical changes of Pyth')
    print('- Included Pyth logo made in pyfiglet')
    print('- Imported pyfiglet module')
    print('- Imported os module')
    print()
    print('Pyth Beta:')
    print('- First created Pyth')


# Pyth Init #
while True:
    exp = input(' > ')
    try:
        exec(exp)
    except Exception as e:
        if pythcfg['defaultTraceback'] is False:
            print(type(e).__name__ + ': ' + str(e))
        elif pythcfg['defaultTraceback'] is True:
            traceback.print_exc()
