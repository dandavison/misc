# mysql.server start    # Start server
# mysqladmin -u root -p # Set root password
# echo "create user '$USER'@'localhost' identified by '$USER-password'" | mysql -u root --password=root-password
echo "grant all privileges on * . * to '$USER'@'localhost'" | MYSQL_PWD=root-password mysql -u root
export MYSQL_PWD=ddavison-password
