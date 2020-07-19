from django.views.generic import *
from .models import *
from .forms import *  # importing the view
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, logout

from django.shortcuts import render, redirect
from django.db.models import Q


class HomeView (TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bibek'] = 'I am bibek'
        context['blogs'] = Blog.objects.all()
        context['events'] = Event.objects.all()

        return context


class AboutView (TemplateView):
    template_name = 'about.html'


class ContactView (FormView):
    template_name = 'contact.html'
    form_class = MessageForm
    success_url = '/'

    def form_valid(self, form):    # for handling the data inserted into form

          #  cleaned for data passed with validation and csrf token
        sender = form.cleaned_data['sender']
        mobile = form.cleaned_data['mobile']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        print(sender, mobile, email, subject, message,
              '===================================================')
        Message.objects.create(name=sender, phone=mobile,
                               email=email, subject=subject, message=message)

        return super().form_valid(form)


class NepalView(TemplateView):
    template_name = 'nepal.html'


# listview is django generic view,it represents in bloglist.html
class BlogListView(ListView):
    template_name = 'bloglist.html'
    # or do as, model=blog , instead of queryset #queryset define the data to be sent to the html file(bloglist.html)
    queryset = Blog.objects.all()
    context_object_name = 'allblogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentform'] = CommentForms
        return context


# listview is django generic view,it represents in bloglist.html
class EventListView(ListView):
    template_name = 'eventlist.html'
    # or do as, model=blog , instead of queryset #queryset define the data to be sent to the html file(bloglist.html)
    queryset = Event.objects.all()
    context_object_name = 'allevent'


class NewsListView(ListView):
    template_name = 'newslist.html'
    queryset = News.objects.all()
    context_object_name = 'allnews'


class BlogCreateView(CreateView):
    template_name = 'blogcreate.html'
    form_class = BlogForm
    success_url = '/blog/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context

    def form_valid(self, form):    # for handling the data inserted into form
        title = form.cleaned_data['title']
        print(title, '===================================================')
        return super().form_valid(form)


# for details of blog
class BlogDetailView(DetailView):
    template_name = "blogdetail.html"
    # queryset = Blog.objects.all()
    model = Blog
    context_object_name = "blogdetail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentform'] = CommentForm
        blog_id = self.kwargs['pk']
        return context


class BlogUpdateView(UpdateView):

    template_name = 'blogcreate.html'
    model = Blog
    form_class = BlogForm
    success_url = '/blog/list/'                        # or  use ,queryset =


class BlogDeleteView(DeleteView):
    template_name = 'blogdelete.html'
    model = Blog       # for primary key model as of database is required
    success_url = '/blog/list/'


class NewsCreateView(CreateView):
    template_name = 'newscreate.html'
    form_class = NewsForm
    success_url = '/news/list/'


class NewsUpdateView(UpdateView):

    template_name = 'newscreate.html'
    model = News
    form_class = NewsForm
    success_url = '/news/list/'                        # or  use ,queryset =


class NewsDeleteView(DeleteView):
    template_name = 'newsdelete.html'
    model = News       # for primary key model as of database is required
    success_url = '/news/list/'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        uname = form.cleaned_data['username']
        pword = form.cleaned_data['password']
        print('*****************', uname, '********************')
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {

                'form': form,
                'error': 'Not authorized'

            })

        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')


class BlogCommentCreateView(CreateView):
    template_name = 'commentcreate.html'
    form_class = CommentForms
    success_url = '/'

    def from_valid(self, form):

        blog_id = self.kwargs['pk']
        blog = Blog.objects.get(id=blog_id)
        form.instance.blog = blog
        return super().form_valid(form)

    def get_success_url(self):
        blog_id = self.kwargs['pk']
        url = '/blog/' + str(blog_id) + '/'

        return url


class SearchView(TemplateView):
    template_name = 'searchlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get is done at base.html in form so do get(if method=post request.post hunxa )
        userkeyword = self.request.GET.get('search')
        searchresults = Blog.objects.filter(
            Q(title__icontains=userkeyword) | Q(contents__icontains=userkeyword))
        context["searchblogs"] = searchresults

        # fors news model search
        searchnews = News.objects.filter(Q(title__icontains=userkeyword) | Q(
            catagory__title__icontains=userkeyword) | Q(detail__icontains=userkeyword))
        context["searchednews"] = searchnews

        return context
