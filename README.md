# Juego de la vida

Simulación del juego de la vida en **pygame**. 

![video](Include/videos/video-GoL-G.gif)

# Índice

1. [Índice](Índice)
2. [Breve historia](Brevehistoria)


## Breve historia

El juego de la vida es un automata celular diseñado por el matemático británico Jonh Horton Convway en 1970. Es un juego de cero jugadores en el que su evolución es determinada por un estado inicial, sin requerir intervención adicional. 

Puede ver una descripción más completa y detallada aquí,
<a href="https://es.wikipedia.org/wiki/Juego_de_la_vida" target="_blank">Juego de la vida - Wikipedia</a>

### Reglas

El estado de todas las células se tiene en cuenta para calcular el estado de las mismas al turno siguiente. Todas las células se actualizan simultáneamente en cada turno, siguiendo estas reglas:

*   Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).

*   Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación").


## Descargar

1. Clone el repositorio desde su bash en la ubicación en la que desea tenerlo:
```
git clone https://github.com/nachoperezzv/Juego-de-la-vida.git
```

2. Cree el entorno virtual de python para no modificar sus bibliotecas personales y asegurarse de que se descarga la versión correcta de **pygame**. Puede hacerlo de la siguiente forma , estando en la misma ubicación que en el paso anterior:

```
python -m venv Juego-de-la-vida
```

3. Acceda a la carpeta:
```
cd Juego-de-la-vida
```

4. Deberá activar su entorno virtual. Por convención, con `venv` debería de disponer de un directorio de nombre `Scripts`. Acceda a el y luego ejecute el siguiente comando. 

    - Desde `cmd`:
    ```
    cd Scripts
    .\activate.bat
    ```

    - Desde `terminal` (linux):
    ```
    source \Scripts\.activate.bat
    ```

5. Una vez ha generado y activado su entorno virtual, instale los paquetes:

```
python install -r requirements.txt
```


## Compilar

Este dato es importante puesto que se debe compilar exclusivamente desde la carpeta `/src`. Si se hace desde la carpeta general de `/PingPong` provocará un fallo. 

```
C:\Users\user\Juego-de-la-vida\src\python main.py 
```

## Controles

Al ser un juego de 0 jugadores no hay muchos controles.

* Pulse el **botón izquierdo del ratón** para detener 'la vida' y añadir celdas vivas. Si pulsa sobre una celda viva esta morirá

* Pulse el **botón derecho del ratón** para matar una celda. 

* Pulse **Espacio** para detener el juego.

* Pulse **ESC** para reiniciar el juego
