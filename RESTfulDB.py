import subprocess

# Install Docker
subprocess.run(["curl", "-sSL", "https://get.docker.com", "|", "sh"], check=True)
subprocess.run(["sudo", "usermod", "-aG", "docker", "pi"], check=True)

# Install Docker Compose
subprocess.run(["sudo", "apt", "install", "-y", "libffi-dev", "libssl-dev", "python3-dev", "python3", "python3-pip"], check=True)
subprocess.run(["sudo", "apt", "remove", "-y", "python-configparser"], check=True)
subprocess.run(["sudo", "pip3", "install", "docker-compose"], check=True)

# Create a directory for Home Assistant
subprocess.run(["mkdir", "homeassistant"], check=True)
subprocess.run(["cd", "homeassistant"], check=True)

# Create a Docker Compose file
compose_file_content = """
version: '3'
services:
  homeassistant:
    container_name: home-assistant
    image: homeassistant/raspberrypi4-homeassistant:stable
    volumes:
      - ./config:/config
    restart: always
    network_mode: host
"""

with open("docker-compose.yml", "w") as f:
    f.write(compose_file_content)

# Start the Home Assistant container
subprocess.run(["docker-compose", "up", "-d"], check=True)

print("Home Assistant has been installed and started. You can access it at http://localhost:8123")
