from argparse import ArgumentParser
from importlib import import_module

interface_type = {"term", "curses"}

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("gametype")
    args = parser.parse_args()
    if args.gametype not in interface_type:
        print(f"Invalid game type: {args.gametype}")
        exit(1)
    game = import_module(f"connect4.{args.gametype}")
    game.play(args)
