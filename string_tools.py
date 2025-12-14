import re


def slugify(text: str) -> str:
    """
    turn a string into a url-friendly slug.
    """
    text = text.strip().lower()
    # replace non-alphanumeric with hyphens
    text = re.sub(r"[^a-z0-9]+", "-", text)
    # remove leading/trailing hyphens
    return text.strip("-")


def shorten(text: str, max_length: int = 120) -> str:
    """
    shorten a string to max_length characters with ellipsis.
    """
    text = text.strip()
    if len(text) <= max_length:
        return text
    return text[: max_length - 3].rstrip() + "..."


if __name__ == "__main__":
    sample = "This is a Sample Title for a Thread about Crypto Yield and Automation"
    print("slug:", slugify(sample))
    print("short:", shorten(sample, max_length=50))
