from flask import Flask

from src.builder import Builder


def main():
    app: Flask = Flask(__name__)
    builder = Builder(app)
    builder.run()


if __name__ == "__main__":
    main()
