pensieve
===

pensieve is an easy extensible server architecture to accept socket data such as sensor readings, images, etc.

Dependencies
------------

* [Python 2.7.x](http://www.python.org/)
* [NumPy](http://www.numpy.org/) (pensieve doesn't need SciPy, just NumPy, but it doesn't hurt)
* [OpenCV 2.4.x](http://opencv.org/)
* [PyZMQ](http://zeromq.org/bindings:python) (optional, for streaming/pub-sub servers)

Installation
------------

1. Clone:
    
    ```bash
    $ git clone git@github.com:sinabahram/pensieve.git
    ```

2. Install (after `cd pensieve/`):
    
    ```bash
    $ [sudo] python setup.py develop
    ```
    
    Note: This installs in [development mode](https://pythonhosted.org/setuptools/setuptools.html#develop-deploy-the-project-source-in-development-mode), which means Python modules are exposed directly from the source directory. You can then update your local copy to pull in changes from the remote repository, and/or make changes yourself. You can also use `[sudo] python setup.py install` for a typical installation (recommended: [Python virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)).

Usage
-----

Run server:
```bash
$ python -m pensieve.server
```

Run test client:
```bash
$ python -m pensieve.tests.client
```

Note: You can connect to a running server instance from any pensieve client.
