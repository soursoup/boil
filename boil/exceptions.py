class BoilError(Exception):

    message = "An unknown exception occurred."

    def __init__(self, **kwargs):
        msg = self.message % kwargs
        super(BoilError, self).__init__(msg)


class PlateNotFound(BoilError):

    message = "Plate '%(name)s' not found."


class ArtifactAlreadyExists(BoilError):

    message = "Artifact '%(name)s' already exists in target directory."
