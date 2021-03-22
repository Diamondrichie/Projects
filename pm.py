import os
import pprint
''' Password Manager that saves users details '''

def collect_info():
    username = input("Enter username: ")
    password = input("Enter password: ")
    website = input("Enter website: ")
    return username + ',' + password + ',' + website

def set_mode():     #finds the path and Set the mode type //Write or //Append
    if os.path.exists(filename):
        mode = 'a'
    else:
        mode = 'w'
    return open(filename, mode)

def readings():
    with open(filename, 'r') as fp:
        contents = fp.read().split('\n')[1:]
        for content in contents:
            if content:
                val = content.split(',')
                dict_ = {'username':val[0], 'password':val[1], 'website':val[2]}        
                pprint.pprint(dict_)

# def write_to_file(fp, value):
#     fp.write(value+ '\n')

write_to_file = lambda fp, value: fp.write(value+ '\n')

def write_header(fp):
    print("Writing headers")
    header = 'username\t,password\t,website'.expandtabs(2)
    write_to_file(fp, header)
    print("Finish writing headers")

def prompt():
    while True:
        val = input("""
            Are you reading(r) or writing(w) or quit(q)?
        """).lower()
        if val in ['r', 'w']:
            return val
        elif val == 'q':
            return        

def writings():
    # writing procedures
    fp = set_mode()
    if fp.mode == 'w':
        write_header(fp)
    while True:
        # write content to CSV
        value = collect_info()
        write_to_file(fp, value)
        # window to quit
        q = input('Quit? ')
        if q == 'y':
            return

def main():
    # file
    response = prompt()
    if response == 'r':
        readings()
    elif response == 'w':
        writings()

if __name__ == "__main__":
    filename = "pm.csv" 
    
    main()