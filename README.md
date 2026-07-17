# 🎮 TicTacArena

A production-style real-time multiplayer Tic-Tac-Toe platform built with **Django**, **Django Channels**, **WebSockets**, and **AWS Cloud**.

TicTacArena demonstrates how to design, build, and deploy a scalable real-time backend application using modern cloud infrastructure. The application supports live multiplayer gameplay through WebSockets and is deployed across multiple EC2 instances behind an Application Load Balancer with a Redis-backed channel layer.

---

# 🚀 Project Highlights

- 🎮 Real-time multiplayer gameplay using WebSockets
- 👥 Private room creation and room-code based joining
- 🔐 User authentication and authorization
- ⚡ Django Channels for real-time communication
- 🌐 Production deployment on AWS
- 🖥 Multi-instance deployment using Amazon EC2
- ⚖️ Application Load Balancer for traffic distribution
- 📈 Auto Scaling Group for scalable infrastructure
- 🧠 Redis Channel Layer using Amazon ElastiCache (Valkey)
- 🗄 PostgreSQL hosted on Amazon RDS
- 🔁 Reverse proxy using Nginx
- 🚀 Daphne ASGI Server for WebSocket handling

---

# 🏗 System Architecture

> **Architecture diagram will be added here**


# ✨ Features

## Authentication

- User Registration
- Secure Login
- Logout
- Session-based Authentication

## Multiplayer

- Create Private Rooms
- Join Rooms using Room Code
- Real-time Game Synchronization
- Automatic Turn Management
- Win Detection
- Draw Detection
- Player Disconnect Detection

## Cloud Deployment

- Multi-instance Deployment
- Load Balancing
- Auto Scaling Ready
- Redis-backed Distributed Messaging

---

# 🛠 Technology Stack

## Backend

- Python
- Django
- Django Channels
- Daphne

## Frontend

- HTML5
- CSS3
- JavaScript

## Database

- PostgreSQL
- Amazon RDS

## Real-Time Communication

- WebSockets
- Redis Pub/Sub
- Amazon ElastiCache (Valkey)

## Web Server

- Nginx

## Cloud

- Amazon EC2
- Application Load Balancer
- Auto Scaling Group
- Amazon VPC
- Security Groups
- IAM
- Amazon RDS
- Amazon ElastiCache (Valkey)

---

# ☁ AWS Infrastructure

The application is deployed on AWS using a production-inspired architecture.

### Compute

- Amazon EC2
- Auto Scaling Group

### Networking

- Amazon VPC
- Public & Private Networking
- Security Groups
- Application Load Balancer

### Database

- Amazon RDS PostgreSQL

### Caching & Messaging

- Amazon ElastiCache (Valkey)
- Redis Channel Layer

### Reverse Proxy

- Nginx

### Application Server

- Daphne

---

# 🎮 Gameplay Flow

1. User logs into the application.
2. Player 1 creates a game room.
3. A unique room code is generated.
4. Player 2 joins using the room code.
5. Both clients establish WebSocket connections.
6. Moves are synchronized in real time.
7. Winner or draw is detected instantly.
8. Players are notified immediately.

---

# 📂 Project Structure

```text
TicTacArena/
│
├── config/
├── game/
├── users/
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

---


# ⚙ Running Locally

### Clone the repository

```bash
git clone https://github.com/yourusername/TicTacArena.git
cd TicTacArena
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Start Redis

```bash
redis-server
```

### Run Daphne

```bash
daphne config.asgi:application
```

Open

```
http://127.0.0.1:8000
```

---

# 📚 Key Concepts Demonstrated

- Django Authentication
- Django Channels
- ASGI Applications
- WebSockets
- Real-time Communication
- Redis Pub/Sub
- Distributed Messaging
- PostgreSQL
- Reverse Proxy
- AWS Cloud Deployment
- Auto Scaling
- Load Balancing
- Cloud Networking
- Production Deployment
- Multi-instance Architecture

---

# 🚧 Challenges Faced

During development, the project involved solving several real-world backend and deployment challenges:

- Configuring Django Channels with Redis.
- Deploying ASGI applications using Daphne and Nginx.
- Managing WebSocket connections through an Application Load Balancer.
- Synchronizing multiplayer events across multiple EC2 instances using Redis.
- Configuring Amazon ElastiCache as the distributed channel layer.
- Integrating Amazon RDS with multiple application servers.
- Debugging distributed deployment behavior in a cloud environment.

---

# 🔮 Future Improvements

- Matchmaking Queue
- Spectator Mode
- Friend System
- Chat System
- Player Statistics
- Match History
- ELO Rating System
- Tournament Mode
- Docker Support
- Kubernetes Deployment
- CI/CD using GitHub Actions
- CloudWatch Monitoring
- Prometheus & Grafana

---

# 👨‍💻 Author

**Vipin**

Backend Developer

### Technologies

Java • Python • Django • Django REST Framework • AWS • PostgreSQL • Redis • WebSockets
