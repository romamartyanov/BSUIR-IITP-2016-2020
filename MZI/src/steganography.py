import textwrap

from PIL import Image, ImageFont, ImageDraw


def decode_image(encoded_image_path="resources/lab_8/Group 4-3_encoded.png",
                 decoded_image_path='resources/lab_8/Group 4-3_decoded.png'):
    """
    Decodes the hidden message in an image

    input_image: the location of the image file to decode. By default is the provided encoded image in the images folder
    output_image: decoded image
    """
    encoded_image = Image.open(encoded_image_path)
    red_channel = encoded_image.split()[0]

    binary_text_list = []

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                binary_text_list.append('0')
                pixels[i, j] = (255, 255, 255)
            else:
                binary_text_list.append('1')
                pixels[i, j] = (0, 0, 0)
    binary_text = ''.join(binary_text_list)

    def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

    normal_text = text_from_bits(binary_text)


    with open('resources/stalker2_art_uhd_new.jpg.txt') as f:
        f.write(normal_text)
    decoded_image.save(decoded_image_path)


def write_text(text_to_write, image_size):
    """
    Writes text to an RGB image. Automatically line wraps

    text_to_write: the text to write to the image
    """
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    # Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin, offset), line, font=font)
        offset += 10
    return image_text


def encode_image(text_to_encode,
                 normal_image_path="images/Group 4-3.png",
                 encoded_image_path='Group 4-3_encoded.png'):
    """
    Encodes a text message into an image

    text_to_encode: the text to encode into the template image
    input_image: the image to use for encoding. An image is provided by default.
    output_image: encoded image
    """
    normal_image = Image.open(normal_image_path)
    red_template = normal_image.split()[0]
    green_template = normal_image.split()[1]
    blue_template = normal_image.split()[2]

    x_size = normal_image.size[0]
    y_size = normal_image.size[1]

    # text draw
    image_text = write_text(text_to_encode, normal_image.size)
    bw_encode = image_text.convert('1')

    # encode text into image
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()
    for i in range(x_size):
        for j in range(y_size):
            red_template_pix = bin(red_template.getpixel((i, j)))
            old_pix = red_template.getpixel((i, j))
            tencode_pix = bin(bw_encode.getpixel((i, j)))

            if tencode_pix[-1] == '1':
                red_template_pix = red_template_pix[:-1] + '1'
            else:
                red_template_pix = red_template_pix[:-1] + '0'
            pixels[i, j] = (int(red_template_pix, 2), green_template.getpixel((i, j)), blue_template.getpixel((i, j)))

    encoded_image.save(encoded_image_path)
