import sys
import cv2, qrcode
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from qr import Ui_MainWindow
class Main_ui:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.pushButton_inputlink.clicked.connect(lambda: self.linktoqr())

    def linktoqr(self):
        qr = qrcode.QRCode(version=15, box_size=10, border=5)
        link = str(self.uic.lineEdit_link.text())
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white", size=(300, 300))
        split = link.split("/")
        name_qr = str(split[-1]) + ".png"
        img.save(name_qr)

        image = name_qr
        img = cv2.imread(image)
        resized = cv2.resize(img, (300, 300))
        cv2.imwrite(name_qr, resized)

        pic = QPixmap(name_qr)
        self.uic.label_Qr.setPixmap(pic)
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Main_ui()
    main_win.show()
    sys.exit(app.exec())