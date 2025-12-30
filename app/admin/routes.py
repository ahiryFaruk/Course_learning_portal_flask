from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.courses.models import Course

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/")
def dashboard():
    courses = Course.query.all()
    return render_template("admin/dashboard.html", courses=courses)


@admin_bp.route("/add-course", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        course = Course(
            title=request.form["title"],
            description=request.form["description"],
            duration=request.form["duration"],
            level=request.form["level"]
        )
        db.session.add(course)
        db.session.commit()
        return redirect(url_for("admin.dashboard"))

    return render_template("admin/course_form.html")


@admin_bp.route("/edit-course/<int:course_id>", methods=["GET", "POST"])
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)

    if request.method == "POST":
        course.title = request.form["title"]
        course.description = request.form["description"]
        course.duration = request.form["duration"]
        course.level = request.form["level"]
        db.session.commit()
        return redirect(url_for("admin.dashboard"))

    return render_template("admin/course_form.html", course=course)


@admin_bp.route("/delete-course/<int:course_id>", methods=["POST"])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for("admin.dashboard"))
