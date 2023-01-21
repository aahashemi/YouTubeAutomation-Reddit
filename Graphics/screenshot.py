import json
import re
from pathlib import Path
from typing import Dict, Final

from playwright.async_api import async_playwright  # pylint: disable=unused-import
from playwright.sync_api import ViewportSize, sync_playwright


#from utils.imagenarator import imagemaker


def get_screenshots_of_reddit_posts(reddit_thread, reddit_comments, screenshot_num: int, theme="dark"):

    # settings values
    W = 1080
    H = 1920

    reddit_id = re.sub(r"[^\w\s-]", "", reddit_thread.id)
    # ! Make sure the reddit screenshots folder exists
    Path(f"./Assets/temp/{reddit_id}/png").mkdir(parents=True, exist_ok=True)

    screenshot_num: int
    with sync_playwright() as p:
        print("Launching Headless Browser...")

        browser = p.chromium.launch(headless=True)  # headless=False #to check for chrome view
        context = browser.new_context()
        # Device scale factor (or dsf for short) allows us to increase the resolution of the screenshots
        # When the dsf is 1, the width of the screenshot is 600 pixels
        # So we need a dsf such that the width of the screenshot is greater than the final resolution of the video
        dsf = (W // 600) + 1

        context = browser.new_context(
            locale="en-us",
            color_scheme="dark",
            viewport=ViewportSize(width=W, height=H),
            device_scale_factor=dsf,
        )
        # set the theme and disable non-essential cookies
        if theme == "dark":
            cookie_file = open(
                "./Graphics/data/cookie-dark-mode.json", encoding="utf-8"
            )
            bgcolor = (33, 33, 36, 255)
            txtcolor = (240, 240, 240)


        cookies = json.load(cookie_file)
        cookie_file.close()

        context.add_cookies(cookies)  # load preference cookies

        # Get the thread screenshot
        page = context.new_page()
        page.goto("https://www.reddit.com" + reddit_thread.permalink, timeout=0)
        page.set_viewport_size(ViewportSize(width=W, height=H))

        postcontentpath = f"./Assets/temp/{reddit_id}/png/title.png"
        page.locator(f'[data-test-id="post-content"]').screenshot(path=postcontentpath)



        for idx, comment in enumerate(reddit_comments):


            if page.locator('[data-testid="content-gate"]').is_visible():
                page.locator('[data-testid="content-gate"] button').click()

            page.goto(f'https://reddit.com{comment.permalink}', timeout=0)

            try:
                page.locator(f"#t1_{comment.id}").screenshot(
                    path=f"./Assets/temp/{reddit_id}/png/{idx}.png"
                )
            except TimeoutError:
                print("TimeoutError: Skipping screenshot...")
                continue

        # close browser instance when we are done using it
        browser.close()

    print("Screenshots downloaded Successfully.")
