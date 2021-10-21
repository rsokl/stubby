Hello
#####


.. code-block:: python
   
   from stubby import func
   func(1)


.. code-block:: python
   :caption: Contents of my_app.py:

   from hydra_zen import make_config, instantiate
    
   Config = make_config("player1", "player2")
    
   def task_function(cfg: Config):
       cfg = instantiate(cfg)

.. code-block:: python
   :caption: Contents of my_app.py:
 
   from hydra_zen import make_config, instantiate
    
   Config = make_config("player1", "player2")


.. code-block:: python
    :caption: Contents of my_app.py:

    1+1
    
    def f(): return


.. currentmodule:: stubby

.. autosummary::
   :toctree: generated/

   func
        