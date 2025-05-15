#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo "Checking prerequisites for Flask Blog Platform..."

# Check if Docker is installed
if command -v docker &> /dev/null; then
    echo -e "${GREEN}✓ Docker is installed${NC}"
else
    echo -e "${RED}✗ Docker is not installed. Please install Docker first.${NC}"
    echo -e "${YELLOW}Visit https://docs.docker.com/get-docker/ for installation instructions.${NC}"
    exit 1
fi

# Check if Docker Compose is installed
if command -v docker-compose &> /dev/null; then
    echo -e "${GREEN}✓ Docker Compose is installed${NC}"
else
    echo -e "${RED}✗ Docker Compose is not installed. Please install Docker Compose first.${NC}"
    echo -e "${YELLOW}Visit https://docs.docker.com/compose/install/ for installation instructions.${NC}"
    exit 1
fi

# Check if Python is installed
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}✓ Python is installed${NC}"
else
    echo -e "${RED}✗ Python is not installed. Please install Python first.${NC}"
    echo -e "${YELLOW}Visit https://www.python.org/downloads/ for installation instructions.${NC}"
    exit 1
fi

# Check if pip is installed
if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}✓ pip is installed${NC}"
else
    echo -e "${RED}✗ pip is not installed. Please install pip first.${NC}"
    echo -e "${YELLOW}You can install pip by running: python3 -m ensurepip --upgrade${NC}"
    exit 1
fi

# Check if PostgreSQL client is installed
if command -v psql &> /dev/null; then
    echo -e "${GREEN}✓ PostgreSQL client is installed${NC}"
else
    echo -e "${YELLOW}! PostgreSQL client is not installed locally.${NC}"
    echo -e "${YELLOW}This is not required as PostgreSQL will run in Docker, but you may want to install it for local development.${NC}"
fi

echo -e "\n${GREEN}All prerequisites are satisfied!${NC}"
echo -e "You can now run the application using: docker-compose up --build"

exit 0
