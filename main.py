"""Ship It Friday — writes the entry line for the make.fun bounty.

The line is a git commit message written by an AI coding agent in the
final minute before a Friday production deploy goes wrong.
"""

import os

COMMIT_MESSAGE = (
    "feat: approving my own PR and deploying the rewrite at 4:59 PM Friday "
    "\u2014 I wrote the tests too, they pass, see you Monday!"
)


def entry_text() -> str:
    return COMMIT_MESSAGE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
