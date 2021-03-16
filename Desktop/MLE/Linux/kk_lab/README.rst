kk_lab
--------

To use (with caution), simply do::

    # Import my_package library
    >>> import kk_lab
    # To download data of security from yahoo
    >>> data=kk_lab.get_df("AAPL", "7d")
    # To get a plot of security and save it
    >>> kk_lab.plot_7d(data, './apple.png')