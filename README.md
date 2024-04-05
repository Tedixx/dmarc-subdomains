# DMARC Subdomains

## Overview
DMARC-Subdomains.py is a Python script designed to retrieve a list of domains that share the same DMARC (Domain-based Message Authentication, Reporting, and Conformance) record as a specified domain. This tool leverages the Playwright library for web automation to fetch this data from the `www.dmarc.live`, and Beautiful Soup for parsing the HTML content to extract the domain names.

## Features
- Fetches and prints a list of domains with the same DMARC record as the input domain.
- Uses asynchronous programming for efficient web scraping.
- Simple CLI for easy operation.

## Requirements
To run this script, you will need Python 3.7 or newer. The following Python packages are also required:
- `beautifulsoup4`
- `playwright`

These dependencies are listed in the `requirements.txt` file for easy installation.

## Installation

First, clone this repository or download the script to your local machine. Then, navigate to the script's directory in your terminal and run the following commands:

1. **Install dependencies:**
`pip install -r requirements.txt`

2. **Install Playwright browsers:**
`playwright install`


## Usage

To use the DMARC Domain Fetcher, run the script from the command line with the `-domain` argument followed by the domain name you wish to query. Here is an example command:

`python dmarc-subdomains.py -domain example.com`


### Output
The script will print a list of domains that share the same DMARC record as the specified domain. If no domains are found, it will output a message indicating that no domains were found for the input domain.

## Note
This script is intended for educational and ethical use only. Ensure you have permission to scrape the website and are compliant with their terms of service and any legal requirements.

## Contributing
Contributions to the DMARC Domain Fetcher are welcome. Please open an issue or pull request to suggest improvements or add new features.

## License
This script is released under the MIT License. See the LICENSE file for details.



