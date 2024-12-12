import abc


class MetadataExtractor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def extract_metadata(self):
        pass

class MetadataExtractorImpl(MetadataExtractor):
    def __init__(self):
        pass

    def extract_metadata(self):
        pass