"""
This module provides the utilities for determining which stack a package should  be sent to. 

Functions include:
- sort: Determines which stack to send a package to given its dimensions and mass
- _is_bulky_package: Determines if a package is considered bulky or not based on its dimensions

Usage:
    Import the module and call the function sort:
        from utilities.package_dispatcher import sort
        stack = sort(width=5, height=5, length=5, mass=5)

Test:   test_package_dispatcher
Author: Michael Kumicich
Date:   January 26, 2025
"""


from enums import DispatchStacks

def sort(width, height, length, mass):
    """
    Determine which stack to dispatch packages to based on the volume and mass of the packages.

    Args:
        width:  The width of the package.
        height: The height of the package.
        length: The length of the package.
        mass:   The mass of the package.

    Returns:
        String: The package to dispatch to.
    """
    args = (width, height, length, mass)
    if not all((isinstance(arg, (float, int)) and arg > 0) for arg in args):
        raise ValueError("Invalid arguments: Width, height, length, and mass must all be numbers greater than 0")
    
    isHeavy = mass >= 20
    isBulky = _is_bulky_package(width, height, length)

    if isHeavy and isBulky:
        return DispatchStacks.REJECTED.value
    elif isBulky or isHeavy:
        return DispatchStacks.SPECIAL.value
    else:
        return DispatchStacks.STANDARD.value

def _is_bulky_package(width, height, length):
    """
    Determine if the package's dimensions qualify it as bulky

    Args:
        width:  The width of the package.
        height: The height of the package.
        length: The length of the package.

    Returns:
        Boolean: Whether or not the package is bulky
    """

    volume = width * height * length
    if any(arg >= 150 for arg in (width, height, length)) or volume >= 1000000:
        return True
    return False
