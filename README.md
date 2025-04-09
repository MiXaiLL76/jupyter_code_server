# jupyter_code_server

## Disclaimer

Many developers are forced to use jupyterlab\\jupyterhub during work, without the ability to use VSCODE.
Our comrades from [coder](https://github.com/coder) have done a great job to make it possible to use VSCODE through a browser.
My job is left to make these two technologies friends and provide the ability to quickly and conveniently launch both of these applications.

This library works in tandem with the [jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy) library, which in turn allows you to create additional servers inside Jupyter.

## Install

Just run the installation from pypi and enjoy
**After installation, be sure to restart the server (if it is running in docker, then restart docker)**

```bash
pip install jupyter_code_server
```

### Extra install

By default, this library installs the latest version of code-server on your device in the **~/.local/lib** directory

> If you do not want automatic installation, you can do it later or disable it altogether.

Disabling automatic installation of code-server

```bash
JUPYTER_CODE_SERVER_SKIP_INSTALL=1 pip install jupyter_code_server
```

Installing a specific [version of code-server](https://api.github.com/repos/coder/code-server/releases)

> To do this, you need to set env CODE_SERVER_VERSION
> CODE_SERVER_VERSION - lataset by default
> Since version search is not controlled by github tags, it is better to look at the api and search for the **id** of the release.

Installation example **tag_name "v4.99.1"**

```bash
CODE_SERVER_VERSION=211138150 pip install jupyter_code_server
```

### CLI Commands

```bash
usage: jupyter_code_server [-h] [--version] [--install] [--install-server] [--install-extensions] [--install-settings] [--patch-tornado]

options:
 -h, --help show this help message and exit
 --version show program's version number and exit
 --install Install code-server, extensions ad settings
 --install-server Install code-server
 --install-extensions Install extensions
 --install-settings Install settings
 --patch-tornado Monkey patch tornado.websocket
```

## Requirements

For more details [see here](https://github.com/coder/code-server?tab=readme-ov-file#requirements)

## License

Since the [code-server](https://github.com/coder/code-server) project has an MIT license, I also use it in this project.

## Citation

```
@article{jupyter_code_server,
title = {{jupyter_code_server}: VSCODE integration in jupyter-lab},
author = {MiXaiLL76},
year = {2024}
}
```
