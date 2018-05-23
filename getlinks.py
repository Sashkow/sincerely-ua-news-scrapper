import sys
from main import Site

# gathers atricle urls in "links" text file
def main(args):
    inputs = args[1:]
    print(inputs)

    # if fails, use recall.py
    for input in inputs:
        s = Site(input)
        # scrap links to articles and save to "links" text file
        s.getlinks(remember=True)




if __name__ == "__main__":
    main(sys.argv)
