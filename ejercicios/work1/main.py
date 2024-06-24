calificacion = float( input("Introduce calificacion: ") )

if calificacion >= 90:
    print("¡Felicidades! Has aprobado con una calificación sobresaliente.")
elif calificacion >= 70 and calificacion < 90:
    print("Has aprobado satisfactoriamente.")
elif calificacion >= 60 and calificacion < 70:
    print("Has aprobado, pero necesitas mejorar un poco.")
elif calificacion < 60:
    print( "Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación.")