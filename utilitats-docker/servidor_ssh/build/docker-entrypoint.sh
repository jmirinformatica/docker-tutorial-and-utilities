#!/usr/bin/env bash

# Variables d'entorn esperades:
#  $ROOT_PASSWORD
#  $SSH_PORT

# Canvio el password del root
echo "root:$ROOT_PASSWORD" | chpasswd

# Inicio el sshd
exec /usr/sbin/sshd -f /etc/ssh/sshd_config -e -p $SSH_PORT -D