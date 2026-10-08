import time
from gpiozero import LED

# Mapeo de los 5 LEDs a pines GPIO consecutivos (puedes ajustarlos a los que estés usando)
# Usamos pines BCM: 17, 27, 22, 5, 6
leds = [
    LED(17), # LED 1 (Extremo izquierdo)
    LED(27), # LED 2
    LED(22), # LED 3 (Centro)
    LED(5),  # LED 4
    LED(6)   # LED 5 (Extremo derecho)
]

def apagar_todos():
    """Apaga todos los LEDs de la lista."""
    for led in leds:
        led.off()

def secuencia_corrida(velocidad=0.15):
    
    print("Iniciando mapeo de 5 LEDs... (Presiona Ctrl+C para detener)")
    try:
        while True:
            # Recorrido de izquierda a derecha (0 -> 4)
            for i in range(len(leds)):
                apagar_todos()
                leds[i].on()
                time.sleep(velocidad)

            # Recorrido de derecha a izquierda (de regreso: 3 -> 1)
            for i in range(len(leds) - 2, 0, -1):
                apagar_todos()
                leds[i].on()
                time.sleep(velocidad)

    except KeyboardInterrupt:
        # Apagado limpio y seguro al interrumpir con el teclado
        print("\nDeteniendo secuencia y apagando LEDs...")
        apagar_todos()

if __name__ == "__main__":
    secuencia_corrida()