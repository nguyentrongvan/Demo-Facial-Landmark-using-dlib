# Demo-Facial-Landmark-using-dlib

# Mô tả:
- Mã nguồn này thực hiện việc xây dựng một demo cơ bản về xác định các điểm Facial Landmark.  
- Hai thư viện chính được sử dụng là dlib và opencv-python. Trong đó:
-- dlib: thư viện hỗ trợ xác định Facial Landmark.  
- - opencv-python: dùng để xác định khuôn mặt.

# Tổ chức:
- `source.py`: source code.
- `data.zip`: chứa 2 file
- - `shape_predictor_68_landmarks.dat`: file chứa điểm neo.
- - `demo.mp4`: clip demo được dựng sẵn.

# Hướng dẫn chạy:
- Đầu tiên nếu chưa cài đặt 2 thư viện trên, cần cài đặt (thử nghiệm trên linux):
- - dilb:
```
$ sudo apt-get  update

$ sudo apt-get  install build-essential cmake
$ sudo apt-get  install libopenblas-dev liblapack-dev
$ sudo apt-get  install libx11-dev libgtk-3-dev
$ sudo apt-get  install python3-dev python3-pip
$ sudo apt-get install libpng16-dev libjpeg9-dev libjpeg9

$ pip3 install dlib
```
- - opencv-python:
```
$ sudo apt-get install opencv-python
```
- Dẫn file `shape_predictor_68_landmarks.dat` cùng thư mục với `source.py`.
- Lệnh run:
```
$ python3 source.py
```
# Nguồn tham khảo:
- https://blog.vietnamlab.vn/2018/04/24/dlib-phan-2-xac-dinh-facial-landmark-voi-dlib-va-python-2/  
- https://thorpham.github.io/blog/2018/04/20/face-landmark/
