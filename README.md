<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>
<h2 align="center">
    PLATFORM ERP
</h2>
<div align="center">
    <p align="center">
        <img src="docs/logo/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/logo/fitdnu_logo.png" alt="AIoTLab Logo" width="180"/>
        <img src="docs/logo/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>
## 1. Tổng quan hệ thống
Hệ thống được xây dựng với mục tiêu cung cấp một giải pháp ERP toàn diện, tập trung vào việc số hóa quy trình quản lý dữ liệu khách hàng và luân chuyển văn bản nội bộ. Hệ thống đóng vai trò là nền tảng trung tâm giúp doanh nghiệp nâng cao hiệu suất làm việc, tối ưu hóa quy trình vận hành và đảm bảo an toàn, bảo mật thông tin.

## 2. Các chức năng chính
- Quản lý nhân sự:Thực hiện đầy đủ các thao tác CRUD (Thêm, Sửa, Xóa, Tìm kiếm) dữ liệu nhân sự.
<img width="1803" height="897" alt="image" src="https://github.com/user-attachments/assets/b94e731d-ebbd-42b7-9a0d-1187aa68c769" />
- Quản lý khách hàng: Thực hiện đầy đủ các thao tác CRUD (Thêm, Sửa, Xóa, Tìm kiếm) dữ liệu khách hàng.
<img width="1782" height="740" alt="image" src="https://github.com/user-attachments/assets/924c1fd5-7dec-4505-9834-2a91f9ead25f" />
- Quản lý văn bản: Hệ thống lưu trữ, cập nhật trạng thái, theo dõi luồng xử lý và tìm kiếm văn bản.
<img width="1796" height="672" alt="image" src="https://github.com/user-attachments/assets/b19be3d3-079d-4090-a138-bb089d6756af" />
- Trợ lý AI: Tích hợp trí tuệ nhân tạo cho phép người dùng tra cứu thông tin bằng ngôn ngữ tự nhiên, hỗ trợ tự động hóa quy trình và nâng cao hiệu suất làm việc.<br>
  
<img width="454" height="174" alt="image" src="https://github.com/user-attachments/assets/7456f3ff-287c-4bce-942b-d526752a1576" />

<img width="173" height="222" alt="image" src="https://github.com/user-attachments/assets/075fd895-4a8f-4e84-af72-194ff07622f4" />

## 📖 3. Giới thiệu
Platform ERP được áp dụng vào học phần Thực tập doanh nghiệp dựa trên mã nguồn mở Odoo. 

## 🔧 4. Các công nghệ được sử dụng
<div align="center">

### Hệ điều hành
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
### Công nghệ chính
[![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![XML](https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.w3.org/XML/)
### Cơ sở dữ liệu
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
</div>

## 🚀 5. Các project đã thực hiện dựa trên Platform

Một số project sinh viên đã thực hiện:
- #### [Khoá 15](./docs/projects/K15/README.md)
- #### [Khoá 16](./docs/projects/K16/README.md)
- #### [Khoá 17](./docs/projects/K17/README.md)
## ⚙️ 6. Cài đặt

### 6.1. Cài đặt công cụ, môi trường và các thư viện cần thiết

#### 6.1.1. Tải project.
```
git clone https://github.com/FIT-DNU/Business-Internship.git
```
#### 6.1.2. Cài đặt các thư viện cần thiết
Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
#### 6.1.3. Khởi tạo môi trường ảo.
- Khởi tạo môi trường ảo
```
python3.10 -m venv ./venv
```
- Thay đổi trình thông dịch sang môi trường ảo
```
source venv/bin/activate
```
- Chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu
```
pip3 install -r requirements.txt
```
### 6.2. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.
```
sudo docker-compose up -d
```
### 6.3. Setup tham số chạy cho hệ thống
Tạo tệp **odoo.conf** có nội dung như sau:
```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5431
xmlrpc_port = 8069
```
Có thể kế thừa từ file **odoo.conf.template**
### 6.4. Chạy hệ thống và cài đặt các ứng dụng cần thiết
Lệnh chạy
```
python3 odoo-bin.py -c odoo.conf -u all
```
Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

## 📝 7. License

© 2024 AIoTLab, Faculty of Information Technology, DaiNam University. All rights reserved.
## 📝 8. Poster
<img width="507" height="732" alt="image" src="https://github.com/user-attachments/assets/7c151463-7ec8-4096-986c-3c80458be1c8" />

---

    
