#!/bin/bash

# Start the MySQL service
service mysql start

#sleep for 5 seconds to let mysql load
sleep 5

#create the database if it hasn't created yet.
mysql -u root < setup_mysql_dev.sql;
mysql -u root < setup_mysql_test.sql

#keep the container running
tail -f /dev/null
