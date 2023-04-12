class Fonts:
    fonts_path: str
    fonts_size: int
    fonts_chars_limit: int

    def __init__(self, fonts_path, fonts_size, fonts_chars_limit):
        self.fonts_path = fonts_path
        self.fonts_size = fonts_size
        self.fonts_chars_limit = fonts_chars_limit
