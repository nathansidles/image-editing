from abc import ABC, abstractmethod


class Editor(ABC):

    @abstractmethod
    def watermark(self, source: str, destination: str):
        """Traverses the source directory recursively, creates a destination
        directory, and copies all images from the source directories into the
        destination directories, adding a watermark and preserving file
        structure.

        Keyword arguments:
        source -- (str) the source directory
        destination -- (str) the destination directory
        """
        pass
