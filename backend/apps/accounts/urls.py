from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import include, path

from apps.iamstudent.forms import StudentForm, StudentFormAndMail
from apps.iamstudent.models import Student
from apps.ineedstudent.forms import HospitalFormInfoCreate, HospitalFormInfoSignUp
from apps.ineedstudent.models import Hospital

from . import views

urlpatterns = [
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="registration/logout.html"),
        name="logout",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done_.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_change",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/password_change_form_.html"
        ),
        name="password_change_form",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form_.html", from_email=settings.NOREPLY_MAIL
        ),
        name="password_reset_form",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done_.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete_.html"
        ),
        name="password_reset_complete_",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm_.html",
            post_reset_login=True,
            success_url="/accounts/validate_email",
        ),
        name="password_reset_confirm_",
    ),
    path(
        "resend_validation_email/<email>",
        views.resend_validation_email,
        name="resend_validation_email",
    ),
    path(
        "login/",
        views.CustomLoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("", include("django.contrib.auth.urls")),
    path("validate_email", views.validate_email, name="validate_email"),
    path("profile_redirect", views.ProfileDashboardRedirect.as_view(), name="profile_redirect"),
    path("login_redirect", views.LoginRedirect.as_view(), name="login_redirect"),
    path("delete_me_ask", views.delete_me_ask, name="delete_me_ask"),
    path("delete_me", views.delete_me, name="delete_me"),
    path(
        "signup_student",
        views.ParticipantSignupView.as_view(
            template_signup="student_signup.html",
            template_thanks_for_registering="/iamstudent/thanks",
            signup_form=StudentFormAndMail,
            save_form=StudentForm,
            subject_template="registration/password_reset_email_subject.txt",
            model=Student,
            mail_template="registration/password_set_email_.html",
        ),
        name="student_signup",
    ),
    path(
        "signup_hospital",
        views.ParticipantSignupView.as_view(
            template_signup="hospital_signup.html",
            template_thanks_for_registering="/iamstudent/thanks",
            signup_form=HospitalFormInfoSignUp,
            save_form=HospitalFormInfoCreate,
            subject_template="registration/password_reset_email_subject.txt",
            model=Hospital,
            mail_template="registration/password_set_email_hospital.html",
        ),
        name="hospital_signup",
    ),
    path("profile_student", views.StudentEditProfileView.as_view(), name="edit_student_profile"),
    path("profile_hospital", views.HospitalEditProfileView.as_view(), name="edit_hospital_profile"),
    path("approve_hospitals", views.ApproveHospitalsView.as_view(), name="approve_hospitals"),
    path(
        "change_hospital_approval/<str:uuid>/",
        views.change_hospital_approval,
        name="change_hospital_approval",
    ),
    path("delete_hospital/<str:uuid>/", views.delete_hospital, name="delete_hospitall"),
    path("count", views.UserCountView.as_view(), name="count"),
    path("change_activation", views.change_activation_ask, name="activate_student_ask"),
    path("change_activation_confirm", views.change_activation, name="activate_student"),
    path("view_newsletter/<uuid>", views.NewsletterDetailView.as_view(), name="view_newsletter"),
    path("new_newsletter", views.new_newsletter, name="new_newsletter"),
    path("list_newsletter", views.NewsletterListView.as_view(), name="list_newsletter"),
    path("did_see_newsletter/<uuid>/<token>", views.did_see_newsletter, name="did_see_newsletter"),
    path("stats", views.view_statistics, name="statistics"),
    path("profile_staff", views.StaffProfileView.as_view(), name="staff_profile"),
    path("i18n/", include("django.conf.urls.i18n")),
]
