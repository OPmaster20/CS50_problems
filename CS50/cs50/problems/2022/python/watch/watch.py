import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    match=re.search(r'^<iframe[ ]?([a-zA_Z0-9; "=-])?[ ]?src="https?://www\.youtube.com/embed/(.+)"[ ](.+)?></iframe>$',s)
    if match:
        print(f"https://youtu.be/{match.group(2)}")


if __name__ == "__main__":
    main()
   # [ ]?\w?[ ]?\w?[ ]?\w?(;[ ])?\w?(;[ ])?\w?
  # <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0"
   # allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>