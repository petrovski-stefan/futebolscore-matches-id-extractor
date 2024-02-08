from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import json
import time
from tqdm import tqdm


def get_leagues() -> list[str]:
    with open('leagues.json', 'r') as f:
        data = json.load(f)
        return data['urls']


def extract_ids(matches_table: WebElement) -> list[int]:
    matches = matches_table.find_elements(By.CSS_SELECTOR, 'tr')
    matches_ids = [int(m.get_attribute('id'))
                   for m in matches if (m.get_attribute('id') != '' and m.get_attribute('id') != None)]
    return sorted(matches_ids)


def get_driver() -> Chrome:
    options = ChromeOptions()
    # comment next line when testing
    options.add_argument('--headless')
    # agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    # options.add_argument(f'--user-agent={agent}')
    options.add_argument('log-level=3')
    driver = Chrome(options=options)

    return driver


def main():
    driver = get_driver()
    leagues_urls = get_leagues()
    data = {"matches": []}

    for url in tqdm(leagues_urls, colour='green'):
        driver.get(url)
        time.sleep(1.5)
        matches_table = driver.find_element(By.CSS_SELECTOR, 'div.tdsolid')

        rounds = driver.find_elements(By.CLASS_NAME, 'lsm2')
        l_name = driver.find_element(
            By.CSS_SELECTOR, '#TitleLeft').text.split('\n')[0].strip()

        # Skipping the first round on purpose
        for r in rounds[1:]:
            r.click()
            time.sleep(1.5)

            r_no = r.text.strip()
            ids = extract_ids(matches_table)

            data['matches'].append(
                {"league_name": l_name, "round_no": r_no, "ids": ids})

            if r.get_attribute('class').endswith('round_now'):
                break

    with open('output.json', 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    main()
