import colorama
import inspect
import sys
print(f"The name: {colorama.__name__}")
print(f"The version: {colorama.__version__}")
print(f"The way: {inspect.getmodule(colorama)}")
print(f"Is it module?: {inspect.ismodule(colorama)}")
print(f"Is it class?: {inspect.isclass(colorama)}")
print(f"Is it function?: {inspect.isfunction(colorama)}")

print()
print("About Python: ")
print(f"The version: {sys.version}")
print(f"The way: {sys.executable}")
print(f"The platform: {sys.platform}")
print("Embedded data: ")
print()
for _ in dir(__builtins__):
    print(_)
print("^^^^^^^^^^^^^^^^^^^")


















