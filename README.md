# police-violence-data

sudo apt-get update
sudo apt-get install git

# git clone repo

sudo apt-get install python3-pip

sudo apt-get install libapache2-mod-wsgi-py3 apache2

sudo pip3 install -r requirements.txt

sudo cp police-violence-data.conf /etc/apache2/sites-available/police-violence-data.conf

sudo ln -sT ~/police-violence-data /var/www/html/police-violence-data

sudo a2ensite police-violence-data

sudo a2dissite 000-default

sudo service apache2 reload