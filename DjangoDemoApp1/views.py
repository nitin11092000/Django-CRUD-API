from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from DjangoDemoApp1.models import Student


@api_view(['POST'])
def create(request):
    """
    Creates a Student Record
    """
    payload: dict = request.data

    try:
        name = payload.get('name')  # data['name']
        age = payload.get('age')
        marks = payload.get('marks')

        student_obj = Student(
            name=name,
            age=age,
            marks=marks
        )
        student_obj.save()
    except Exception:
        return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)

    return Response('Ok', status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list(request):
    """
    Return all student records
    """
    # Student.objects.get() -> model instance/obj Student(name='..', age='...',,,,)
    # Student.objects.all() -> queryset  [qs(name='nitin', age='12'), qs(name='siddhanth', age='12'), .....]
    # Student.objects.filter() -> queryset
    # Student.objects.all().values() -> converts queryset to list of dicts

    students = Student.objects.all().values()

    return Response(students, status=status.HTTP_200_OK)


@api_view(['GET'])
def retrieve(request, pk):
    """
    Retrieves a specific student record based on primary key given in the url
    """
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response('Does Not Exist', status=status.HTTP_404_NOT_FOUND)

    student_dict = model_to_dict(student)

    return Response(student_dict, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update(request, pk):
    """
    Updates an entire student record with pk specified in the url
    """
    payload = request.data

    new_name = payload.get('name')  # data['name']
    new_age = payload.get('age')
    new_marks = payload.get('marks')

    rows = Student.objects.filter(pk=pk).update(
        name=new_name,
        age=new_age,
        marks=new_marks
    )

    if rows > 0:
        return Response('Record Updated', status=status.HTTP_200_OK)
    else:
        return Response('No Record Updated', status=status.HTTP_200_OK)


@api_view(['PATCH'])
def partial_update(request, pk):
    """
    Does a partial update on a student record with pk specified in the url
    """
    payload = request.data

    new_marks = payload.get('marks')

    rows_count = Student.objects.filter(pk=pk).update(
        marks=new_marks
    )

    if rows_count > 0:
        return Response('Record Updated', status=status.HTTP_200_OK)
    else:
        return Response('No Record Updated', status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete(request, pk):
    """
    Deletes a record specified by pk in the url
    """
    is_deleted, rows_count = Student.objects.filter(pk=pk).delete()

    if is_deleted:
        return Response('Record Deleted', status=status.HTTP_200_OK)
    else:
        return Response('No Record Deleted', status=status.HTTP_200_OK)
