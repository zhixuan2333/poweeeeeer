# Poweeeeeeeeeer tool

## What does poweeeer do.

- reverse color of file and directory (form every image to png)
- convert pdf to svg

## Quick start

Python何もわからない人はこれ。 I can use python [come here](#advance).
```sh
git clone https://github.com/zhixuan2333/poweeeeeer
cd poweeeeeer

pip install -r requirements.txt
./poweeeeer.py --help
```

### With Docker

```
docker run --rm -it -v $(pwd):/mnt/data ghcr.io/zhixuan2333/poweeeeeer:latest
```


### Advance
Make a python env.

```sh
git clone https://github.com/zhixuan2333/poweeeeeer
cd poweeeeeer

conda create -n <env_name> python==3.12
conda activate <env_name>
pip install -r requirements.txt
```

> If you are using linux or macos.
```sh
chmod +x ./poweeeeer.py
```

### Run

```sh
./poweeeeer.py --help
```

## Revision

### 2024-12-16
- Change reverse command to output every image to `.png`
- 🎉 Support convert pdf to svg

### 2024-11-14
- Init all project
- 🎉 Support reverse color with file
- 🎉 Support reverse color with directory