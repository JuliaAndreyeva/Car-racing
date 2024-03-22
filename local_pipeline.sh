Cyan="\033[1;36m"
Blue="\033[1;34m"
NC="\033[0m"
echo -e "${Blue}Starting tests...${NC}"
pytest
echo -e "${Cyan}Tests finished${NC}"
echo -e "${Blue}Starting linting...${NC}"
flake8
echo -e "${Cyan}Linting finished${NC}"