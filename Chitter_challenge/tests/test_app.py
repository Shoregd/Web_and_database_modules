from playwright.sync_api import Page, expect

def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    expect(page.locator("h2")).to_have_text("Chitter Posts")
    p_tags = page.locator('p')
    expect(p_tags).not_to_have_text('Sign out.')

def test_sign_in_takes_user_to_sign_in_form(page,test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click('text=Sign in!')
    h1_tag = page.locator('.t-title')
    expect(h1_tag).to_have_text('Sign in')

def test_user_can_sign_in_and_main_page_updates(page,test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click('text=Sign in!')
    page.fill('input[name=username]','Twizzle')
    page.fill('input[name=user_email]','terrywizzles@gmail.com')
    page.click('text=Sign in.')
    checkuser = page.locator('.t-current_user')
    expect(checkuser).to_have_text('Signed in as Twizzle')

def test_user_can_sign_out_and_returns_to_main_page_signed_out(page,test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click('text=Sign in!')
    page.fill('input[name=username]','Twizzle')
    page.fill('input[name=user_email]','terrywizzles@gmail.com')
    page.click('text=Sign in.')
    page.click('text=Sign out.')
    expect(page.locator("h2")).to_have_text("Chitter Posts")
    p_tags = page.locator('p')
    expect(p_tags).not_to_have_text('Sign out.')

def test_user_can_sign_up_and_main_page_updates(page,test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click('text=Sign up!')
    page.fill('input[name=username]','Twizzles')
    page.fill('input[name=user_email]','terrywizzle@gmail.com')
    page.click('text=Sign up.')
    checkuser = page.locator('.t-current_user')
    expect(checkuser).to_have_text('Signed in as Twizzles')

def test_user_can_app_peep_while_signed_in(page,test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click('text=Sign in!')
    page.fill('input[name=username]','Twizzle')
    page.fill('input[name=user_email]','terrywizzles@gmail.com')
    page.click('text=Sign in.')
    page.screenshot(path="screenshot.png", full_page=True)
    page.fill('textarea[name=message]','This is a test message.')
    page.click('text=Post.')
    user_locator = page.locator('.t-username')
    message_locator = page.locator('.t-usermessage')
    expect(user_locator).to_have_text('Twizzle')
    expect(message_locator).to_have_text('This is a test message.')

    
