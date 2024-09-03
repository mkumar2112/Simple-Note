from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from bson import ObjectId

# Create your views here.

class NoteAPIView(APIView):

    def get(self, request, id=None): # Get Method to extract data from database
        title = request.query_params.get('title', None)
        if id: # Getting Data with id
            try:
                note_instance = Notes.objects.filter(_id=ObjectId(id))
                serialized_note = Noteserializer(note_instance, many=True)
                return Response({'status': 200, 'message': 'Valid Id', 'data': serialized_note.data})
            except Notes.DoesNotExist:
                return Response({"status": 404, 'error': 'Note not found'}, status=404)
            except Exception as e:
                print(e)
                return Response({"status": 500, 'error': 'Server error'}, status=500)

        elif title : # Getting data with searching in title column and return result.
            try:
                title = request.query_params.get('title', None)
                # Fetch notes with only the '_id' and 'title' fields
                notes = Notes.objects.filter(title__icontains=title).values('_id', 'title', 'body')
                note_list = [ {'_id': str(note['_id']), 'title': note['title'], 'body': note['body'], 'updateLink': f"http://127.0.0.1:8000/notes/{str(note['_id'])}" } for note in notes] # Creating list of our data
                return Response({'status': 200, 'message': f'Search results for title containing "{title}"', 'data': list(note_list)})
            except Exception as e:
                print(e)
                return Response({"status": 500, 'error': 'Server error'}, status=500)
        else: # Return All data
            try: 
                notes = Notes.objects.all()
                serialized_notes = Noteserializer(notes, many=True)
                return Response({'status': 200, 'message': 'Getting All Notes', 'data': serialized_notes.data})
            except Exception as e:
                print(e)
                return Response({"status": 500, 'error': 'Server error'}, status=500)

    def post(self, request): # Send data to Database
        serializer = Noteserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 400, 'message': 'Validation error', 'error': serializer.errors}, status=400)
        serializer.save()
        return Response({'status': 201, 'message': 'Note created', 'data': serializer.data}, status=201)

    def put(self, request, id=None): # Update data from database
        note_id = id or request.data.get('id')
        if not note_id:
            return Response({'status': 400, 'error': 'ID not provided'}, status=400)

        try:
            note_instance = Notes.objects.get(_id=ObjectId(note_id))
            serializer = Noteserializer(note_instance, data=request.data)
            if not serializer.is_valid():
                return Response({'status': 400, 'message': 'Validation error', 'error': serializer.errors}, status=400)
            serializer.save()
            return Response({'status': 200, 'message': 'Note updated successfully', 'data': serializer.data}, status=200)
        except Notes.DoesNotExist:
            return Response({'status': 404, 'error': 'Note not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({'status': 500, 'error': 'Server error'}, status=500)

    def patch(self, request, id=None): # Update data from database
        note_id = id or request.data.get('id')
        if not note_id:
            return Response({'status': 400, 'error': 'ID not provided'}, status=400)

        try:
            note_instance = Notes.objects.get(_id=ObjectId(note_id))
            serializer = Noteserializer(note_instance, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status': 400, 'message': 'Validation error', 'error': serializer.errors}, status=400)
            serializer.save()
            return Response({'status': 200, 'message': 'Note updated successfully', 'data': serializer.data}, status=200)
        except Notes.DoesNotExist:
            return Response({'status': 404, 'error': 'Note not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({'status': 500, 'error': 'Server error'}, status=500)

    def delete(self, request, id=None): # Delete data from database.
        note_id = id or request.data.get('id')
        if not note_id:
            return Response({'status': 400, 'error': 'ID not provided'}, status=400)

        try:
            note_instance = Notes.objects.get(_id=ObjectId(note_id))
            note_instance.delete()
            return Response({'status': 200, 'message': 'Note has been deleted'}, status=200)
        except Notes.DoesNotExist:
            return Response({'status': 404, 'error': 'Note not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({"status": 500, 'error': 'Server error'}, status=500)