# Install Python packages
python -m pip install alive-progress python-whois shodan python-nmap

# Additional Python packages
python -m pip install requests
python -m pip install beautifulsoup4
python -m pip install pandas
python -m pip install numpy

# Ensure nmap is installed on the system
if ! command -v nmap &> /dev/null
then
    echo "nmap could not be found, please install it from https://nmap.org/download.html"
    exit
fi

echo "All requirements installed successfully."