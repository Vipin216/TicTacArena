#!/bin/bash
set -e

apt update
apt install -y python3-pip python3-venv git nginx
apt install -y awscli
cd /home/ubuntu

if [ ! -d "TicTacArena" ]; then
    git clone https://github.com/Vipin216/TicTacArena.git
fi

cd TicTacArena

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

cat > .env <<EOF
SECRET_KEY=$(aws ssm get-parameter --name "/tictacarena/SECRET_KEY" --with-decryption --query Parameter.Value --output text)

DEBUG=$(aws ssm get-parameter --name "/tictacarena/DEBUG" --query Parameter.Value --output text)

ALLOWED_HOSTS=$(aws ssm get-parameter --name "/tictacarena/ALLOWED_HOSTS" --query Parameter.Value --output text)

DB_NAME=$(aws ssm get-parameter --name "/tictacarena/DB_NAME" --query Parameter.Value --output text)

DB_USER=$(aws ssm get-parameter --name "/tictacarena/DB_USER" --query Parameter.Value --output text)

DB_PASSWORD=$(aws ssm get-parameter --name "/tictacarena/DB_PASSWORD" --with-decryption --query Parameter.Value --output text)

DB_HOST=$(aws ssm get-parameter --name "/tictacarena/DB_HOST" --query Parameter.Value --output text)

DB_PORT=$(aws ssm get-parameter --name "/tictacarena/DB_PORT" --query Parameter.Value --output text)
EOF


python manage.py migrate

python manage.py collectstatic --noinput