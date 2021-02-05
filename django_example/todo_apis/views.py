from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from todo.models import Task
from todo_apis.serializers import TaskSerializer


@api_view(['GET', 'POST'])
def tasks_apiview(request, format=None):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def task_apiview(request, pk, format=None):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'status': 'notfound'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sr = TaskSerializer(task)
        return Response(sr.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        sr = TaskSerializer(task, data=request.data)
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status.HTTP_200_OK)
        else:
            return Response(sr.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        sr = TaskSerializer(task, data=request.data, partial=True)
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status.HTTP_200_OK)
        else:
            return Response(sr.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        resp = {
            'deleted': 'ok'
        }
        return Response(resp, status.HTTP_204_NO_CONTENT)
