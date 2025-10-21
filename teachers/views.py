from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher
from .forms import TeacherForm
from django.contrib import messages


# List all teachers
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

# Add teacher
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher-list')
    else:
        form = TeacherForm()
    return render(request, 'teachers/add_teacher.html', {'form': form})



def view_teacher(request, slug):
    print('Request coming into view_teacher function...')
    try:
        print('inside the try block......')
        teacher = Teacher.objects.get(slug=slug)
        print(teacher, 'data is here...')
        context = {'teacher': teacher}
        print(context, 'teacher context is here...')
        return render(request, 'teachers/teacher-details.html', context)
    except Teacher.DoesNotExist:
        messages.error(request, f"No teacher found with ID '{slug}'.")
        return render(request, 'teachers/teacher-details.html', {})
    
# Edit teacher
def edit_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher-list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/edit_teacher.html', {'form': form, 'teacher': teacher})

# Delete teacher
def delete_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher-list')
    return render(request, 'teachers/delete_teacher.html', {'teacher': teacher})

def teacher_dashboard(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)

    # Example dynamic stats (replace with real data later)
    total_classes = 6
    total_students = 60
    total_lessons = 50
    total_hours = 20
    lesson_progress = int((30 / total_lessons) * 100)  # Example progress

    context = {
        'teacher': teacher,
        'total_classes': total_classes,
        'total_students': total_students,
        'total_lessons': total_lessons,
        'total_hours': total_hours,
        'lesson_progress': lesson_progress,
        'completed_lessons': 30,
    }
    return render(request, 'teachers/teacher-dashboard.html', context)