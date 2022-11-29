import math
from typing import List, Optional, Any


class Pagination:
    def __init__(self, items: List[Any] = '', page_size: Optional[int] = 10):
        self.items = items
        self.page_size = page_size
        self.now_page = 1
        self.max_pages = math.ceil(len(self.items) / page_size)

    def get_visible_items(self):
        visible_items = self.items[((self.now_page - 1) * self.page_size):(self.now_page * self.page_size)]
        print(visible_items)

    def next_page(self):
        if 0 < self.now_page < self.max_pages:
            self.now_page += 1
        else:
            pass

    def prev_page(self):
        if 1 < self.now_page < self.max_pages + 1:
            self.now_page -= 1
        else:
            pass

    def first_page(self):
        self.now_page = 1

    def last_page(self):
        self.now_page = self.max_pages

    def go_to_page(self, pg: int):
        if pg < 1:
            self.now_page = 1
        elif pg > self.max_pages:
            self.now_page = self.max_pages
        else:
            self.now_page = pg

    def get_current_page(self):
        print(self.now_page)

    def get_page_size(self):
        print(self.page_size)

    def get_items(self):
        print(self.items)