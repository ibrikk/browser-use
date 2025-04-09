import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://ibrikk.github.io/gui-agents-template-website1/redfin-ub.html")
        await page.screenshot(path="page.png")
        print("✅ Page loaded, screenshot saved.")
        await asyncio.sleep(5)  # Keep browser open for a few seconds
        await browser.close()

asyncio.run(main())
