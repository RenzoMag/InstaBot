# InstaBot

Bot automatizador de interacciones.  
Hecho con Python y selenium WebDriver.

### <ins>Funcionamiento:</ins>

- El bot obtiene los seguidores de una cuenta aleatoria de una lista de personas pertenecientes a un nicho.
- Seguidamente empieza a seguir a cada uno, en la cantidad total, seleccionada en la ejecucion del programa.
- El tiempo de espera entre peticion se seguimiento queda randomizada entre los rangos seleccionados.
- Luego de finalizar la secuencia, el bot puede apagar la computadora, o no hacerlo.

***

En el repositorio se encuentran dos archivos, de los cuales uno pertenece al sistema de seguimiento y el otro al sistema inverso.  
Esto se debe a que el bot utiliza el metodo seguir-dejar de seguir para generar interaccion en la cuenta.


### <ins>Configuración y requerimientos:</ins>
- Usted deberá descargar ambos archivos.
- Deberá tener python instalado.  
- En el final de los dos archivos encontrará la linea <code>bot = InstagramBot('user', 'password')</code> y <code>l2 = ["accounts"]</code>, en estos deberá configurar su correo, contraseña y a continuación una lista de cuentas pertenecientes a su nicho correspondiente.
***
### <ins>Descargo de responsabilidad:</ins>
- La utilización de cualquier tipo de automatización en instagram esta penada con shadowbans, ban definidos e indefinidos.  
- La programación y el sistema utilizado para este bot fue seleccionado para poder sortear los sistemas de detección de instagram.  
Esto no quiere decir que una mala utilización del bot no pueda ser detectada.
- Actue como si fuera una persona y no tendrá problemas.
- Utilicelo bajo su propio riesgo.
