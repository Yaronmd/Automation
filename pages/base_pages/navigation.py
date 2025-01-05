from pages.base_pages.base_page import SeleniumBasePage


class Navigation(SeleniumBasePage):
    def go_to_end_point(self, url: str) -> bool:
        try:
            self.driver.get(url)
            return True
        except Exception as e:
            self.logger.error(f"Failed to navigate to {url}: {e}")
            return False