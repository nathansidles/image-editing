import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from editor.editor import Editor


class EditorV1(Editor):

    @staticmethod
    def watermark(source: str, destination: str, message: str):
        """Traverses the source directory recursively, creates a destination
        directory, and copies all images from the source directories into the
        destination directories, adding a watermark and preserving file
        structure.

        Keyword arguments:
        source -- (str) the source directory
        destination -- (str) the destination directory
        """
        source = os.path.abspath(source)
        source_prefix = len(source) + len(os.path.sep)

        try:
            os.makedirs(destination)
        except Exception as e:
            print("'" + destination + "' already exists")

        for root, dirs, files in os.walk(source):

            for dirname in dirs:

                dirpath = os.path.join(destination,
                                       root[source_prefix:],
                                       dirname)
                dirroot = os.path.join(destination, root[source_prefix:])

                try:
                    os.mkdir(dirpath)
                except Exception as e:
                    print("'" + dirname + "' exists in '" + dirroot + "'")

            for file in files:
                source_path = source + '/' + os.path.join(root[source_prefix:]
                                                          + '/'
                                                          + file)
                destination_path = (destination
                                    + '/' + os.path.join(root[source_prefix:]
                                                         + '/'
                                                         + file))

                try:
                    watermark = Image.open(source_path).copy()

                    draw = ImageDraw.Draw(watermark)
                    font = ImageFont.truetype("LiberationSans-Regular.ttf", 50)

                    # add watermark
                    text = message
                    left_offset = 5
                    bottom_offset = watermark.height - 5
                    anchor = "lb"
                    fill = (255, 255, 255, 50)
                    draw.text((left_offset, bottom_offset),
                              text,
                              font=font,
                              anchor=anchor,
                              fill=fill)

                    try:
                        watermark.save(destination_path)
                    except Exception as e:
                        print("File '" + destination_path + "' not exportable")

                except Exception as e:
                    print(e)
