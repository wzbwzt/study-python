import ray

ray.init()


@ray.remote
def my_task():
    return "Hello, world!"


result = ray.get(my_task.remote())
print(result)

ray.shutdown()
