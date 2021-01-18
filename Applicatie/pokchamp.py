import subprocess

image_in = r"C:\tools\transfer_782052_files_3c3b1f65\Hydrologic_Package_2020-12-09\Hydrologic_Package_2020-12-09\Afstroomanalyse\Buurten\Ondiep\resultaten"
image_out = r"path_output_image.tif"
subprocess.call(["gdal_translate.exe","-co", "TILED=YES", "-co", "COMPRESS=LZW" "-ot", "Byte", "-scale", image_in, image_out ])