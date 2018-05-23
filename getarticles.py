# for each url in links parse articles for metadata and upload to elastic search
# uses domain of the last site
# does not take arguments
from main import Site
def main():
    s = Site('memory')
    s.getarticles()

if __name__ == "__main__":
    main()
