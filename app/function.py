from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash  # 用于密码校验
from .models import db, User  # 导入数据库和 User 模型
