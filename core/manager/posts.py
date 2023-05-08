from core.repository import posts as repo_posts


def get_likes_by_date_range(date_from, date_to):
    return repo_posts.get_likes_by_date_range(date_from, date_to)


def get_all_posts():
    return repo_posts.get_all_posts()
