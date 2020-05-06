def test_verify_text_message(home_page, message_page):
    home_page.click_button()
    message_page.verify_message_text()
