pensieve
===

pensieve is an easy extensible server architecture to accept socket data such as sensor readings, images, etc.

Dependencies
------------

List your project's dependencies here, e.g.:

* [Python 2.7.x](http://www.python.org/)
* [NumPy](http://www.numpy.org/) (lumos doesn't need SciPy, just NumPy, but it doesn't hurt)
* [OpenCV 2.4.x](http://opencv.org/)
* [PyZMQ](http://zeromq.org/bindings:python) (optional, for streaming/pub-sub servers)

Installation
------------

List installation steps here to make it easier for people grab your project and start hacking.

1. Clone:
    
    ```bash
    $ git clone git@github.com:<your_username>/pensieve.git
    ```

2. Install:
    
    ```bash
    $ [sudo] python setup.py develop
    ```
    
    Note: This installs in [development mode](https://pythonhosted.org/setuptools/setuptools.html#develop-deploy-the-project-source-in-development-mode), which means Python modules are exposed directly from the source directory. You can then update your local copy to pull in changes from the remote repository, and/or make changes yourself. You can also use `[sudo] python setup.py install` for a typical installation (recommended: [Python virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)).

Usage
-----

Give some usage examples, like how to run your project or use your package in code.

Note that this outermost `pensieve` directory is a container for your top-level Python package that lives in the inner `pensieve` directory. Any module under that, say `pensieve/bar.py` will be accessible as `import pensieve.bar` from this level and from anywhere on the system once installed (even in developer mode). The recommended way to run your scripts is from this outer level, e.g. `$ python -m pensieve.bar`.
