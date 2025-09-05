from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Post
from django.http import JsonResponse

# 📝 All blog posts list
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # latest first
    return render(request, 'blog/post_list.html', {'posts': posts})

# 📄 Single post details
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 📩 Contact form
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Collect form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # For now: print data in console (later: save to DB or send email)
            print("📩 Contact Form Submission:")
            print(f"Name: {name}, Email: {email}, Message: {message}")

            # Redirect to success page
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'blog/contact_form.html', {'form': form})

# ✅ Success page
def contact_success(request):
    return render(request, 'blog/contact_success.html')

#api function
def post_list_api(request):
    all_posts = Post.objects.all()
    context = {'all_the_posts': all_posts}
    data = {
        "posts": 
            list(all_posts.values(
                'pk', 
                'title', 
                'content', 
                'author__username', 
                'created_at'))
    }
    return JsonResponse(data)