import mistune

from .models import Job, Education

from utils.http_tools import SuccessResponse


def query_resume(request):
    job_qs = Job.objects.all()
    job_list = []
    for job in job_qs:
        job_list.append({
            'company_name': job.company_name,
            'company_site': job.company_site,
            'start_dt': job.start_dt,
            'end_dt': job.end_dt,
            'title': job.title,
            'product': mistune.markdown(job.product),
            'duties': job.duties,
            'tech_stack': mistune.markdown(job.tech_stack),
        })

    education_qs = Education.objects.all()
    education_list = []
    for education in education_qs:
        education_list.append({
            'school_name': education.school_name,
            'school_site': education.school_site,
            'start_dt': education.start_dt,
            'end_dt': education.end_dt,
            'degree': education.degree,
            'major': education.major,
            'course': education.course,
        })

    return SuccessResponse({
        'job_list': job_list,
        'education_list': education_list,
    })
