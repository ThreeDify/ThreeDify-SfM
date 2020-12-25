# ThreeDify-SfM

A simple SfM pipeline for ThreeDify.

[![Lint](https://github.com/ThreeDify/ThreeDify-SfM/workflows/Lint%20Check/badge.svg)](https://github.com/silwalanish/ThreeDify-SfM/actions)

# What's ThreeDify?

ThreeDify is a online platform where you can upload images and create a 3D reconstruction of the images.

## Environment Variables

| Variable                      | Description                                      |
| ----------------------------- | ------------------------------------------------ |
| API_BASE_URL                  | API base url e.g. http://localhost               |
| SFM_IMPLEMENTATION            | SfM implementation to use. (OPENSFM/THREEDIFY)   |
| APP_ID                        | App ID for ThreeDify api.                        |
| APP_SECRET                    | App secret for ThreeDify api.                    |

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

4. Setup OpenSfM. [Docs](https://www.opensfm.org/docs/building.html)

## Run

```bash
$ python src/main.py
```

## Run with Docker

1. Setup Docker.

2. Build image.

```
$ docker build --target=main -t threedify_sfm .
```

3. Run

```
$ docker run --env-file=.env threedify_sfm
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

Check lint and format errors with docker.

```bash
$ docker build --target=lint -t threedify_sfm_lint .
$ docker run threedify_sfm_lint
```
