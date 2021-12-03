from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from .models import Bank, Branch
from .forms import BankDetailsForm


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, There..!'}
        return Response(content)


class Banks(APIView):
     permission_classes = (IsAuthenticated,)

     default_per_page = 10

     def make_record(self, record):
         return {
             'id': record.id,
             'name': record.name
         }

     def get(self, request):
         try:
             query = Bank.objects.all().order_by('-id')
         except Exception as e:
             error = {
                 'error': True,
                 'message': 'An error occurred during querying..!',
                 'exception': str(e)
             }

             return Response(error)

         else:
             get = request.GET.get

             self.per_page = int(get("per_page", self.default_per_page))

             self.page = int(get("page", 1))

             paginator = Paginator(query, self.per_page)

             page = paginator.page(self.page)

             records = page.object_list

             data = [self.make_record(record) for record in records]

             success = {
                 'error': False,
                 'last_page': paginator.num_pages,
                 'from': page.start_index(),
                 'current_page': self.page,
                 'per_page': self.per_page,
                 'to': page.end_index(),
                 'data': data
             }

             return Response(success)


class BranchDetailsView(APIView):

    permission_classes = (IsAuthenticated,)

    form_class = BankDetailsForm

    def post(self, request):

        form = self.form_class(request.POST)

        if not form.is_valid():
            error_data = {
                'error': True,
                'message': 'form error..!',
                'errors': form.errors
            }

            return Response(error_data)

        ifsc = form.cleaned_data.get('ifsc_code')

        try:
            query = Branch.objects.get(ifsc=ifsc)
        except Exception as e:
            error_data = {
                'error': True,
                'message': 'An error occurred during querying..!',
                'exception': str(e)
            }

            return Response(error_data)
        else:
            bank_data = {
                'id': query.id,
                'ifsc': query.ifsc,
                'bank': {
                    'id': query.bank.id,
                    'name': query.bank.name
                },
                'branch': query.branch,
                'address': query.address,
                'city': query.city,
                'district': query.district,
                'state': query.state,
            }

            success_data = {
                'error': False,
                'data': bank_data
            }

            return Response(success_data)


class BankBranchesListView(APIView):

    permission_classes = (IsAuthenticated,)
    default_per_page = 10

    def make_record(self, record):
        bank_data = {
            'id': record.id,
            'ifsc': record.ifsc,
            'bank': {
                'id': record.bank.id,
                'name': record.bank.name
            },
            'branch': record.branch,
            'address': record.address,
            'city': record.city,
            'district': record.district,
            'state': record.state,
        }
        return bank_data

    def get(self, request):

        get = request.GET.get

        bank_name = get('bank_name')
        city = get('city')

        try:
            query = Branch.objects.all().order_by('-id')
            if bank_name:
                query = query.filter(bank__name__contains=bank_name)
            if city:
                query = query.filter(city__contains=city)
        except Exception as e:
            error_data = {
                'error': True,
                'message': 'An error occurred during querying..!',
                'exception': str(e)
            }

            return Response(error_data)
        else:

            self.per_page = int(get("per_page", self.default_per_page))

            self.page = int(get("page", 1))

            paginator = Paginator(query, self.per_page)

            page = paginator.page(self.page)

            records = page.object_list

            data = [self.make_record(record) for record in records]

            success = {
                'error': False,
                'last_page': paginator.num_pages,
                'from': page.start_index(),
                'current_page': self.page,
                'per_page': self.per_page,
                'to': page.end_index(),
                'data': data
            }

            return Response(success)

