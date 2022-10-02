
# Creating NFTs Seasons

## Prerequsites

 - Python3
 - VirtualEnv
 - IPFS CLI

### IPFS-CLI
For its CLI interface IPFS uses a package called [Kobo](https://docs.ipfs.tech/install/command-line). The script uses a library called [ipfshttpclient](https://github.com/ringabout/ipfshttpclient) and this only works with [Kobo version 7](https://github.com/ipfs-shipyard/py-ipfs-http-client/issues/239) *(& [here as well](https://github.com/ipfs-shipyard/py-ipfs-http-client/issues/275#issuecomment-830010444))*. So please only install Kobo version 7 from this [site](https://dist.ipfs.tech/go-ipfs/v0.7.0).
```
# ipfs init
...
# ipfs version
ipfs version 0.7.0
# ipfs daemon
```

### Setup
```
# cp .env.example .env
# vim .env
export DESCRIPTION=Simple Base Apes Project
export BASE_EXTERNAL_URL=https://nfts.someproject.io/
export NFT_BASE_NAME=Simple Apes
export BACKGROUND_0=Wall
...
export BACKGROUND_9=House
export HEAD_0=Hat
...
export HEAD_9=Blond Hair
export EYES_0=Green
...
export EYES_9=Blue
export MOUTH_0=Open
...
export MOUTH_9=Cigarette
export TATTOO_0=Dove
...
export TATTOO_9=Celtic
export CLOTHES_0=Open Shirt
...
export CLOTHES_9=Big Coat
# ...
```

### Virtual Environment
```
# virtualenv .venv
# pip install -f requirments.txt
# source .venv/bin/activate
# python generate_nfts.py ...
```

https://ipfs.io/ipfs/QmZ7D8KX8ECntVUrYP13UqQztcq7oo6kArvJqwFznNoA8z
