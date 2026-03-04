def exists(x):
    """Check if a value is not None.

    Args:
        x: Any value to check.

    Returns:
        bool: True if x is not None, False otherwise.

    Examples:
        >>> from exists import exists
        >>> exists(42)
        True
        >>> exists(None)
        False
        >>> exists(0)
        True
        >>> exists("")
        True
        >>> exists([])
        True
    """
    return x is not None
