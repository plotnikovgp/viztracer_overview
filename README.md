## Brief overview of [VizTracer](https://github.com/gaogaotiantian/viztracer)
VizTracer is a ~pretty low-overhead (2x-3x times slower) logging/debugging/profiling tool that can trace and visualize your python code execution. Works with trheads multiprocessing and asyncio.

installation:
```
pip install viztracer
```

usage on *.py* files:
```
viztracer script.py [args]
...
vizviewer result.json
```
