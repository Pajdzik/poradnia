from django.db.models import F, Func, IntegerField, Case, Sum, When
from braces.views import JSONResponseMixin
from django.views.generic import TemplateView
from django.views.generic import View
from cases.models import Case as CaseModel


class ApiListViewMixin(JSONResponseMixin):
    def get(self, request, *args, **kwargs):
        return self.render_json_response(list(self.get_object_list()))


class StatsCaseView(TemplateView):
    template_name = 'stats/cases.html'


class StatsCaseApiView(ApiListViewMixin, View):
    def get_object_list(self):
        return (
            CaseModel.objects.annotate(
                                        month=Func(F('created_on'),
                                                   function='month',
                                                   output_field=IntegerField())
            ).annotate(
                        year=Func(F('created_on'),
                                  function='year',
                                  output_field=IntegerField())
            ).values('month', 'year')
            .annotate(
                count_open=Sum(
                    Case(
                        When(status=CaseModel.STATUS.free, then=1),
                        default=0,
                        output_field=IntegerField()
                    )
                ),
                count_assigned=Sum(
                    Case(
                        When(status=CaseModel.STATUS.assigned, then=1),
                        default=0,
                        output_field=IntegerField()
                    )
                ),
                count_closed=Sum(
                    Case(
                        When(status=CaseModel.STATUS.closed, then=1),
                        default=0,
                        output_field=IntegerField()
                    )
                )
            ).values('month', 'year', 'count_open', 'count_assigned', 'count_closed')
            .order_by(F('year'), F('month'))
        )
