from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import UserProfile
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile

def chat_view(request):
    return render(request, 'chat.html')

@csrf_exempt
def save_profile(request):
    if request.method == 'POST':
        try:
            # Debug print to see what data is received
            print("Received POST data:", request.POST)

            profile = UserProfile(
                name=request.POST.get('name', ''),
                email=request.POST.get('email', ''),
                hobbies=request.POST.get('hobbies', ''),
                favorite_book=request.POST.get('favorite_book', ''),
                career_goal=request.POST.get('career_goal', '')
            )
            profile.save()
            print(f"Profile saved successfully! ID: {profile.id}")
            return JsonResponse({'success': True, 'id': profile.id})
        except Exception as e:
            print(f"Error saving profile: {str(e)}")
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def profile_view(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    return render(request, 'profile.html', {'profile': profile})

def download_report(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    response = HttpResponse(f"""
        USER PROFILE REPORT\n\n
        Name: {profile.name}\n
        Email: {profile.email}\n
        Hobbies: {profile.hobbies}\n
        Favorite Book: {profile.favorite_book}\n
        Career Goals: {profile.career_goal}\n
    """, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{profile.name}_profile.txt"'
    return response