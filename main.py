'''
1. Chỉ ra lỗi bằng test case cụ thể
    test 1:
        id = 3, student_id = "SV001", course_id = 1

        Kết quả: API vẫn tạo bản ghi mới
        kết quả mong muốn: báo lỗi nếu đăng ký trùng khóa học
        Lỗi phát hiện: không kiểm tra trùng đăng ký
    test 2:
        id = 4, student_id="SV002" course_id=1

        kết quả: vẫn đăng ký được khóa học
        Kết quả đúng mong muốn: báo lỗi khi kiểm tra mã bài học đã đăng ký
        Lỗi phát hiện: không kiểm tra trùng mã khóa học

'''
# 2. Sửa lại source code
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
enrollments = [
    {
        "id": 1,
        "student_id": "SV001",
        "course_id": 1
    },
    {
        "id": 2,
        "student_id": "SV002",
        "course_id": 1
    }
]
class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: int
@app.post("/enrollments")
def create_enrollment(enrollment: EnrollmentCreate):
    for course in enrollments:
        if course['student_id'] == enrollment.student_id and course['course_id'] == enrollment.course_id:
            raise HTTPException (status_code=400, detail="khóa học đã được đăng ký")

    new_enrollment = {
        "id": len(enrollments) + 1,
        "student_id": enrollment.student_id,
        "course_id": enrollment.course_id
    }
    enrollments.append(new_enrollment)
    return {
        "message": "Enroll successfully",
        "data": new_enrollment
    }