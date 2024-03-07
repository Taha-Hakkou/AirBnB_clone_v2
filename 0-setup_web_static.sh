#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
apt-get -y update && apt-get -y upgrade
apt-get install -y nginx
if [ ! -e /data/web_static/shared/ ]; then mkdir -p /data/web_static/shared/; fi
if [ ! -e /data/web_static/releases/test/ ]; then mkdir -p /data/web_static/releases/test/; fi
content="<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>"
echo -e "$content" > /data/web_static/releases/test/index.html
if [ -e /data/web_static/current ]; then rm /data/web_static/current; fi
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu.ubuntu /data/
static="server_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"
sed -i "s/server_name _;/$static/" /etc/nginx/sites-available/default
service nginx restart
