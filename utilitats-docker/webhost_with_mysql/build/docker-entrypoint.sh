#!/usr/bin/env bash

# Variables d'entorn esperades:
#  $HOSTNAME
#  $PASSWORD

# Creo l'usuari amb el mateix nom que el hostname
useradd -g sudo -ms /bin/bash $HOSTNAME || echo "User already exists."

# Canvio el password de l'usuari
echo "$HOSTNAME:$PASSWORD" | chpasswd

# Canvio el password del root
echo "root:$PASSWORD" | chpasswd

# HOSTNAME val g10 o el que toqui
mkdir -p /var/www/html/$HOSTNAME
echo "<h1>$HOSTNAME</h1>" > /var/www/html/$HOSTNAME/index.html

# Inicio apache2
service apache2 start || echo "Apache2 no s'ha pogut iniciar"

# Inicio el sshd
exec /usr/sbin/sshd -f /etc/ssh/sshd_config -e -p 22 -D