#!/usr/bin/env bash
# Set up the web server for deployment
sudo apt install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Hello World" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/test /data/web_static/releases/current/
sudo chown -hR ubuntu:ubuntu /data
sudo sed - i '/sever_name _;/a\location /hbnb_static{\n\talias /data/web_static/current/;/n/t}' /etc/nginx/sites-available/default
sudo service nginx start
sudo service nginx restart
