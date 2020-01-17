from zipfile import ZipFile
from os import system, path, getcwd
from subprocess import call

def get_kit():
    system('cls')
    print ("\n \nSelect kit:")

    kits = [
        {
            "name" : "Flask Server",
            "path" : "kits/flask_server.zip"  
        },
        
        {
            "name" : "Also Flask Server",
            "path" : "kits/flask_server.zip"  
        }
    ]

    for id, kit in enumerate(kits, start=1):
        print (f'{id}. {kit["name"]}')

    try:
        sel = int(input())
        return kits[sel]["path"]
    except ValueError:
        print("Bad selection. Enter to try again.")
        input()
        return get_kit()

def get_path():
    system('cls')
    print ("\nEnter path to build new project.")
    new_project_path = input()
    if path.exists(new_project_path):
        return(new_project_path)
    else:
        print("The path does not exist. Enter to try again.")
        input()
        return get_path()

if __name__ == "__main__":
    
    system('cls')
    print("""
  _____            _        _     _                            _     
 |  __ \          | |      | |   | |                          | |               /\      
 | |__) |___   ___| | _____| |_  | |     __ _ _   _ _ __   ___| |__            (  )     
 |  _  // _ \ / __| |/ / _ \ __| | |    / _` | | | | '_ \ / __| '_ \           (  )     
 | | \ \ (_) | (__|   <  __/ |_  | |___| (_| | |_| | | | | (__| | | |         /|/\|\    
 |_|  \_\___/ \___|_|\_\___|\__| |______\__,_|\__,_|_| |_|\___|_| |_| v 1.0  /_||||_\   

By Acey

Enter to start.
""")
    input()
    k = get_kit()
    kit_path = path.join(getcwd(), k)
    project_path = get_path()

    try: 
        with ZipFile(kit_path, 'r') as zip:
            zip.extractall(project_path)
        wd = str(project_path + "\\activation.py")
        print("Done. \nNow running kit's activation script.")
        call(f'python "{wd}"', shell=True)

    except Exception as e:
        print(e)