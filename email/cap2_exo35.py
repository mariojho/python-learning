#!/usr/bin/env python 

import smtplib

# Un email muliparte (contiene anexos)
from email.mime.multipart import MIMEMultipart

# Un mensaje email de tipo texto 
from email.mime.text import MIMEText

# Un mensaje email de tipo imagen
from email.mime.image import MIMEImage

import mimetypes, posixpath 

def image_a_mail(rutaarchivo):
    '''envío de un mensaje de tipo MIMEImage a partir'''
# Utilizamos posix para tener el nombre del archivo
    nomarchivo = posixpath.basename(rutaarchivo)
# luego obtenermos la extensión del archivo 
    extension = posixpath.splitext(nomarchivo)
# Luego usamos mimetypes para tener el content-type de la extensión 
    content_type = mimetypes.types_map[extension[1]]
# Abrimos el archivo de imagen en modo binario 
    archivo = open(rutaarchivo, 'rb')
# Un objeto message con el contenido del archivo
    image = MIMEImage(archivo.read())
# Añadimos las cabeceras para la imagen
    image.add_header('Content-Disposition', 'attachment;filename="%s"'%nomarchivo)
    image.add_header("Content-Type", content_type)
# Devolvemos el objeto message que contiene la imagen
    return image 

def send(mfrom, mto):
    #Añadimos las cabeceras para el mail principal 
    emailmultipart['From'] = mfrom 
    emailmultipart['To'] = mto 
    emailmultipart['Subject'] = '¡Hola!'
    # Creamos un mensaje simple en HTML (¡Qué nivel!;)
    emailtext = MIMEText('<b>¡Hola!</b>', 'html')
    # agregamos este mail a nuestro multipart 
    emailmultipart.attach(emailtext)

# Creamos un objeto mensaje multipart
emailmultipart = MIMEMultipart()
# Creamos un mensaje de tipo MIMEImage empleando nuestra función
emailimage = image_a_mail("/home/mariojho/Desarrollo/hacking/python-learning/email/imagen1.png")
# Vinculamos la imagen a nuestro multipart
emailmultipart.attach(emailimage)

# Enviamos el mail
server = smtplib.SMTP('smtp.linuxmedellin.org', 587)
send('mario@correo.com', 'maria@correo.es')
# Agregamos el mail a nuestro multipart 
server.sendmail('mario@correo.com', 'maria@correo.es', emailmultipart.as_string())
server.quit()