Dispatch from command-line arguments to functions
=================================================

Experimental.

Example
-------

.. code:: python

    """Run something in development or production mode.

    Usage: run.py --development <host> <port>
           run.py --production <host> <port>
           run.py remote add <item>
           run.py remote delete <item>

    """
    from docopt_dispatch import dispatch


    @dispatch.on('--development')
    def development(host, port, **kwargs):
        print('in *development* mode')


    @dispatch.on('--production')
    def development(host, port, **kwargs):
        print('in *production* mode')


    @dispatch.on('items', 'add')
    def items_add(item, **kwargs):
        print('adding item...')


    @dispatch.on('items', 'delete')
    def items_delete(item, **kwargs):
        print('deleting item...')


    if __name__ == '__main__':
        dispatch(__doc__)
