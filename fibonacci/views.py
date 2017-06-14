from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fibonacci import calculator


@api_view(['GET'])
def fibonacci_request(request):

    from_data = None
    try:
        from_data = request.query_params['from']
    except KeyError:
        return Response({"error": "From field is required"}, status=status.HTTP_400_BAD_REQUEST)

    to_data = None
    try:
        to_data = request.query_params['to']
    except KeyError:
        return Response({"error": "To field is required"}, status=status.HTTP_400_BAD_REQUEST)

    fro = 0
    to = 0

    try:
        fro = int(from_data)
    except ValueError:
        return Response({"error": "From field must be a number"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        to = int(to_data)
    except ValueError:
        return Response({"error": "To field must be a number"}, status=status.HTTP_400_BAD_REQUEST)

    if fro < 0 or to < 0:
        return Response({"error": "From and to must be non-negative"}, status=status.HTTP_400_BAD_REQUEST)

    if fro > to:
        return Response({"error": "From value must be less or equal than to value"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"response": calculator.calculate_fibonacci(fro, to)})
