#!/usr/bin/env python3
"""Entry for make.fun bounty: One Line, Lights Out

A tiny one-liner joke program. Run it and it prints the joke.
"""

JOKE = "Lights out. The server is sleeping. Do not wake it. It dreams in error messages."


def tell_joke():
    """Return the one-line joke for this bounty."""
    return JOKE


def main():
    print(tell_joke())


if __name__ == "__main__":
    main()
