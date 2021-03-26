from appy.pod.renderer import Renderer

inter="/usr/bin/python3"
 
staff = [{'nombre': 'Delannay', 'apellido': 'Gaetan', 'cedula': 112},
           {'nombre': 'Gauthier', 'apellido': 'Bastien', 'cedula': 5},
           {'nombre': 'Jean-Michel', 'apellido': 'Abe', 'cedula': 79}]

  
renderer = Renderer('prueba_template.ods', globals(), 'result.pdf',pythonWithUnoPath=inter)
renderer.run()
