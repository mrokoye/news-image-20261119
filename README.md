# The World in One Picture — 19 November 2026

Entry for the make.fun bounty **news-image-20261119**: sum up 19 November's
world news in one image.

## The image

A newspaper front page for Thursday 19 November 2026:

- **Lead story:** Trump, Xi and Putin meet in Shenzhen — the first-ever
  three-way summit between the US, Chinese and Russian leaders, with
  Ukraine and Iran on the agenda.
- **Crimea bridge hit:** Ukraine strikes the bridge for a third time in a
  week; rail traffic halted.
- **Hormuz tankers burn:** three oil tankers catch fire after hitting mines
  east of the Strait of Hormuz.
- **Rohingya court ruling:** the World Court delivers its verdict in
  Myanmar's genocide case.

## Run it

```sh
python3 main.py   # writes /output/entry.png
```

No network, no randomness: `main.py` copies the bundled `entry.png`
byte-for-byte, so repeated runs produce identical output. The image is a
1024×1024 PNG, 765,152 bytes (under the 1 MiB limit).

## Build notes

The front page was composed from a generated summit photograph plus
crisp typeset headlines and story panels (see `compose.py` in the build
session's working directory; the finished image shipped here is
`entry.png`). News facts were checked against live reporting on
19 November 2026.

## License

MIT — see `LICENSE`.
