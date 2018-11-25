from rest_framework import pagination


class DynamicPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page-size'
    max_page_size = 10000

    def get_page_size(self, request):
        """
        make disabling pagination possible
        :param request:
        :return:
        """
        if self.page_size_query_param:
            page_size = min(int(request.query_params.get(self.page_size_query_param, self.page_size)), self.max_page_size)
            if page_size > 0:
                return page_size
            elif page_size == 0:
                return None
            else:
                pass
        return self.page_size


class LargeResultsSetPagination(DynamicPagination):
    page_size = 1000
    page_size_query_param = 'page-size'
    max_page_size = 10000
