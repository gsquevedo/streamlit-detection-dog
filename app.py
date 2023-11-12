# Python In-built packages
from pathlib import Path
import PIL
from PIL import ImageDraw
import cv2
import numpy as np

# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="Detecção de imagens",
    page_icon=":)",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Detectando imagens usando YOLOv8")

# Sidebar
st.sidebar.header("Configurando a imagem")

# Model Options
model_type = st.sidebar.radio(
    "Faça sua escolha", ['Detecção', 'Segmentação'])

confidence = float(st.sidebar.slider(
    "Selecione a confidenciabilidade", 25, 100, 60)) / 100

# Selecting Detection Or Segmentation
if model_type == 'Detecção':
    model_path = Path(settings.DETECTION_MODEL)
elif model_type == 'Segmentação':
    model_path = Path(settings.SEGMENTATION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)
st.sidebar.header("Escolha uma imagem")

source_radio = settings.IMAGE
source_img = None

# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Upload de imagens", type=("jpg", "jpeg", "png"))
    col1, col2 = st.columns(2)
    with col1:
        try:
            if source_img is None:
                default_image_path = str(settings.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Imagem padrão",
                         use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Imagem enviada",
                         use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)
    with col2:
        if source_img is None:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(default_detected_image_path)
            st.image(default_detected_image_path, caption='Imagem detectada',
                    use_column_width=True)
        else:
            if st.sidebar.button('Detecte..'):
                res = model.predict(uploaded_image, conf=confidence)
                
                # Inicialize uma lista vazia para armazenar detecções de "dog"
                dog_detections = []
                
                # Itere pelas detecções e adicione as detecções de "dog" à lista
                for name, box in zip(res[0].names, res[0].boxes):
                    cords = box.xyxy[0].tolist()
                    cords = [round(x) for x in cords]
                    class_id = res[0].names[box.cls[0].item()]
                    conf = round(box.conf[0].item(), 2)
                    if class_id == 'dog':
                        dog_detections.append((name, box))

                if dog_detections:
                    names, boxes = zip(*dog_detections)
                    image_array = np.array(uploaded_image)

                    for box in boxes:
                        cords = box.xyxy[0].tolist()
                        cords = [int(x) for x in cords]
                        class_id = names[boxes.index(box)]
                        conf = round(box.conf[0].item(), 2)

                        # Draw bounding box on the image
                        color = (255, 0, 0)  # Green color for the bounding box (you can change this)
                        thickness = 2  # Thickness of the bounding box

                        cv2.rectangle(
                            image_array,
                            (cords[0], cords[1]),
                            (cords[2], cords[3]),
                            color,
                            thickness
                        )

                        # Label the bounding box
                        label = f"Dog ({conf})"
                        cv2.putText(
                            image_array,
                            label,
                            (cords[0], cords[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            color,
                            2
                        )

                    st.image(image_array, caption='Imagem com detecções de cachorro',
                            use_column_width=True)
                else:
                    st.info("Nenhum cão detectado na imagem.")
else:
    st.error("Please select a valid source type!")

