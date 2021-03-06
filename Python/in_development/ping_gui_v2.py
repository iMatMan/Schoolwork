# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file
# Initial UI generated with PyQt 5
# Author: Mathias Nygård Evensen
#
# Only works on Windows OS for now
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ip2geotools.databases.noncommercial import DbIpCity
from queue import Queue
import urllib.request
import time
import os
import re
import socket
import subprocess
import ipaddress
import threading
import speedtest
import nmap3
import pprint

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(560, 450)
        Dialog.setMinimumSize(QtCore.QSize(560, 450))
        Dialog.setMaximumSize(QtCore.QSize(560, 450))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        # Removes windows question mark for "what is this"
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowTitleHint)
        Dialog.setToolTipDuration(-1)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("color: rgb(0, 0, 0);\n"
                             "border-color: rgb(136, 136, 136);\n"
                             "background-color: rgb(90, 90, 90);")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 321, 31))
        self.lineEdit.setMinimumSize(QtCore.QSize(321, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(212, 212, 212);")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 81, 23))
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(212, 212, 212);")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 50, 91, 23))
        self.pushButton_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(212, 212, 212);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 15, 91, 23))
        self.pushButton_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(212, 212, 212);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 90, 391, 351))
        self.textEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(212, 212, 212);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 90, 91, 23))
        self.pushButton_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(212, 212, 212);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 120, 91, 23))
        self.pushButton_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(212, 212, 212);")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 150, 91, 23))
        self.pushButton_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(212, 212, 212);")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 50, 81, 23))
        self.pushButton_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(212, 212, 212);")
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(477, 10, 81, 23))
        self.pushButton_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(212, 212, 212);")
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 50, 91, 23))
        self.pushButton_9.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(212, 212, 212);")
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(410, 180, 91, 23))
        self.pushButton_10.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(212, 212, 212);")
        self.pushButton_10.setObjectName("pushButton_10")

        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(430, 420, 118, 23))
        self.progressBar.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.run_ping)
        self.pushButton_2.clicked.connect(self.multi_ping)
        self.pushButton_3.clicked.connect(self.clear_text)
        self.pushButton_4.clicked.connect(self.get_public_ip)
        self.pushButton_5.clicked.connect(self.measure_speed)
        self.pushButton_6.clicked.connect(self.get_ip)
        self.pushButton_7.clicked.connect(self.port_scanner)
        self.pushButton_8.clicked.connect(self.show_popup)
        self.pushButton_9.clicked.connect(self.os_detect)
        self.pushButton_10.clicked.connect(self.detect_all_network)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Network Tool"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Write IP or command here"))

        self.pushButton.setToolTip(_translate("Dialog", "Write the desired IP you want to ping"))
        self.pushButton.setText(_translate("Dialog", "Ping IP"))

        self.pushButton_2.setToolTip(_translate("Dialog", "EX: 192.168.1.0/24"))
        self.pushButton_2.setText(_translate("Dialog", "Ping All /24"))

        self.pushButton_3.setToolTip(_translate("Dialog", "Clears both input and output"))
        self.pushButton_3.setText(_translate("Dialog", "Clear All Text"))

        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                   "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                                   "/><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                                   "font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                   "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                   "-qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br "
                                                   "/></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "Output"))

        self.pushButton_4.setToolTip(_translate("Dialog", "Retrieves your public IP address"))
        self.pushButton_4.setText(_translate("Dialog", "Get Public IP"))

        self.pushButton_5.setToolTip(_translate("Dialog", "Performs a speedtest from speedtest.net"))
        self.pushButton_5.setText(_translate("Dialog", "Speedtest"))

        self.pushButton_6.setToolTip(_translate("Dialog", "Retrieves your local IP address"))
        self.pushButton_6.setText(_translate("Dialog", "Your local IP"))

        self.pushButton_7.setToolTip(_translate("Dialog", "Port scan of open ports on specified IP"))
        self.pushButton_7.setText(_translate("Dialog", "Port scan"))

        self.pushButton_8.setToolTip(_translate("Dialog", "Gives a popup box with help"))
        self.pushButton_8.setText(_translate("Dialog", "Information"))

        self.pushButton_9.setToolTip(_translate("Dialog", "OS detection of specified IP"))
        self.pushButton_9.setText(_translate("Dialog", "OS detection"))

        self.pushButton_10.setToolTip(_translate("Dialog", "Retrieves all IP's on network with /24"))
        self.pushButton_10.setText(_translate("Dialog", "Get all hosts"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("All buttons are explained in the details section under!")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Close)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("Creator: Mathias Nygård Evensen\n"
                               "License: ---\n"
                               "Version: 2")

        msg.setDetailedText("details")
        msg.exec_()

    def clear_text(self):
        self.lineEdit.clear()
        self.textEdit.clear()

    def get_ip(self):
        def callback():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                # doesn't even have to be reachable
                s.connect(('10.255.255.255', 1))
                IP = s.getsockname()[0]
            except Exception:
                IP = '127.0.0.1'
            finally:
                s.close()
            self.textEdit.append("Your local IP: " + IP)

        t = threading.Thread(target=callback)
        t.start()

    def detect_all_network(self):
        def callback():
            global IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                # doesn't even have to be reachable
                s.connect(('10.255.255.255', 1))
                IP = s.getsockname()[0]
            except Exception:
                IP = '127.0.0.1'
            finally:
                s.close()
                print_lock = threading.Lock()

                net_addr = str(".".join(IP.split('.')[0:-1]) + '.'+'0'+'/24')
                start_time = time.time()
                ip_net = ipaddress.ip_network(net_addr)
                all_hosts = list(ip_net.hosts())
                info = subprocess.STARTUPINFO()
                info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                info.wShowWindow = subprocess.SW_HIDE

                print('Sweeping Network with ICMP: ', net_addr)
                self.textEdit.append('Sweeping the network with ICMP: ' + str(net_addr) + '\n')

                def pingsweep(ip):
                    response = \
                        subprocess.Popen(['ping', '-n', '1', '-w', '600', str(all_hosts[ip])],
                                         stdout=subprocess.PIPE,
                                         startupinfo=info).communicate()[0]

                    with print_lock:
                        print('\033[93m', end='')
                        # code logic if we have/don't have good response
                        if "Reply" in response.decode('utf-8'):
                            print(str(all_hosts[ip]), '\033[32m' + "is Online")
                            self.textEdit.append(str(all_hosts[ip]))
                        elif "Destination host unreachable" in response.decode('utf-8'):
                            # print(str(all_hosts[ip]), '\033[90m'+"is Offline (Unreachable)")
                            pass
                        elif "Request timed out" in response.decode('utf-8'):
                            # print(str(all_hosts[ip]), '\033[90m'+"is Offline (Timeout)")
                            pass
                        else:
                            print("UNKNOWN", end='')
                            self.textEdit.append("UNKNOWN")

                def threader():
                    while True:
                        worker = q.get()
                        pingsweep(worker)
                        q.task_done()

                q = Queue()

                for x in range(64):
                    th = threading.Thread(target=threader)
                    th.daemon = True
                    th.start()

                for worker in range(len(all_hosts)):
                    q.put(worker)

                q.join()

                runtime = float("%0.2f" % (time.time() - start_time))
                print("Run Time: ", runtime, "seconds")
                self.textEdit.append("\nThe IP's listed above are online:\nRun Time: " + str(runtime) + " seconds")

        t = threading.Thread(target=callback)
        t.start()

    def run_ping(self):
        text_input = self.lineEdit.text()
        self.textEdit.clear()
        def callback():
            if len(text_input) == 0:
                self.textEdit.append("You have to write an IP : EX(192.168.1.1)\n")
            else:
                self.textEdit.append("Pinging: " + text_input + "\n")
                ping = os.popen('ping ' + text_input).read()
                self.textEdit.append(ping)

        t = threading.Thread(target=callback)
        t.start()

    def os_detect(self):
        text_input = self.lineEdit.text()
        self.textEdit.clear()
        def callback():
            self.textEdit.append('Performing OS scan on: ' + str(text_input) + '\n')
            nmap = nmap3.Nmap()
            version_result = nmap.nmap_version_detection(text_input)
            # pprint.pprint(version_result, width=61)

            try:
                self.textEdit.append('Port       : ' + str(version_result[0]['port']))
                self.textEdit.append('Protocol  : ' + str(version_result[0]['protocol']))
                self.textEdit.append('Reason   : ' + str(version_result[0]['reason']))
                self.textEdit.append('Method   : ' + str(version_result[0]['service']['method']))
                self.textEdit.append('OS type  : ' + str(version_result[0]['service']['ostype']))
            except (IndexError, KeyError):
                self.textEdit.append('Could not detect OS')
            try:
                if str(version_result[0]['service']['ostype']) == 'Linux':
                    self.textEdit.append('Conn    : ' + str(version_result[0]['service']['name']))
                    self.textEdit.append('Product : ' + str(version_result[0]['service']['product']))
                    self.textEdit.append('Version : ' + str(version_result[0]['service']['version']))
            except:
                self.textEdit.append('Error retrieving values or timed out')

        t = threading.Thread(target=callback)
        t.start()

    def get_public_ip(self):
        self.textEdit.clear()
        def callback():
            filtered_list_ip = ['ip']
            def seek_keys(d, key_list):
                for k, v in d.items():
                    if k in key_list:
                        if isinstance(v, dict):
                            #print(k + ": " + list(v.keys())[0])
                            self.textEdit.append(k + ": " + list(v.keys())[0])
                        else:
                            # print(k + ": " + str(v))
                            self.textEdit.append(k + ": " + str(v))
                    if isinstance(v, dict):
                        seek_keys(v, key_list)

            self.textEdit.append("Retrieving public ip address: \n")
            try:
                s = speedtest.Speedtest()
                s.get_servers()
                s.get_best_server()
                s.get_config()
                res = s.results.dict()
                seek_keys(res, filtered_list_ip)
            except:
                self.textEdit.append("Could not access server")

        t = threading.Thread(target=callback)
        t.start()

    def measure_speed(self):
        self.textEdit.clear()
        def callback():
            global response, res
            try:
                dataip = re.search('"([0-9.]*)"',
                                   urllib.request.urlopen("http://ip.jsontest.com/").read().decode('utf-8')).group(1)
                response = DbIpCity.get(dataip, api_key='free')
            except:
                self.textEdit.append('Could not retrieve location data')
            filtered_list = ['cc', 'host', 'ip', 'isp']
            def seek_keys(d, key_list):
                for k, v in d.items():
                    if k in key_list:
                        if isinstance(v, dict):
                            # print(k + ": " + list(v.keys())[0])
                            self.textEdit.append(k + ': ' + list(v.keys())[0] + '\n')
                        else:
                            # print(k + ": " + str(v))
                            self.textEdit.append(k + ': ' + str(v) + '\n')
                    if isinstance(v, dict):
                        seek_keys(v, key_list)

            self.textEdit.append("Running speedtest. Please wait.\n")
            try:
                s = speedtest.Speedtest()
                s.get_servers()
                s.get_best_server()
                s.download()
                s.upload()
                res = s.results.dict()
                seek_keys(res, filtered_list)
            except:
                self.textEdit.append("Could not access speedtest")

            self.textEdit.append('city: ' + response.city + '\nstate: ' + response.region + '\n'+
                                     '\nDownload: {:.2f} Mbps/s'.format(res["download"] / 1024 / 1024) +
                                     '\nUpload: {:.2f} Mbps/s'.format(res["upload"] / 1024 / 1024) +
                                     '\nPing: {}'.format(res["ping"]) + ' ms')

        t = threading.Thread(target=callback)
        t.start()

    def port_scanner(self):
        text_input = self.lineEdit.text()
        self.textEdit.clear()
        def callback():
            if len(text_input) == 0:
                self.textEdit.append("You have to write an IP : EX(192.168.1.1)\n")
            else:
                try:
                    socket.setdefaulttimeout(0.6)
                    print_lock = threading.Lock()

                    t_IP = socket.gethostbyname(text_input)
                    self.textEdit.append('Starting scan on host: ' + str(text_input) + '\n')
                except:
                    self.textEdit.append('Error')

                def portscan(port):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    try:
                        conn = s.connect((t_IP, port))
                        with print_lock:
                            self.textEdit.append(str(port) + ' is open')
                        conn.close()
                    except:
                        pass

                def threader():
                    while True:
                        worker = q.get()
                        portscan(worker)
                        q.task_done()

                q = Queue()
                start_time = time.time()

                for x in range(64):
                    th = threading.Thread(target=threader)
                    th.daemon = True
                    th.start()

                for worker in range(1, 500):
                    q.put(worker)

                q.join()
                runtime = float("%0.2f" % ( time.time() - start_time))
                self.textEdit.append("\nRun Time: " + str(runtime) + " seconds")

        t = threading.Thread(target=callback)
        t.start()

    def multi_ping(self):
        text_input = self.lineEdit.text()
        self.textEdit.clear()
        if len(text_input) == 0:
            self.textEdit.append("You have to write an IP : EX(192.168.1.0)\n")
        else:
            print_lock = threading.Lock()
            net_addr = str(".".join(text_input.split('.')[0:-1]) + '.' + '0/24')
            #net_addr = str(text_input)
            start_time = time.time()
            ip_net = ipaddress.ip_network(net_addr)
            all_hosts = list(ip_net.hosts())
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            info.wShowWindow = subprocess.SW_HIDE

            print('Sweeping Network with ICMP: ', net_addr)
            self.textEdit.append('Sweeping the network with ICMP: ' + str(net_addr) + '\n')

            def pingsweep(ip):
                response = \
                    subprocess.Popen(['ping', '-n', '1', '-w', '600', str(all_hosts[ip])], stdout=subprocess.PIPE,
                                     startupinfo=info).communicate()[0]

                with print_lock:
                    # code logic if we have/don't have good response
                    if "Reply" in response.decode('utf-8'):
                        print(str(all_hosts[ip]), "is Online")
                        self.textEdit.append(str(all_hosts[ip]))
                        """ip_to_int = int(ipaddress.IPv4Address(all_hosts[ip]))
                        ip_to_list = [ip_to_int]
                        test = str(ip_to_list)[1:-1]
                        test = int(test)
                        ip_to_string = str(ipaddress.IPv4Address(test))
                        print(ip_to_string)"""
                    elif "Destination host unreachable" in response.decode('utf-8'):
                        # print(str(all_hosts[ip]), '\033[90m'+"is Offline (Unreachable)")
                        pass
                    elif "Request timed out" in response.decode('utf-8'):
                        # print(str(all_hosts[ip]), '\033[90m'+"is Offline (Timeout)")
                        pass
                    else:
                        print("UNKNOWN", end='')
                        self.textEdit.append("UNKNOWN")

            def threader():
                while True:
                    worker = q.get()
                    pingsweep(worker)
                    q.task_done()

            q = Queue()

            for x in range(32):
                th = threading.Thread(target=threader)
                th.daemon = True
                th.start()

            for worker in range(len(all_hosts)):
                q.put(worker)

            q.join()

            runtime = float("%0.2f" % (time.time() - start_time))
            print("Run Time: ", runtime, "seconds")
            self.textEdit.append("\nThe IP's listed above are online:\nRun Time: " + str(runtime) + " seconds")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
