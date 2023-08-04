wanted_path = os.path.join(self.find_path(),'info.txt')
        with open(wanted_path) as info_file:
            for line in info_file:
                list = (re.split(':|\n', line))
                print(list)
                match list[0]:
                    case "streak":
                        self.streak = list[1]
                    case "points":
                        self.user_points = list[1]
                    case "ava_hat":
                        self.ava_hat = list[1]
                    case "ava_body":
                        self.ava_body = list[1]
                    case "ava_clothes":
                        self.ava_clothes = list[1]
        info_file.close()