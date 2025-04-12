import os
import platform
import setuptools
from setuptools.command.install import install
from importlib.util import module_from_spec, spec_from_file_location


def readme():
    with open("README.md", encoding="utf-8") as f:
        content = f.read()
    return content


version_file = "jupyter_coder_server/version.py"


def get_version():
    spec = spec_from_file_location("version", version_file)
    py = module_from_spec(spec)
    spec.loader.exec_module(py)
    return py.__version__, py.__author__


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        if platform.system().lower() != "linux":
            raise Exception("Only Linux is supported")

        value = super().run()

        if len(os.environ.get("SKIP_INSTALL", "")) == 0:
            from jupyter_coder_server import CoderServer, WebFileBrowser

            CoderServer().full_install()
            WebFileBrowser().full_install()

        return value


__version__, __author__ = get_version()

setuptools.setup(
    name="jupyter_coder_server",
    version=__version__,
    description="VSCODE integration in jupyter-lab",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/MiXaiLL76/jupyter_coder_server",
    author=__author__,
    author_email="mike.milos@yandex.ru",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Framework :: Jupyter",
        "Framework :: Jupyter :: JupyterLab",
        "Framework :: Jupyter :: JupyterLab :: 3",
        "Framework :: Jupyter :: JupyterLab :: 4",
        "Framework :: Jupyter :: JupyterLab :: Extensions",
        "Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9",
    entry_points={
        "jupyter_serverproxy_servers": [
            # name = packagename:function_name
            "vscode_server_fb = jupyter_coder_server:WebFileBrowser.setup_proxy",
            "vscode_server = jupyter_coder_server:CoderServer.setup_proxy",
        ],
        "console_scripts": ["jupyter_coder_server = jupyter_coder_server:main"],
    },
    install_requires=["jupyter-server-proxy", "tornado"],
    cmdclass={
        "install": PostInstallCommand,
    },
)
