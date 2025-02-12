import importlib.metadata

__version__ = importlib.metadata.version("gha_release_demo_pkg")

if __name__ == "__main__":
    print(__version__)
