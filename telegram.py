from playwright.sync_api import sync_playwright
import schedule
import time

def send_telegram_message():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Open Telegram Web
        page = context.new_page()
        page.goto("https://web.telegram.org/")

        print("⚠️ Login manually with QR code or session once")

        input("✅ Press Enter after logging in...")

        # Search for a contact or group
        page.locator('//div[@class="input-field-border"]/preceding::input').fill('mom')
        time.sleep(0.5)
        page.locator('(//div[contains(@class, "search-group")]//ul//a)[1]').click()
        # page.keyboard.press("Enter")
        time.sleep(1)

        # Type and send the message
        page.locator('//div[contains(@class, "new-message")]//span[text()="Message"]').click()
        page.keyboard.type('Hello from Playwright bot!')
        # page.keyboard.press("Enter")

        print("✅ Message sent!")

        browser.close()

    # ⏰ Schedule the bot to run daily at 09:00 AM
    schedule.every().day.at("09:00").do(send_telegram_message)

    print("🕒 Bot scheduler is running. Waiting for 09:00 AM daily trigger...")
    while True:
        schedule.run_pending()
        time.sleep(1)
send_telegram_message()