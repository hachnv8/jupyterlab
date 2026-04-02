# JupyterLab Test Project

Dự án này chứa các script mẫu để test việc chuyển đổi kết nối Database (SQLite) trong JupyterLab.

## 1. Yêu cầu hệ thống
- Python 3.x
- Git

## 2. Hướng dẫn cài đặt (Trên máy mới)

Nếu bạn vừa clone code về máy mới, hãy làm theo các bước sau:

### Bước 1: Cài đặt thư viện cần thiết
Mở terminal tại thư mục dự án và chạy lệnh:
```bash
pip install -r requirements.txt
```

### Bước 2: Tạo dữ liệu mẫu (Database)
Vì các file `.sqlite` không được đẩy lên Git, bạn cần chạy script sau để tạo lại 2 database test:
```bash
python init_test_dbs.py
```

### Bước 3: Khởi chạy JupyterLab
Chạy lệnh sau để mở giao diện JupyterLab:
```bash
python -m jupyterlab
```

## 3. Cấu trúc thư mục
- `db_connection.py`: Logic kết nối database. 
- `init_test_dbs.py`: Script khởi tạo database mẫu.
- `test_connection.ipynb`: Notebook mẫu để chạy thử nghiệm.
- `requirements.txt`: Danh sách thư viện cần cài đặt.
- `.gitignore`: Các file không được đẩy lên Git (như database, cache).
