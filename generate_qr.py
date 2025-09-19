#!/usr/bin/env python3
"""
Generador de código QR para Hotel Ajedrez
Genera un código QR permanente para la URL del sitio web
"""

import qrcode
import os

def generate_qr_code():
    """Genera códigos QR para la URL del Hotel Ajedrez"""
    
    # URL del sitio web
    url = "https://gadielma.github.io/ajedrez/"
    
    # Crear instancia de QR Code con configuración optimizada
    qr = qrcode.QRCode(
        version=1,  # Controla el tamaño del QR
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección de errores
        box_size=10,  # Tamaño de cada "caja" del QR
        border=4,     # Borde alrededor del QR
    )
    
    # Añadir datos al QR
    qr.add_data(url)
    qr.make(fit=True)
    
    # Crear imagen básica en negro y blanco
    print("Generando código QR básico...")
    img_basic = qr.make_image(fill_color="black", back_color="white")
    img_basic.save("hotel_ajedrez_qr_basic.png")
    print("✓ QR básico guardado como: hotel_ajedrez_qr_basic.png")
    
    # Crear versión roja sobre negro (colores del hotel)
    print("Generando código QR rojo sobre negro...")
    img_red_black = qr.make_image(fill_color="#DC143C", back_color="black")
    img_red_black.save("hotel_ajedrez_qr_red_black.png")
    print("✓ QR rojo/negro guardado como: hotel_ajedrez_qr_red_black.png")
    
    # Crear versión negro sobre rojo
    print("Generando código QR negro sobre rojo...")
    img_black_red = qr.make_image(fill_color="black", back_color="#DC143C")
    img_black_red.save("hotel_ajedrez_qr_black_red.png")
    print("✓ QR negro/rojo guardado como: hotel_ajedrez_qr_black_red.png")
    
    # Crear versión de alta resolución en rojo y negro
    print("Generando código QR de alta resolución...")
    qr_large = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,  # Doble tamaño
        border=4,
    )
    qr_large.add_data(url)
    qr_large.make(fit=True)
    img_large = qr_large.make_image(fill_color="#DC143C", back_color="black")
    img_large.save("hotel_ajedrez_qr_large_red.png")
    print("✓ QR de alta resolución rojo/negro guardado como: hotel_ajedrez_qr_large_red.png")
    
    print(f"\n🎉 ¡Códigos QR generados exitosamente!")
    print(f"📱 URL codificada: {url}")
    print(f"📁 Ubicación: {os.getcwd()}")
    print("\nArchivos generados:")
    print("  • hotel_ajedrez_qr_basic.png      - Versión básica negro/blanco")
    print("  • hotel_ajedrez_qr_red_black.png  - Versión rojo sobre negro")
    print("  • hotel_ajedrez_qr_black_red.png  - Versión negro sobre rojo")
    print("  • hotel_ajedrez_qr_large_red.png  - Versión de alta resolución rojo/negro")

if __name__ == "__main__":
    generate_qr_code()
