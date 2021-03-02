import os
import shutil
from subprocess import Popen, PIPE, STDOUT, call
import time

# N is number of clients
N = 1

# Test File Load Sizes
TEST_LOAD_SIZES = [128,512,2000,8000,32000]

# Get parent directory
PARENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Create server directory
def create_server():
    if not os.path.exists(f"{PARENT_DIR}/../server"):
        os.mkdir(f"{PARENT_DIR}/../server")
    if not os.path.exists(f"{PARENT_DIR}/../server/watch_folder"):
        os.mkdir(f"{PARENT_DIR}/../server/watch_folder")

    shutil.copyfile(f"{PARENT_DIR}/config.json", f"{PARENT_DIR}/../server/config.json")
    shutil.copyfile(f"{PARENT_DIR}/server.py", f"{PARENT_DIR}/../server/server.py")

# Create N client directories
def create_clients():
    for i in range(N):
        if not os.path.exists(f"{PARENT_DIR}/../client_{i}"):
            os.mkdir(f"{PARENT_DIR}/../client_{i}")
        if not os.path.exists(f"{PARENT_DIR}/../client_{i}/download_folder"):
            os.mkdir(f"{PARENT_DIR}/../client_{i}/download_folder")

        shutil.copyfile(f"{PARENT_DIR}/config.json", f"{PARENT_DIR}/../client_{i}/config.json")
        shutil.copyfile(f"{PARENT_DIR}/client.py", f"{PARENT_DIR}/../client_{i}/client.py")

# Delete server directory
def delete_server():
    shutil.rmtree(f"{PARENT_DIR}/../server")

# Delete N client directories
def delete_clients():
    for i in range(N):
        shutil.rmtree(f"{PARENT_DIR}/../client_{i}")

# Create test loads in server
def create_test_loads():
    for size in TEST_LOAD_SIZES:
        f = open(f"{PARENT_DIR}/../server/watch_folder/load_{size}","w")
        for i in range(size):
            if i % 10000 == 0:
                f.write('\n')
            else:
                f.write("b")
        f.close()

# automate downloads and timeit
def automate():
    server_process = Popen(['python','server.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE, cwd=f"{PARENT_DIR}/../server")

    client_processes = [None for _ in range(N)]
    for i in range(N):
        client_processes[i] = Popen(['python','client.py','Mr.{i}','get_files_list','get_files_list'], stdout=PIPE, stdin=PIPE, stderr=PIPE, cwd=f"{PARENT_DIR}/../client_{i}")
        ret = client_processes[i].communicate(input="".encode())[0]
        print(ret)
        # eee = client_processes[i].communicate(input=f"help".encode())[0]
        # print(eee)


if __name__ == "__main__":
    
    try:
        N = int(input("Number of clients: "))
        
        if N <= 0:
            print("Input must be 1 or higher.")
    except:
        print("Input is not a number.")
    
    create_server()
    create_clients()
    create_test_loads()

    automate()
    # delete_server()
    # delete_clients()
