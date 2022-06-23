from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogAuthor, BlogComment
from django.views import generic
from django.urls import reverse


def index(request):
    return render(request, 'blog/index.html')


class BlogsView(generic.ListView):
    model = Blog
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs_list'
    paginate_by = 5

    # def get_queryset(self):   # Use as an alternative to Class Meta: in Models.
    #     """Return the last five published blogs."""
    #     return Blog.objects.order_by('-post_date')[:5]


class BloggersView(generic.ListView):
    model = BlogAuthor
    template_name = 'blog/bloggers.html'
    context_object_name = 'bloggers_list'


class BlogsDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blogsdetails.html'

    # def get_queryset(self):   #  Same as 'model = Blog'  # Use get_queryset(self) here for overriding method
    #     queryset = super(BlogsDetailView, self).get_queryset()
    #     queryset = queryset.order_by('author_name')
    #     return queryset


class BloggersDetailView(generic.DetailView):
    model = BlogAuthor
    template_name = 'blog/bloggersdetails.html'


class CommentView(LoginRequiredMixin, generic.CreateView):
    """
        Form for adding a blog comment. Requires login.
    """
    model = BlogComment
    fields = ['comment_desc']

    def get_context_data(self, **kwargs):
        """
            Add associated blog to form template so can display its title in HTML.
        """
        # You will also need to pass the name of the blog post to the comment page in the context given below.
        # Call the base implementation first to get a context
        context = super(CommentView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['Blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # ('pk' is a blog id passed in from the URL/URL configuration).
        return context

    def form_valid(self, form):
        """
            Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.user = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(CommentView, self).form_valid(form)

    def get_success_url(self):
        """
            After posting comment return to associated blog.
        """
        return reverse('blog:blogsdetails', kwargs={'pk': self.kwargs['pk'], })


class CommentUpdateView(generic.UpdateView):
    model = BlogComment
    fields = ['comment_desc']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('blog:blogsdetails', kwargs={'pk': self.object.blog.pk})


class CommentDeleteView(generic.DeleteView):
    model = BlogComment

    def get_success_url(self):
        return reverse('blog:blogsdetails', kwargs={'pk': self.object.blog.pk})

