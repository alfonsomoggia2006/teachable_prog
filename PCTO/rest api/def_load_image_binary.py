def load_image_binary(image_binary):
    binary_numpy=np.fromfile(image_binary, dtype="uint8")

    image=cv2.imdecode(binary_numpy, cv2.IMREAD_COLOR)

    return image