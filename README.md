# Train Alert Process

[The story!](https://www.linkedin.com/posts/rabbitix98_%D9%85%D8%A7-%D9%87%D9%85%D9%87-%DA%86%DB%8C%D8%B2%D9%85%D9%88%D9%86%D9%88-%D8%AE%D9%88%D8%AF%D9%85%D9%88%D9%86-%D9%85%DB%8C%D8%B3%D8%A7%D8%B2%DB%8C%D9%85-%D9%87%D9%81%D8%AA%D9%87-%D9%BE%DB%8C%D8%B4-activity-7208721460696170496-EfiM?utm_source=share&utm_medium=member_desktop)

____
#### how to setup:
set your telegram bot token in utils file.


#### how to build:
```shell
docker build -t alert-process:0.0.1 .
```

#### how to deploy manually: [(link)](https://stackoverflow.com/a/26226261)
```shell
docker save alert-process:0.0.1 | bzip2 | pv | ssh  user@host docker load
```

#### how to start:

```shell
docker compose up -d
```
### and stop
```shell
docker compose down
```

 