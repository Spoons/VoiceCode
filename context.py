#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Context generators

Easily generate context instances.
"""
from aenea import AppContext, ProxyAppContext, ProxyPlatformContext

def linux():
    """
    Context that matches only on linux.

    Raises
    ------
    None

    Returns
    -------
    aenea.ProxyPlatformContext

    Examples
    --------
    ..doctest::

        >>> TODO
    """
    return ProxyPlatformContext('linux')

def cross_platform_title_match(title):
    """
    Match title on both windows and any proxy.

    Parameters
    ----------
    title: str
        title to (partially) match

    Raises
    ------
    None

    Returns
    -------
    dragonfly.LogicOrContext

    Examples
    --------
    ..doctest::

        >>> TODO
    """
    return AppContext(title=title) | \
            ProxyAppContext(title=title)

def terminal():
    """
    Matches terminal applications.

    Matches PuTTY on windows or terminator on linux.

    Raises
    ------
    None

    Returns
    -------
    dragonfly.LogicOrContext

    Examples
    --------
    ..doctest::

        >>> terminal()
        LogicOrContext(...)
    """
    return AppContext('putty') | \
            ProxyAppContext(cls='terminator')

def true_vim():
    """
    Real vim context.

    Complete vim as opposed to vi or apps with vim
    key bindings.

    Raises
    ------
    None

    Returns
    -------
    dragonfly.LogicAndContext

    Examples
    --------
    ..doctest::

        >>> TODO
    """
    return terminal() & cross_platform_title_match(' VIM ')

def terminal_not_vim():
    """
    Terminal, not currently in vim.

    Raises
    ------
    None

    Returns
    -------
    dragonfly.LogicAndContext

    Examples
    --------
    ..doctest::

        >>> TODO
    """
    return terminal() & ~cross_platform_title_match(' VIM ')

def vim_normal_mode():
    """
    True vim in normal mode.

    Raises
    ------
    None

    Returns
    -------
    dragonfly.LogicAndContext

    Examples
    --------
    ..doctest::

        >>> TODO
    """
    return true_vim() & cross_platform_title_match(' mode:Normal')

def vim_insert_mode():
    """
    True vim in insert mode.

    Raises
    ------
    None

    Returns
    -------
    dragonfly.LogicAndContext

    Examples
    --------
    ..doctest::

        >>> TODO
    """
    return true_vim() & cross_platform_title_match(' mode:Insert')

def vim_visual_mode():
    """
    True vim in visual mode.

    This includes line and block visual modes.

    Raises
    ------
    None

    Returns
    -------
    dragonfly.LogicAndContext

    Examples
    --------
    ..doctest::

        >>> TODO
    """
    return true_vim() & cross_platform_title_match(' mode:Visual')

def vim_file_type(file_type):
    """
    True vim with buffer of type file_type focussed.

    Parameters
    ----------
    file_type: str
        vim file type to match

    Raises
    ------
    None

    Returns
    -------
    dragonfly.LogicAndContext

    Examples
    --------
    ..doctest::

        >>> TODO
    """
    return true_vim() & cross_platform_title_match(
        ' [{}] '.format(file_type))
