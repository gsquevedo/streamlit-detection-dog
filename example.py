    # with col2:
    #     if source_img is None:
    #         default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
    #         default_detected_image = PIL.Image.open(
    #             default_detected_image_path)
    #         st.image(default_detected_image_path, caption='Imagem detectada',
    #                  use_column_width=True)
    #     else:
    #         if st.sidebar.button('Detecte..'):
    #             res = model.predict(uploaded_image,
    #                                 conf=confidence
    #                                 )
    #             names = res[0].names
    #             boxes = res[0].boxes

    #             print(names)
    #             res_plotted = res[0].plot('dogs')[:, :, ::-1]
                
    #             st.image(res_plotted, caption='Imagem detectada',
    #                      use_column_width=True)