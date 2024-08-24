from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
import json

# In-memory data structures
users = {}
notes = {}

@csrf_exempt
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if username in users:
            return JsonResponse({'error': 'Username already exists'}, status=400)

        users[username] = {'email': email, 'password': password, 'notes': []}
        return JsonResponse({'message': 'User registered successfully'})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if username not in users:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        
        if users[username]['password'] != password:
            return JsonResponse({'error': 'Invalid username or password'}, status=400)

        return JsonResponse({'message': 'Login successful', 'notes': users[username]['notes']})


@csrf_exempt
def add_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        note_content = data.get('note')

        if username not in users:
            return JsonResponse({'error': 'User does not exist'}, status=404)

        note_id = len(users[username]['notes']) + 1
        timestamp = now().isoformat()
        note = {'id': note_id, 'content': note_content, 'timestamp': timestamp}

        users[username]['notes'].append(note)
        return JsonResponse({'message': 'Note added successfully', 'note': note})
