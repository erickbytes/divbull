from datetime import date
import os


def post_name():
    """Ask for the new post's name."""
    name = input("Enter the new post's title:\n")
    return name


def post_template(title):
    """Return str, post draft"""
    post = f"Title: {title} \nDate: {date.today()} 4:20 \nCategory: Essay"
    return post


def save_draft(name, post):
    """Save new post draft to content folder."""
    cwd = os.getcwd()
    content = f"{cwd}/content/blog"
    name = name.replace(" ", "-")
    md = f"{content}/{name}.md"
    try:
        with open(md, "w") as fhand:
            fhand.write(post)
    except FileNotFoundError:
        content = "/home/erickbytes/divbull/divbull.com/content/blog"
        md = f"{content}/{name}.md"
        with open(md, "w") as fhand:
            fhand.write(post)
    return None


name = post_name()
post = post_template(name)
save_draft(name, post)
