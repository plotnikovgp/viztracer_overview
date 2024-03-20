from viztracer import VizTracer

tracer = VizTracer()
tracer.start()

# code you want to profile here
a = 10**5
# end

tracer.stop()
tracer.save("result_.json") 
