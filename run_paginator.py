from page_class import Pagination

pag = list('abcdefgefghdsadsdawszvafwafaf')

if __name__ == '__main__':
    paginator = Pagination(pag, 5)
    paginator.last_page()
    paginator.get_current_page()
    paginator.get_visible_items()
    paginator.prev_page()
    paginator.prev_page()
    paginator.get_visible_items()
    paginator.get_current_page()
    paginator.go_to_page(3)
    paginator.get_visible_items()
    paginator.get_current_page()