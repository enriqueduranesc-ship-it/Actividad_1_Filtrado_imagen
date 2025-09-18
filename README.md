# Actividad_1_Filtrado_imagen
Detección de Placas

En este trabajo hice un código para poder detectar las placas de un coche en python usando matplotlib, pytesseract, numpy y cv2

Para finalizar la lectura de Texto probé con diferentes configuraciónes y la mejor para el tema fue PSM 8 aunque la PSM 13 tamíen lo leía bien, a su vez como detectaba caracteres raros con todas las configuraciónes cree una whitelist con solo el Alfabeto pues estas placas solo contienten texto y no números, en caso de querer detectar números se debería cambiar la Whitelist a solo números.
