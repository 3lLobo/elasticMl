from optimum.exporters.tasks import TasksManager

model_type = "meta-llama/Llama-2-7b-hf"
# For instance, for the ONNX export.
backend = "onnx"
distilbert_tasks = TasksManager.infer_task_from_model(model_type)
print(distilbert_tasks)
