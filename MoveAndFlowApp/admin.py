#Admin.py se utiliza para indicar a Django qué modelos utilizar en el proyecto
# Register your models here.

from django.contrib import admin

#a continuacion el resgistro de los modelos en la aplicación, lo dejo comentado mientras hay mas 
#claridad sobre ello, ver guia de clase #8

# from .models.administrador import Administrador
from .models.estacion import Estacion
from .models.bicicleta import Bicicleta
from .models.user import User

admin.site.register(Estacion)
admin.site.register(Bicicleta)
admin.site.register(User)

