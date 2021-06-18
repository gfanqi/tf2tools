from tensorflow.python.compiler.tensorrt import convert as trt
from tensorflow.keras.applications import MobileNet

model = MobileNet(include_top=False)
input_saved_model_dir = './saved_model'
output_saved_model_dir = './'

converter = trt.TrtGraphConverterV2(input_saved_model_dir=input_saved_model_dir)
converter.convert()
converter.save(output_saved_model_dir)
