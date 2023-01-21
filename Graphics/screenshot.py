import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import json
import re
from pathlib import Path


def get_screenshots_of_reddit_posts(reddit_thread, reddit_comments, screenshot_num: int, theme="dark"):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--force-dark-mode')

    # settings values
    W = 1080
    H = 1920

    reddit_id = re.sub(r"[^\w\s-]", "", reddit_thread.id)
    # ! Make sure the reddit screenshots folder exists
    Path(f"./Assets/temp/{reddit_id}/png").mkdir(parents=True, exist_ok=True)

    screenshot_num: int

    print("Launching Headless Browser...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    dsf = (W // 600) + 1

    # set the theme and disable non-essential cookies

    driver.get("https://www.reddit.com" + reddit_thread.permalink)
    driver.set_window_size(width=W, height=H)
    driver.add_cookie({"name": "USER",
                       "value": "eyJwcmVmcyI6eyJ0b3BDb250ZW50RGlzbWlzc2FsVGltZSI6MCwiZ2xvYmFsVGhlbWUiOiJSRURESVQiLCJuaWdodG1vZGUiOnRydWUsImNvbGxhcHNlZFRyYXlTZWN0aW9ucyI6eyJmYXZvcml0ZXMiOmZhbHNlLCJtdWx0aXMiOmZhbHNlLCJtb2RlcmF0aW5nIjpmYWxzZSwic3Vic2NyaXB0aW9ucyI6ZmFsc2UsInByb2ZpbGVzIjpmYWxzZX0sInRvcENvbnRlbnRUaW1lc0Rpc21pc3NlZCI6MH19",
                       "domain": ".reddit.com", "path": "/"})
    driver.add_cookie(
        {"name": "eu_cookie", "value": "{%22opted%22:true%2C%22nonessential%22:false}", "domain": ".reddit.com","path": "/"})

    time.sleep(5)
    postcontentpath = f"./Assets/temp/{reddit_id}/png/title.png"
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="post-content"]').screenshot(filename=postcontentpath)

    for idx, comment in enumerate(reddit_comments):

        # if driver.find_element(By.CSS_SELECTOR, '[data-testid="content-gate"]').is_displayed():
        #     driver.find_element(By.CSS_SELECTOR, '[data-testid="content-gate"] button').click()

        driver.get(f'https://reddit.com{comment.permalink}')

        try:
            driver.find_element(By.CSS_SELECTOR, f"#t1_{comment.id}").screenshot(
                filename=f"./Assets/temp/{reddit_id}/png/{idx}.png"
            )
        except TimeoutError:
            print("TimeoutError: Skipping screenshot...")
            continue

    # close browser instance when we are done using it
    driver.close()

    print("Screenshots downloaded Successfully.")