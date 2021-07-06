from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from django.utils.translation import ugettext_lazy as _


class CustomIndexDashboard(Dashboard):
    columns = 1

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(modules.LinkList(
            _('Поддержка'),
            children=[
                {
                    'title': _('При возникновении проблем писать'),
                    'url': 'Тут будет ссылка',
                    'external': True,
                },
            ],
            column=0,
            order=0
        ))
