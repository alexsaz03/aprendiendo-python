# Gestor básico de parcelas
cultivo = input("¿Qué cultivo tienes? (mango/aguacate/otro) ").lower()
dias_sin_lluvia = int(input("¿Cuántos días sin lluvia? "))
temperatura = float(input("¿Temperatura actual en grados? "))

if cultivo == "mango":
    if dias_sin_lluvia > 5 and temperatura > 30:
        print("⚠️ Riego urgente — el mango necesita agua.")
    elif dias_sin_lluvia > 3:
        print("💧 Considera regar pronto.")
    else:
        print("✅ El mango está bien por ahora.")
elif cultivo == "aguacate":
    if dias_sin_lluvia > 7:
        print("⚠️ Riego urgente — el aguacate es sensible a la sequía.")
    else:
        print("✅ El aguacate está bien por ahora.")
else:
    if dias_sin_lluvia > 4:
        print("💧 Revisa el riego de tu cultivo.")
    else:
        print("✅ Todo en orden.")