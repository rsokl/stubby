# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import stubby

# -- Project information -----------------------------------------------------

project = "stubby"
copyright = "NONE"
author = "Ryan Soklaski"

# The short X.Y version
version = "1.0.0"
# The full version, including alpha/beta/rc tags
release = "1.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosummary",
    "numpydoc",
    "sphinx_codeautolink",
]


default_role = "py:obj"

autodoc_typehints = "none"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "hydra_zen": ("https://mit-ll-responsible-ai.github.io/hydra-zen/", None),
}


# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
# A dictionary of external sites
#   alias ->  (base-URL, prefix)
_repo = "https://github.com/mit-ll-responsible-ai/hydra-zen/"
extlinks = {
    "commit": (_repo + "commit/%s", "commit "),
    "gh-file": (_repo + "blob/master/%s", ""),
    "gh-link": (_repo + "%s", ""),
    "issue": (_repo + "issues/%s", "issue #"),
    "pull": (_repo + "pull/%s", "pull request #"),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_favicon = "../../brand/hydra_zen_favicon_32x32.ico"
html_logo = "../../brand/Hydra-Zen_logo_full_filled_bkgrnd_smaller.png"

html_theme_options = {
    "collapse_navigation": True,
    "navigation_depth": 4,
    "favicons": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "../../brand/hydra_zen_favicon_32x32.ico",
        },
        {
            "rel": "icon",
            "sizes": "64x64",
            "href": "../../brand/hydra_zen_favicon_64x64.ico",
        },
        {
            "rel": "icon",
            "sizes": "134x134",
            "href": "../../brand/hydra_zen_favicon.ico",
        },
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/mit-ll-responsible-ai/hydra-zen",
            "icon": "fab fa-github-square",
        },
    ],
}


def setup(app):
    app.add_css_file("my_theme.css")


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
