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

2. How to get models’ predicted values and the target values？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We provide tutorial about how to get the models’ predicted values and
the target values, you can click :ref:`here <get-pre-tar>`.

3. Examples of script writing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to run datasets in parallel, test multiple datasets, or test
multiple algorithms, and so on, you can refer to the following command.

.. code:: shell

    # 1、Simultaneously evaluating 25 multivariate datasets, note that there is no need to specify the --data-name-list parameter at this time.
    python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --strategy-args '{"horizon":24}' --model-name "time_series_library.DLinear" --model-hyper-params '{"batch_size": 16, "d_ff": 512, "d_model": 256, "lr": 0.01, "horizon": 24, "seq_len": 104}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "DLinear"

    # 2、Use ray to parallelly evaluate all multivariate datasets.
    python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --strategy-args '{"horizon":24}' --model-name "time_series_library.DLinear" --model-hyper-params '{"batch_size": 16, "d_ff": 512, "d_model": 256, "lr": 0.01, "horizon": 24, "seq_len": 104}' --adapter "transformer_adapter"  --gpus 0 1 2 3  --eval-backend "ray" --num-workers 4  --timeout 60000  --save-path "DLinear"

    # 3、According to the forecast horizon of the dataset, it is divided into two categories of multivariate datasets (24, 36, 48, 60 and 96, 192, 336, 720), and evaluated simultaneously.
    python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json"  --data-name-list "ETTm1.csv" "ETTm2.csv" "Exchange.csv" "Weather.csv" "METR-LA.csv" "PEMS-BAY.csv" "PEMS04.csv" "PEMS08.csv" "Electricity.csv" "Traffic.csv" "AQShunyi.csv" "AQWan.csv" "ZafNoo.csv" "CzeLan.csv" "Wind.csv" "ETTh1.csv" "ETTh2.csv" "Solar.csv" --strategy-args '{"horizon":96}' --model-name "time_series_library.Linear" --model-hyper-params '{"d_ff": 64, "d_model": 32, "lr": 0.005, "horizon": 96, "seq_len": 512}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Linear"

    python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json"  --data-name-list "Covid-19.csv" "FRED-MD.csv" "ILI.csv" "NN5.csv" "NYSE.csv" "Wike2000.csv" "NASDAQ.csv" --strategy-args '{"horizon":24}' --model-name "time_series_library.Linear" --model-hyper-params '{"d_ff": 64, "d_model": 32, "lr": 0.005, "horizon": 24, "seq_len": 104}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Linear"

    # 4、Simultaneously evaluate the performance of specified algorithms on specified multivariate datasets.
    # Please note that --model-name, --model-hyper-params, and --adapter correspond one-to-one.
    # For algorithms starting with time_series_library, the corresponding adapter is transformer_adapter; The corresponding adapter starting with darts is "None"
    # If an algorithm does not require input parameters, write {} at the corresponding position in --model-hyper-params.
    python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json"  --data-name-list "ILI.csv" "NN5.csv" --strategy-args '{"horizon":24}' --model-name "time_series_library.DLinear" "self_impl.VAR_model" "time_series_library.PatchTST" "darts.TCNModel" --model-hyper-params '{"batch_size": 16, "d_ff": 512, "d_model": 256, "lr": 0.01, "horizon": 24, "seq_len": 104}' {} '{"batch_size": 32, "d_model": 512, "e_layers": 4, "factor": 3, "n_headers": 4, "horizon": 24, "seq_len": 104, "d_ff": 2048}' '{"input_chunk_length": 104, "n_epochs": 10, "output_chunk_length": 24}' --adapter "transformer_adapter" "None" "transformer_adapter" "None" --gpus 0  --num-workers 1  --timeout 60000  --save-path "Multiple_algorithms"

