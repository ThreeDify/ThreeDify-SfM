# ThreeDify-SfM

A simple SfM pipeline for ThreeDify.

[![Lint](https://github.com/ThreeDify/ThreeDify-SfM/workflows/Lint%20Check/badge.svg)](https://github.com/silwalanish/ThreeDify-SfM/actions)

# What's ThreeDify?

ThreeDify is a online platform where you can upload images and create a 3D reconstruction of the images.

## Environment Variables

| Variable                      | Description                                      |
| ----------------------------- | ------------------------------------------------ |
| BASE_URL                      | API base url e.g. http://localhost               |

# Setup
1. Install `python-3.8` and `pip`.
2. Install requirements.

```bash
$ pip install -e .[dev]
```

3. Create `.env` file

```
$ cp .env.example .env
```

## Run

```bash
$ python src/main.py
```

## Lint

Check lint errors.

```bash
$ pylint src
```

Fix format.

```bash
$ black src
```
