"""Set of reusable human tasks."""
from django.views import generic

from galahad.views import TaskViewMixin


__all__ = (
    'StartView',
    'UpdateView',
)


class StartView(TaskViewMixin, generic.CreateView):
    """
    Start a new process by a human with a view.

    Starting a process with a view allows users to provide initial data.

    Similar to Django's :class:`CreateView<django.views.generic.edit.CreateView>`
    but does not only create the process but also completes a tasks.
    """
    pass


class UpdateView(TaskViewMixin, generic.UpdateView):
    """
    Modify the process state and complete a human task.

    Similar to Django's :class:`UpdateView<django.views.generic.edit.UpdateView>`
    but does not only update the process but also completes a tasks.
    """
    pass