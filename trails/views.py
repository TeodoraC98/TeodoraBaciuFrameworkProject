from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Trail,Participant,Comment
from .forms import CreateCommentForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
)
def bad_request(request):
    return render(request,"trails/403.html")
   
class TrailListView(ListView):
  model = Trail
  template_name = 'app/index.html' 
  context_object_name = 'trails' 
  # ordering = ['-date_posted'] 


class TrailDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
   permission_required = ('trails.can_view_trail')
   login_url='bad_request'
   model =Trail



class TrailCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    permission_required = ('trails.add_trail')
    model = Trail
    fields=['title','difficulty_level','type','duration'
            ,'distance','meeting_point','date','description']
    raise_exception = True
    def form_valid(self, form):
       form.instance.coordinator = self.request.user
       return super().form_valid(form)
  
class TrailUpdateView(LoginRequiredMixin, UpdateView,UserPassesTestMixin): 
    permission_required ='trails.change_trail'
    model = Trail
    fields=['title','difficulty_level','type','duration'
            ,'distance','meeting_point','date','description']
     
    def form_valid(self, form):
        form.instance.coordinator = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        trail = self.get_object()
        if self.request.user == trail.coordinator:
            return True
        return False
    
class TrailDeleteView(LoginRequiredMixin, DeleteView,UserPassesTestMixin): 
    model = Trail
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.coordinator:
            return True
        return False
    

def join(request):
   if request.method == 'POST':
       user=request.user
       id_trail=int(request.POST['join_trail'])
       trail=Trail.objects.get(id=id_trail)
       all_participants=[]
       all_participants = Participant.objects.all().filter(
          trail_id=id_trail).values_list('user_id',flat=True)
       if not user.id in all_participants:
         participant=Participant.objects.create(trail=trail,user=user)
         participant.save()
       return redirect('trail-detail',id_trail)
   return redirect('index')
    
       
def add_comment(request):
    if request.method=='POST':
       comment=Comment()
       comment.user=request.user
       trail_id=int(request.POST['add_comment_trail-id'])
       comment.trail_id=trail_id
       comment.comment=request.POST['add_comment_trail-text']
       comment.save()
    return redirect('trail-detail',trail_id)
   