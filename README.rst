Dispatch from command-line arguments to functions
=================================================

Experimental.

Example
-------

.. code:: python

    """Run something in development or production mode.

    Usage: run-something.py (--development | --production) <host> <port>

    """
    from docopt_dispatch import dispatch


    @dispatch.on('--development')
    def development(host, port, **kwargs):
        print('in *development* mode')


    @dispatch.on('--production')
    def development(host, port, **kwargs):
        print('in *production* mode')


    if __name__ == '__main__':
        dispatch(__doc__)
