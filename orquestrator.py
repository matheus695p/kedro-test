from kedro.io import DataCatalog, MemoryDataSet
from kedro.pipeline import node, Pipeline
from kedro.runner import SequentialRunner

from src.cleaning.clean import cleaning_process
from src.preprocessing.preprocess import prepro_process
from src.inference.predict import inference_process
from src.monitoring.monitor import monitor_process

# Prepare a data catalog
data_catalog = DataCatalog({"cleaning": MemoryDataSet()})

# Hacer los nodos
cleaning = node(cleaning_process, inputs=None, outputs="cleaning")
preprocess = node(prepro_process, inputs="cleaning", outputs="preprocess")
predict = node(inference_process, inputs="preprocess", outputs="inference")
monitor = node(monitor_process, inputs="inference", outputs="monitor")

# Hacer el pipeline
pipeline = Pipeline([cleaning, preprocess, predict, monitor])

# crear el runner
runner = SequentialRunner()
# Ejecutar
print(runner.run(pipeline, data_catalog))
