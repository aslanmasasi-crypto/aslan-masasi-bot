name: AslanMasasiBot
on:
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with: {python-version: '3.9'}
      - run: pip install instagrapi
      - run: python main.py
        env:
          INSTA_USER: ${{ secrets.INSTA_USER }}
          INSTA_PASS: ${{ secrets.INSTA_PASS }}
