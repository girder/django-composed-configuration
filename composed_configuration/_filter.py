from typing import Type

from ._base import ComposedConfiguration, ConfigMixin


class FilterMixin(ConfigMixin):
    """
    Configure Django-filter.

    This requires the `django-filter` package to be installed.
    """

    @staticmethod
    def mutate_configuration(configuration: Type[ComposedConfiguration]) -> None:
        configuration.INSTALLED_APPS += ['django_filters']
