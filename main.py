# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2016-08-21
# Message：余时锐文件重命名v3.0


import os

import sys


# 导入正则
import re

# 字符转换
from urllib.parse import unquote

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *




# 导入ui文件
from Ui_main import Ui_MainWindow

# 图片
import image_rc

# 暗黑主题
import qdarkstyle


# 文件路径名字后缀分离
def fileFenli(file_path):
    # 文件路径，文件名分离
    filepath, tempfilename = os.path.split(file_path)
    # print(filepath, tempfilename)
    # D:/test test.py

    # 文件名，扩展名分离
    filename, extension = os.path.splitext(tempfilename)
    # print(filename, extension)
    # test .py

    return {'路径': filepath, '文件名': tempfilename, '后缀': extension}


# 重命名
class ReName(QMainWindow, Ui_MainWindow):
    # 构造函数
    def __init__(self, parent=None):
        # 调用父类构造函数
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 经典暗黑主题
        qApp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # 窗口置顶
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # 图标，QIcon作为参数(相对/绝对路径)
        self.setWindowIcon(QIcon(':/yu/yu.ico'))

        # 标题
        self.setWindowTitle('余时锐文件重命名v3.0')

        # 不能修改表格内容
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 表格列宽
        # self.tableWidget.setColumnWidth(0, 100)
        # self.tableWidget.setColumnWidth(1, 100)
        # self.tableWidget.setColumnWidth(2, 50)

        # 表格0行
        self.tableWidget.setRowCount(0)

        # 表格3列
        self.tableWidget.setColumnCount(3)

        # 水平列名([列表])
        self.tableWidget.setHorizontalHeaderLabels(['原文件名', '新文件名', '状态'])

        # 表头自适应伸缩
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 自动调整列宽
        self.tableWidget.resizeColumnsToContents()

        # 调用Drops方法
        self.setAcceptDrops(True)

        # 文件路径空列表
        self.old_file_xpath_list = []
        self.new_file_xpath_list = []
        # 文件名空列表
        self.old_file_name_list = []
        self.new_file_name_list = []
        # 文件后缀空列表
        self.old_file_houzhui_list = []
        self.new_file_houzhui_list = []

        # 清空槽函数
        self.btn_qingkong.clicked.connect(self.qingkong)

        # 预览槽函数
        self.btn_rename.clicked.connect(lambda: self.yulan(self.btn_rename))
        self.btn_tihuan.clicked.connect(lambda: self.yulan(self.btn_tihuan))
        self.btn_charu.clicked.connect(lambda: self.yulan(self.btn_charu))
        self.btn_daxiaoxie.clicked.connect(lambda: self.yulan(self.btn_daxiaoxie))
        self.btn_kuozhanming.clicked.connect(lambda: self.yulan(self.btn_kuozhanming))
        self.btn_baoliuzhongwen.clicked.connect(lambda: self.yulan(self.btn_baoliuzhongwen))

        # 执行槽函数
        self.btn_zhixing.clicked.connect(self.zhixing)

    # 执行槽函数，文件重命名
    def zhixing(self):

        # 表格总行数
        rowCount = self.tableWidget.rowCount()
        # 表格总行数 > 0
        if rowCount > 0:
            # 循环变量
            i = 0
            # 循环变量 < 表格总行数
            while i < rowCount:
                # 获取单元格的值
                old_file_name = self.tableWidget.item(i, 0).text()

                # 获取单元格的值
                new_file_name = self.tableWidget.item(i, 1).text()

                # 旧文件路径
                old_all_xpath = os.path.join(self.old_file_xpath_list[i], old_file_name)
                # print(old_all_xpath)
                # H:/图片/余时锐表情2019\\%7B0S$PI0MG$N998)HTSC$I(M.jpg
                # H:\图片\余时锐表情2019\{0S$PI0MG$N998)HTSC$I(M.jpg

                # 新文件路径
                new_all_xpath = os.path.join(self.old_file_xpath_list[i], new_file_name)
                # print(old_all_xpath)

                try:
                    # 重命名
                    os.rename(old_all_xpath, new_all_xpath)
                    # 成功
                    # 单元格对象（文件名）
                    newItem = QTableWidgetItem('成功')

                    # 表格新增行，加入单元格（行从0开始）,命名成功
                    self.tableWidget.setItem(i, 2, newItem)

                    # 单元格回填
                    # 单元格对象（文件名）
                    newItem = QTableWidgetItem(new_file_name)
                    # 表格新增行，加入单元格（行从0开始）,命名成功
                    self.tableWidget.setItem(i, 0, newItem)

                except:
                    # 失败
                    # 单元格对象（文件名）
                    newItem = QTableWidgetItem('失败')

                    # 表格新增行，加入单元格（行从0开始）,命名成功
                    self.tableWidget.setItem(i, 2, newItem)

                # 循环变量+1
                i += 1

    # 清空槽函数
    def qingkong(self):
        # 删除1行
        # self.tableWidget.removeRow(0)
        # 删除所有行
        self.tableWidget.setRowCount(0)

        # 文件路径空列表
        self.old_file_xpath_list = []
        self.new_file_xpath_list = []
        # 文件名空列表
        self.old_file_name_list = []
        self.new_file_name_list = []
        # 文件后缀空列表
        self.old_file_houzhui_list = []
        self.new_file_houzhui_list = []

    # 预览槽函数
    def yulan(self, btn):
        # 表格总行数
        rowCount = self.tableWidget.rowCount()
        # 表格总行数 > 0
        if rowCount > 0:
            # 循环变量
            i = 0
            # 循环变量 < 表格总行数
            while i < rowCount:

                # 获取单元格的值
                # 如果预览列有值，用预览列的值
                if self.tableWidget.item(i, 1):
                    item_text = self.tableWidget.item(i, 1).text()
                # 预览列无值，用原始值
                else:
                    # 单元格内容，文件名+扩展名，第n行第1列
                    item_text = self.tableWidget.item(i, 0).text()

                # 文件名与扩展名分离
                new_filename, new_kuozhanname = os.path.splitext(item_text)

                # 修改文件名
                # print(self.old_file_xpath_list)
                # print(self.old_file_name_list)
                # print(self.old_file_houzhui_list)

                if btn.text() == '重命名':
                    # 新主文件名
                    le_new_name = self.le_new_name.text()
                    # 开始文件编号
                    sb_start = self.sb_start.value()
                    # 文件增加步长
                    sb_step = self.sb_step.value()
                    # 文件号码位数
                    sb_weishu = self.sb_weishu.value()
                    # 增加位数勾选
                    if self.cb_add.isChecked():
                        new_filename = le_new_name + str(sb_start + sb_step * i).zfill(sb_weishu)
                    else:
                        new_filename = le_new_name

                if btn.text() == '替换':
                    # 查找的
                    le_chazhao = self.le_chazhao.text()
                    # 替换的
                    le_tihuan = self.le_tihuan.text()
                    # 替换文件名
                    new_filename = new_filename.replace(le_chazhao, le_tihuan)

                if btn.text() == '插入':
                    # 新主文件名
                    le_new_name = self.le_new_name.text()
                    # 开始文件编号
                    sb_start = self.sb_start.value()
                    # 文件增加步长
                    sb_step = self.sb_step.value()
                    # 文件号码位数
                    sb_weishu = self.sb_weishu.value()

                    # 插入位置
                    index = self.sb_charuweizhi.value()
                    # 文件名分割
                    # 文件名第一部分
                    new_filename_1 = new_filename[:index]
                    # 文件名第二部分
                    # 增加位数勾选
                    if self.cb_add.isChecked():
                        new_filename_2 = self.le_charuneirong.text() + str(sb_start + sb_step * i).zfill(sb_weishu)
                    else:
                        new_filename_2 = self.le_charuneirong.text()
                    # 文件名第三部分
                    new_filename_3 = new_filename[index:]
                    # 文件名全部
                    new_filename = new_filename_1 + new_filename_2 + new_filename_3

                if btn.text() == '大小写':
                    if self.cb_kaitou_s.isChecked():
                        new_filename = new_filename[0].lower() + new_filename[1:]
                    if self.cb_kaitou_b.isChecked():
                        new_filename = new_filename.title()
                    if self.cb_all_s.isChecked():
                        new_filename = new_filename.lower()
                    if self.cb_all_b.isChecked():
                        new_filename = new_filename.upper()

                if btn.text() == '扩展名':
                    # 查找的
                    le_old_kuozhanname = self.le_old_kuozhanname.text()
                    # 替换的
                    le_new_kuozhanname = self.le_new_kuozhanname.text()
                    # 替换扩展名
                    new_kuozhanname = new_kuozhanname.replace(le_old_kuozhanname, le_new_kuozhanname)

                if btn.text() == '保留中文':
                    # 保留中文
                    pattern = re.compile(r'[^\u4e00-\u9fa5]')
                    new_filename = re.sub(pattern, '', new_filename)

                # 单元格对象（文件名+扩展名）
                newItem = QTableWidgetItem(new_filename + new_kuozhanname)

                # 表格加入单元格（行从0开始），第n行第二列
                self.tableWidget.setItem(i, 1, newItem)

                # 循环变量++
                i += 1

    # 鼠标拖入
    def dragEnterEvent(self, file):
        # self.setWindowTitle('鼠标拖入')

        # 鼠标放开接受
        file.accept()

        # 文件名，去除最后一个字符（换行符）
        file_name = file.mimeData().text()
        # file:///C:/Users/Administrator/Desktop/安卓启动时间v2.exe file:///C:/Users/Administrator/Desktop/随机字符串v8.exe
        # $H%60XM%259EZS$~%25D%7DCWLVVGUY.jpg
        # $H`XM%9EZS$~%D}CWLVVGUY.jpg

        # 字符转换
        file_name = unquote(file_name, 'utf-8')
        # print(file_name)

        # 文件名，通过空格，切分成列表
        file_list = file_name.split('\n')
        # print(file_list)
        # ['file:///C:/Users/Administrator/Desktop/自动化工具箱.lnk',
        # 'file:///C:/Users/Administrator/Desktop/安卓启动时间v2.exe']

        # 遍历列表
        for i in file_list:
            # 如果列表内容有值
            if len(i) > 0:
                # 文件路径空列表
                self.old_file_xpath_list.append(fileFenli(i)['路径'].replace(r'file:///', ''))

                # 文件名空列表
                self.old_file_name_list.append(fileFenli(i)['文件名'].replace(r'file:///', ''))

                # 文件后缀空列表
                self.old_file_houzhui_list.append(fileFenli(i)['后缀'])

                # print(self.old_file_xpath_list)
                # print(self.old_file_name_list)
                # print(self.old_file_houzhui_list)

                # 获取表格行数
                row_num = self.tableWidget.rowCount()

                # 表格增加行（总行数+1）
                self.tableWidget.setRowCount(row_num + 1)

                # 单元格对象（文件名）
                newItem = QTableWidgetItem(fileFenli(i)['文件名'])

                # 表格新增行，加入单元格（行从0开始）
                self.tableWidget.setItem(row_num, 0, newItem)

    # 鼠标放开
    def dropEvent(self, file):
        # self.setWindowTitle('鼠标放开')
        pass

    # 鼠标移入
    def dragMoveEvent(self, file):
        # self.setWindowTitle('鼠标移入')
        pass

# pyinstaller -F -w -i yu.ico main.py
if __name__ == "__main__":
    app = QApplication(sys.argv)
    rename = ReName()
    rename.show()
    sys.exit(app.exec_())
