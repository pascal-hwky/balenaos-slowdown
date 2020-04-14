import time
import tflite_runtime.interpreter as tflite
import numpy as np

# Set up model
interpreter = tflite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
input_shape = input_details[0]['shape']
output_details = interpreter.get_output_details()

# Generate input data
frame = np.zeros((1, input_shape[1], input_shape[2], 3), np.float32)
interpreter.set_tensor(input_details[0]['index'], frame)

# Time N inferences
N = 100
duration = []
for _ in range(N):
    t0 = time.time()
    interpreter.invoke()
    tf = time.time()
    duration.append(tf - t0)

# Print results
print(f'Finished {N} inferences.')
print(f'Max time: {int(1000 * max(duration))} [ms]')
print(f'Min time: {int(1000 * min(duration))} [ms]')
print(f'Avg time: {int(1000 * sum(duration) / len(duration))} [ms]')

time.sleep(5.)
