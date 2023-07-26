def setup_avatar(self):
        cur_path = Path(os.path.join(self.find_path(),'avatar'))
        pixmap = QPixmap(os.path.join(cur_path, "bodies" + "\\" + self.ava_body + '.png'))
        self.ui.AVATAR_BODY.setPixmap(pixmap)
        pixmap = QPixmap(os.path.join(cur_path, "hats" + "\\" + self.ava_hat + '.png'))
        self.ui.AVATAR_HAT.setPixmap(pixmap)
        pixmap = QPixmap(os.path.join(cur_path, "clothes" + "\\" + self.ava_clothes + '.png'))
        self.ui.AVATAR_CLOTHES.setPixmap(pixmap)