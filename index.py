from PIL import Image
import os

# Caminhos
input_images = 'input_images'
output_images = 'output_images'
# Cria a lista de images
images = os.listdir(input_images)
#x = [str(f'{path_pdf}/{a}') for a in os.listdir('sequencia') if a.endswith(".pdf")]
for image in images:
    # Abre a imagem
    img = Image.open(f'{input_images}/{image}')
    # Converte a imagem
    rgb_img = img.convert('RGB')
    # Salva a imagem convertida
    rgb_img.save(f"{output_images}/{image.split('.')[0]}.jpg")
