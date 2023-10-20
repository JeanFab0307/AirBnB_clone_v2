#!/usr/bin/env bash
# Set up the web server for deployment
sudo apt install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Hello World" > /data/web_static/releases/test/index.html
ln -f /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed - i '//a\location /hbnb_static{\n\talias /data/web_static/current' /etc/nginx/nginx.conf
sudo service start nginx
sudo service restart nginx