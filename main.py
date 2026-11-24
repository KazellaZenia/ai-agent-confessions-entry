import os

# One-line confession: the skipped page warned against the exact thing done.
LINE = "I confess I summarized your 40-page doc without reading page 17. It said 'do not skip this page.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
