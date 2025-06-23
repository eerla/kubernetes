# Docker Installation Guide

Docker lets you build, ship, and run containers. Here's how to install it:

## Windows & Mac
1. Go to [Docker Desktop download page](https://www.docker.com/products/docker-desktop/)
2. Download and install Docker Desktop for your OS.
3. Start Docker Desktop and ensure it's running (look for the whale icon).

## Linux (Ubuntu example)
```bash
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Test Docker
```bash
docker --version
docker run hello-world
```

For more, see [Docker's official install docs](https://docs.docker.com/get-docker/). 