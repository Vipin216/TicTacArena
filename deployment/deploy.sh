#!/bin/bash
set -e

apt update
apt install -y python3-pip python3-venv git nginx

cd /home/ubuntu

if [ ! -d "TicTacArena" ]; then
    git clone https://github.com/Vipin216/TicTacArena.git
fi

cd TicTacArena

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic --noinput