## By @tedixh1

import argparse
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def fetch_dmarc_domains(domain):
    """Fetch domains sharing the same DMARC record."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f'https://dmarc.live/info/{domain}')

        # Check for the presence of the 'Get All' button and click if available
        button_selector = 'button:text("Get All")'
        if await page.query_selector(button_selector):
            await page.click(button_selector)
            # Wait for any dynamic content to load after clicking the button
            await page.wait_for_load_state('networkidle')

        content = await page.content()
        await browser.close()

    soup = BeautifulSoup(content, 'html.parser')
    dmarc_domains = []
    h3_element = soup.find('h3', string=lambda text: 'Same DMARC Record' in text)

    if h3_element:
        p_sibling = h3_element.find_next_sibling('p')
        if p_sibling:
            dmarc_domains = [link.get_text(strip=True) for link in p_sibling.find_all('a')]

    return dmarc_domains

async def main(domain):
    """Main function to print domains sharing the same DMARC record."""
    domains_list = await fetch_dmarc_domains(domain)
    if not domains_list:
        print(f"No domains found for {domain}")
    else:
        print("\n".join(domains_list))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch domains with the same DMARC record.')
    parser.add_argument('-domain', required=True, help='Specify the domain to check.')
    args = parser.parse_args()

    asyncio.run(main(args.domain))
