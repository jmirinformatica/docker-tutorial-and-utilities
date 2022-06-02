sudo apt-get update

sudo apt-get install php7.4 php7.4-mysql

cd /tmp
wget https://wordpress.org/latest.tar.gz
tar -xvzf latest.tar.gz
rm latest.tar.gz
sudo mv wordpress /var/www/wordpress
sudo chown -R www-data:www-data /var/www/wordpress/
sudo chmod -R 755 /var/www/wordpress/

sudo apt-get install nano
sudo nano /etc/apache2/sites-available/000-default.conf

    apt-get install php7.4 php7.4-mysql

    # aquesta linea ja existe
    DocumentRoot /var/www/html

    # Canviar gXX pel grup que sigueu
    Alias /gXX/wordpress /var/www/wordpress
    <Directory /var/www/wordpress/>
        Options FollowSymlinks
        AllowOverride All
        Require all granted
    </Directory>

sudo service apache2 stop
sudo service apache2 start
