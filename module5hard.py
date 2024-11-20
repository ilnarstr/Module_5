import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __repr__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __repr__(self):
        return f'{self.title}'

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == hash(user.password):
                self.current_user = nickname

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_video):
        found_videos = [title for title in self.videos if search_video.lower() in str(title).lower()]
        print(found_videos)

    def watch_video(self, name_video):
        if self.current_user == None:
            print('Войдите в аккаунт, чтоб смотреть видео')
        else:
            for video in self.videos:
                if video.title == name_video:
                    if video.adult_mode == True:
                        for user in self.users:
                            if str(self.current_user) == str(user.nickname):
                                if user.age >= 18:
                                    for i in range(video.duration):
                                        video.time_now += 1
                                        print(video.time_now)
                                        time.sleep(1)
                                    print('Конец видео')
                                else:
                                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for i in range(video.duration):
                            video.time_now += 1
                            print(video.time_now)
                            time.sleep(1)
                        print('Конец видео')




if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

    ur.add(v1, v2)

    ur.get_videos('лучший')
    ur.get_videos('ПРОГ')

    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    ur.watch_video('Лучший язык программирования 2024 года!')







    # print(ur.current_user)
    # print(ur.users)
    # ur.log_out()
    # print(ur.current_user)
    # ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
    # print(ur.current_user)





