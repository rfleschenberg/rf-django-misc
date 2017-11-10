from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory


def get_test_request(url='/', data=None, method='get', session_data=None,
                     user=None):
    """Get a test request for testing a Django view

       This is helpful if you want to test a view as an isolated unit, i.e. not
       with the usual Django test client. This function returns a test request
       generated by ``RequestFactory``, with the ``session`` and ``user``
       attributes set.

       :param url: The URL for the request
       :param data: Request data
       :param method: Request method
       :param session_data: Session data
       :param user: A user object
    """
    method_to_call = getattr(RequestFactory(), method)
    if data is None:
        data = {}
    if session_data is None:
        session_data = {}
    if user is None:
        user = AnonymousUser()
    request = method_to_call(url, data)
    request.session = session_data
    request.user = user
    return request