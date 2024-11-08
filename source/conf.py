# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('../TFB'))

project = 'TFB'
copyright = ('2024, Xiangfei Qiu, Jilin Hu, Lekui Zhou, Xingjian Wu, Junyang Du, Buang Zhang, Chenjuan Guo, '
             'Aoying Zhou, Christian S. Jensen, Zhenli Sheng, Bin Yang')
author = ('Xiangfei Qiu, Jilin Hu, Lekui Zhou, Xingjian Wu, Junyang Du, Buang Zhang, Chenjuan Guo, Aoying Zhou, '
          'Christian S. Jensen, Zhenli Sheng, Bin Yang')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "furo"
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_domain_indices = False
html_show_sourcelink = False
add_module_names = False
autodoc_mock_imports = [
    "darts",
    "einops",
    "matplotlib",
    "merlion",
    "numpy",
    "pandas",
    "scikit_learn",
    "scipy",
    "statsmodels",
    "torch",
    "ray",
    "tqdm",
    "dash",
    "dash_bootstrap_components",
    "reformer_pytorch",
    "lightgbm",
    "sklearn",
    "sklearn.preprocessing",
    "sympy",
    "flask",
]
