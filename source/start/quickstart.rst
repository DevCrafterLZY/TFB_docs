Quick Start
===========

Installation
~~~~~~~~~~~~

You can obtain the source code from `GitHub <https://github.com/decisionintelligence/TFB>`_.

From PyPI
^^^^^^^^^

Given a python environment (**note**: this project is fully tested under
**python 3.8**), install the dependencies with the following command:

.. code:: shell

   pip install -r requirements.txt

From Docker
^^^^^^^^^^^

We also provide a
`Dockerfile <https://github.com/decisionintelligence/TFB/blob/master/Dockerfile>`__
for you. For this setup to work you need to have a Docker service
installed. You can get it at `Docker
website <https://docs.docker.com/get-docker/>`__.

.. code:: shell

   docker build . -t tfb:latest

.. code:: shell

   docker run -it -v $(pwd)/:/app/ tfb:latest bash

Data preparation
~~~~~~~~~~~~~~~~

You can obtained the well pre-processed datasets from `Google
Drive <https://drive.google.com/file/d/1vgpOmAygokoUt235piWKUjfwao6KwLv7/view?usp=drive_link>`__.
Then place the downloaded data under the folder ``./dataset``.

Train and evaluate model
~~~~~~~~~~~~~~~~~~~~~~~~

We provide the experiment scripts for all benchmarks under the folder
``./scripts/multivariate_forecast``, and
``./scripts/univariate_forecast``. For example you can reproduce a
experiment result as the following:

.. code:: shell

   sh ./scripts/multivariate_forecast/ILI_script/DLinear.sh

