from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student, Parent
from django.contrib import messages
from django.db import IntegrityError



def add_student(request):
    if request.method == 'POST':
        admission_number = request.POST.get('admission_number', '').strip()

        if Student.objects.filter(admission_number=admission_number).exists():
            messages.error(request, f"Admission number '{admission_number}' already exists.")
            return render(request, 'students/add-student.html')

        try:
            print('request is heree.......,', request.POST)
            print("Type of request.POST:", type(request.POST))

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            student_id = request.POST.get('student_id')
            gender = request.POST.get('gender')
            date_of_birth = request.POST.get('date_of_birth')
            student_class = request.POST.get('student_class')
            religion = request.POST.get('religion')
            joining_date = request.POST.get('joining_date')
            admission_number = request.POST.get('admission_number')
            section = request.POST.get('section')
            student_image = request.POST.get('student_image')
            parent = request.POST.get('parent')


            father_name = request.POST.get('father_name')
            father_occupation = request.POST.get('father_occupation')
            father_mobile = request.POST.get('father_mobile')
            father_email = request.POST.get('father_email')
            mother_name = request.POST.get('mother_name')
            mother_email = request.POST.get('mother_email')
            mother_mobile = request.POST.get('mother_mobile')
            present_address = request.POST.get('present_address')
            permanent_address = request.POST.get('permanent_address')

            parent_data = Parent.objects.create(father_name=father_name,
                                        father_occupation=father_occupation,
                                        father_mobile=father_mobile,
                                        father_email=father_email,
                                        mother_name=mother_name,
                                        mother_email=mother_email,
                                        mother_mobile=mother_mobile,
                                        present_address=present_address,
                                        permanent_address=permanent_address
                                        )
            
            student_data = Student.objects.create(first_name=first_name,
                                                last_name=last_name,
                                                student_id=student_id,
                                                gender=gender,
                                                date_of_birth=date_of_birth,
                                                student_class=student_class,
                                                religion=religion,
                                                joining_date=joining_date,
                                                admission_number=admission_number,
                                                section=section,
                                                student_image=student_image,
                                                parent=parent_data
                                                )
            messages.success(request, f"Student '{first_name} {last_name}' added successfully.")
            return redirect('student_list')

        except IntegrityError as e:
            messages.error(request, f"Database error: {e}")
            return render(request, 'students/add-student.html')

        



    return render(request, 'students/add-student.html')

def student_list(request):

    student_list = Student.objects.select_related('parent').all()

    context = {
        'student_list':student_list
    }
    return render(request, 'students/students.html', context)

def edit_student(request):
    return render(request, 'students/edit-student.html')

def view_student(request, slug):
    try:
        student = Student.objects.get(student_id=slug)
        context = {
            'student': student
        }
        return render(request, 'students/student-details.html', context=context)
    except Student.DoesNotExist:
        messages.error(request, f"No student found with ID '{slug}'.")
        return render(request, 'students/student-details.html', context={})