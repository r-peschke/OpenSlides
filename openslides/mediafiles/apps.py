from django.apps import AppConfig


class MediafilesAppConfig(AppConfig):
    name = 'openslides.mediafiles'
    verbose_name = 'OpenSlides Mediafiles'
    angular_site_module = True
    angular_projector_module = True
    js_files = ['js/mediafiles/base.js', 'js/mediafiles/site.js', 'js/mediafiles/projector.js']

    def ready(self):
        # Load projector elements.
        # Do this by just importing all from these files.
        from . import projector  # noqa

        # Import all required stuff.
        from openslides.utils.rest_api import router
        from .views import MediafileViewSet

        # Register viewsets.
        router.register('mediafiles/mediafile', MediafileViewSet)
