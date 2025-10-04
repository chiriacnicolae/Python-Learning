import venv as tf
print(tf.config.list_physical_devices('GPU'))
print("Test running...")

print(tf.reduce_sum(tf.random.normal([1000, 1000])))