import os
import sys

# ----------------
# input arguments
# ----------------
# -create, create containers

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]   

# if -create input argument, create containers
if(argument == '-create'):
    # mySQL
    # create('docker run -d -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=MyNewPass mysql/mysql-server:latest-aarch64', 'mysql')
    # mongoDB
    create('docker run -p 27017:27017 --network MBTANetwork --name some-mongo -d mongo','mongoDB')
    # # redis
    # create('docker run -p 6379:6379 --name some-redis -d redis','redis')
    # # Cassandra
    # create('docker run -p 9042:9042 --name some-cassandra -d cassandra','Cassandra')

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# if -delete input argument, delete 'named'containers
if(argument == '-delete'):
    delete('some-mysql')
    delete('some-mongo')
    delete('some-redis')
    delete('some-cassandra')