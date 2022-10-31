import cv2
import numpy as np
import streamlit as st
import mediapipe as mp

st.title("Image Processing")
st.write(
    "Upload an image below and I will annotate the faces in the image using [MediaPipe](https://mediapipe.dev/)."
)

file = st.file_uploader("Upload a file")
if file is None:
    file = st.camera_input("Or take a picture")

if file is not None:
    # Display original image
    st.write("You uploaded", file.name)
    col1, col2 = st.columns(2)
    col1.image(file)

    # Annotate image
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    with mp.solutions.face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Display annotate image
        if results.multi_face_landmarks:
            annotated_image = image.copy()

            for face_landmarks in results.multi_face_landmarks:
                # st.code(face_landmarks)

                mp.solutions.drawing_utils.draw_landmarks(
                    image=annotated_image,
                    landmark_list=face_landmarks,
                    connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_tesselation_style(),
                )
                mp.solutions.drawing_utils.draw_landmarks(
                    image=annotated_image,
                    landmark_list=face_landmarks,
                    connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style(),
                )

            col2.image(annotated_image, channels="BGR")
        else:
            col2.write("No faces found")
