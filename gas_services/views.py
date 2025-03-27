from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import ServiceRequest
from django.utils.timezone import now
from .models import User

import json

@csrf_exempt
def submit_request(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.get(id=data['customer_id'])

            attachment = None
            if 'attachment' in request.FILES:
                file = request.FILES['attachment']
                file_name = default_storage.save(f'service_requests/{file.name}', ContentFile(file.read()))
                attachment = file_name

            service_request = ServiceRequest.objects.create(
                customer=user,
                service_type=data['service_type'],
                description=data['description'],
                attachment=attachment,
                status='pending'
            )
            return JsonResponse({'message': 'Service request submitted successfully', 'request_id': service_request.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    data = {
        'customer': service_request.customer.username,
        'service_type': service_request.service_type,
        'description': service_request.description,
        'status': service_request.status,
        'submitted_at': service_request.submitted_at.strftime('%Y-%m-%d %H:%M:%S'),
        'resolved_at': service_request.resolved_at.strftime('%Y-%m-%d %H:%M:%S') if service_request.resolved_at else None,
        'attachment': service_request.attachment.url if service_request.attachment else None
    }
    return JsonResponse(data)

def list_requests(request):
    requests = ServiceRequest.objects.all()
    data = [{'id': r.id, 'customer': r.customer.username, 'status': r.status} for r in requests]
    return JsonResponse({'requests': data})

# @csrf_exempt
# def register_user(request):
    # if request.method == 'POST':
    #     try:
    #         data = json.loads(request.body)
    #         username = data.get('username')
    #         password = data.get('password')
    #         email = data.get('email', '')

    #         if not username or not password:
    #             return JsonResponse({'error': 'Username and password are required'}, status=400)

    #         if User.objects.filter(username=username).exists():
    #             return JsonResponse({'error': 'Username already exists'}, status=400)

    #         user = User.objects.create_user(username=username, password=password, email=email)
    #         return JsonResponse({'message': 'User registered successfully', 'user_id': user.id})
    #     except Exception as e:
    #         return JsonResponse({'error': str(e)}, status=400)
    # return JsonResponse({'error': 'Invalid request'}, status=400)




@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email', '')
            first_name = data.get('first_name', '')
            last_name = data.get('last_name', '')

            if not username or not password:
                return JsonResponse({'error': 'Username and password are required'}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

            return JsonResponse({'message': 'User registered successfully', 'user_id': user.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)






### update status 
@csrf_exempt
def update_status(request, request_id):
    try:
        service_request = ServiceRequest.objects.get(id=request_id)
        data = json.loads(request.body)
        new_status = data.get('status')

        if new_status in ['resolved', 'cancelled']:
            service_request.status = new_status
            service_request.resolved_at = now()  # Explicitly update resolved_at
        else:
            service_request.status = new_status
            service_request.resolved_at = None  # Reset resolved_at

        service_request.save()
        return JsonResponse({
            'message': 'Status updated successfully',
            'resolved_at': service_request.resolved_at.strftime('%Y-%m-%d %H:%M:%S') if service_request.resolved_at else None
        })

    except ServiceRequest.DoesNotExist:
        return JsonResponse({'error': 'Service request not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



def get_user_info(request, customer_id):
    try:
        user = User.objects.get(id=customer_id)
        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)