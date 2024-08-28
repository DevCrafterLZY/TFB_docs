FAQ
===

How to use Pycharm to run code？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When running under pycharm，please escape the double quotes, remove the
spaces, and remove the single quotes at the beginning and end.

Such as: **‘{“d_ff”: 512, “d_model”: 256, “horizon”: 24}’ —>
{\\“d_ff\\”:512,\\“d_model\\”:256,\\“horizon\\”:24}**

.. code:: shell

   --config-path "rolling_forecast_config.json" --data-name-list "ILI.csv" --strategy-args {\"horizon\":24} --model-name "time_series_library.DLinear" --model-hyper-params {\"batch_size\":16,\"d_ff\":512,\"d_model\":256,\"lr\":0.01,\"horizon\":24,\"seq_len\":104} --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/DLinear"