SRComp Scorer
=============

|Build Status| |Docs Status|

A web UI to edit scores from SRComp score files.

Usage
-----

**Install**:

.. code:: shell

    script/install.sh

The install script prints instructions regarding the setup of the corresponding
compstate as well as how to run the resulting instance. Currently this is aimed
at install on a user's own machine rather than being hosted externally.

Development
-----------

**Install**:

.. code:: shell

    pip install git+https://github.com/PeterJCLaw/srcomp
    pip install -e .

**Run**:
``python -m sr.comp.scorer`` (see the ``--help``) for details.

Developers may wish to use the `SRComp Dev`_ repo to setup a dev instance.


.. |Build Status| image:: https://travis-ci.org/PeterJCLaw/srcomp-scorer.png?branch=master
   :target: https://travis-ci.org/PeterJCLaw/srcomp-scorer

.. |Docs Status| image:: https://readthedocs.org/projects/srcomp-scorer/badge/?version=latest
   :target: https://srcomp-scorer.readthedocs.org/


.. _`SRComp Dev`: https://github.com/PeterJCLaw/srcomp-dev
