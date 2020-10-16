from PIL import Image
import time

def brightness(source_name, result_name, brightness):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))

            red = int(r * brightness)
            red = min(255, max(0, red))

            green = int(g * brightness)
            green = min(255, max(0, green))

            blue = int(b * brightness)
            blue = min(255, max(0, blue))

            result.putpixel((x, y), (red, green, blue))
    result.save(result_name, "JPEG")


start_time = time.time()
br = brightness('pic.jpg', 'ex3 pic.jpg', 3)
print("--- %s seconds ---" % (time.time() - start_time))

